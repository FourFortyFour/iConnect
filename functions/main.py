from flask import Flask, request, Response
from firebase_functions import https_fn, options
from utils import initialized_stripe as stripe, webhook_sk
import event_handler


app = Flask(__name__)


stripe.api_version = "2022-11-15"


def make_event(req_data: str, sign_header: str, webhook_sk: str) -> stripe.Event:
    try:
        return stripe.Webhook.construct_event(req_data, sign_header, webhook_sk)
    except stripe.error.SignatureVerificationError as e:
        print(f"- Webhook signature verification failed: {str(e)}")
        return None
    except ValueError as e:
        print(f"- Webhook construction failed: {str(e)}")
        return None


@app.route("/paymentwebhook", methods=["POST"])
def event_receiver() -> Response:
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
        # event_handler.proc_payment(
        #     event.data, live=True
        # ) if app.debug else event_handler.proc_payment(event.data, live=True)
        event_handler.proc_payment(event.data, live=True)
        return Response(status=200, response="payment successful")
    elif isinstance(event, stripe.Event) and event.type == "payment_intent.created":
        return Response(status=200, response="payment intent started")

    return Response(status=200, response="Event processed")


# Exposing the flask app to accept http requests from stripe webhook
# i.e. payment_intent events
@https_fn.on_request(
    cors=options.CorsOptions(cors_origins="*", cors_methods=["get", "post"]),
    region="europe-west1",
)
def paymentwebhook(req: https_fn.Request) -> https_fn.Response:
    # https://cloud.google.com/functions/docs/concepts/execution-environment?hl=en#functions-concepts-scopes-python
    # Potential future optimization: "A single function invocation results in execution of only the body of the function declared as the entry point"
    with app.request_context(req.environ):
        return app.full_dispatch_request()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
    )
