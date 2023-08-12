from flask import Flask, request, Response
from firebase_functions import https_fn
from utils import initialized_stripe as stripe, webhook_sk
import event_handler

app = Flask("internal")


def make_event(req_data: str, sign_header: str, webhook_sk: str) -> stripe.Event:
    try:
        return stripe.Webhook.construct_event(req_data, sign_header, webhook_sk)
    except stripe.error.SignatureVerificationError as e:
        print(f"- Webhook signature verification failed: {str(e)}")
        return None
    except ValueError as e:
        print(f"- Webhook construction failed: {str(e)}")
        return None


@app.route("/payment_done", methods=["POST"])
def payment_webhook() -> Response:
    req_data = request.get_data(as_text=True)
    event = request.get_json()
    sign_header = request.headers.get("stripe-signature")

    if webhook_sk is None:
        return Response(status=400, response="Invalid endpoint secret key")

    event = make_event(req_data, sign_header, webhook_sk)

    if event is None:
        return Response(
            status=400, response="Event construction failed, invalid payload"
        )
    elif isinstance(event, stripe.Event) and event.type == "payment_intent.succeeded":
        event_handler.proc_payment(event.data)
        return Response(status=200, response="payment successful")
    elif isinstance(event, stripe.Event) and event.type == "payment_intent.created":
        return Response(status=200, response="payment intent started")

    return Response(status=200, response="Event processed")


# Exposing the flask app
@https_fn.on_request()
def webhook_runner(req: https_fn.Request) -> https_fn.Response:
    with app.request_context(req.environ):
        return app.full_dispatch_request()


if __name__ == "__main__":
    app.run()
