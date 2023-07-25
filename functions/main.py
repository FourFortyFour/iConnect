from firebase_functions import https_fn
from firebase_admin import initialize_app, firestore, credentials
from flask import Flask, jsonify, request, Response
import stripe
from dotenv import load_dotenv
import os

load_dotenv()

cred = credentials.Certificate(os.environ.get("FIREBASE_ADMIN_CRED"))

fire_app = initialize_app(cred)
db = firestore.client()
stripe.api_key = os.environ.get("STRIPE_PUBLISHABLE_KEY")
app = Flask("internal")
endpoint_sk = os.environ.get("STRIPE_WEBHOOK_KEY")
print(endpoint_sk)


def make_event(req_data: str, sign_header: str, endpoint_sk: str) -> stripe.Event:
    try:
        return stripe.Webhook.construct_event(req_data, sign_header, endpoint_sk)
    except stripe.error.SignatureVerificationError as e:
        print("⚠️  Webhook signature verification failed. " + str(e))
        return None


def proc_payment(data: dict) -> None:
    # make a new order doc in firestore, will have to extract data
    # email the user, will have to collect info here
    print(data)
    # amount = data["object"]["amount"]
    # charges = data["object"]["charges"]["data"][0]
    # billing_details = charges["billing_details"]
    # name = billing_details["name"]
    # email = billing_details["email"]

    # doc = {"name": name, "email": email, "price": amount / 100}

    # print(
    #     f"Payment intent successful for {name} of amount {amount / 100} with email {email}"
    # )
    # db.collection("orders").add(doc)


@app.route("/payment_done", methods=["POST"])
def payment_webhook() -> Response:
    req_data = request.get_data(as_text=True)
    event = None

    # try:
    #     event = request.get_json()
    #     # have to import stripe
    #     # event = stripe.Event.construct_from(event_payload, stripe.api_key)
    # except:
    #     print("Something went wrong")
    #     return Response(status=404, response="Invalid payload")
    #     # Invalid payload
    event = request.get_json()
    if endpoint_sk:
        sign_header = request.headers.get("stripe-signature")
        event = make_event(req_data, sign_header, endpoint_sk)

    if event and event.type == "payment_intent.succeeded":
        proc_payment(event.data)
        return Response(status=200, response="payment successful")
    return Response(status=404, response="Invalid payload")


# Exposing the flask app
@https_fn.on_request()
def webhookrunner(req: https_fn.Request) -> https_fn.Response:
    with app.request_context(req.environ):
        return app.full_dispatch_request()
