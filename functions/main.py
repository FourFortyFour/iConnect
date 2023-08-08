from firebase_functions import https_fn
from firebase_admin import initialize_app, firestore, credentials
from flask import Flask, request, Response
import stripe
import re
import os
from dotenv import load_dotenv


load_dotenv()

cred = credentials.Certificate(os.environ.get("FIREBASE_ADMIN_CRED"))
fire_app = initialize_app()
db = firestore.client()
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")
app = Flask("internal")
webhook_sk = os.environ.get("STRIPE_WEBHOOK_KEY")


test_email = lambda e: db.collection("icon_mail").add(e)


def is_arabic(text: str) -> bool:
    arabic_pattern = re.compile(
        r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]+"
    )
    return bool(arabic_pattern.search(text))


def make_event(req_data: str, sign_header: str, webhook_sk: str) -> stripe.Event:
    try:
        return stripe.Webhook.construct_event(req_data, sign_header, webhook_sk)
    except stripe.error.SignatureVerificationError as e:
        print(f"Webhook signature verification failed: {str(e)}")
        return None
    except ValueError as e:
        print(f"Webhook construction failed: {str(e)}")
        return None


def proc_payment(data: dict):
    # make a new order doc in firestore, will have to extract data
    # email the user, will have to collect info here
    # print(f"Processing payment for {data}")
    doc = {}
    try:
        customer_details = data["object"]["shipping"]
        metadata = data["object"]["metadata"]
    except:
        print("Error processing payment")
        doc["message"] = "Error processing data payload"
        db.collection("orders").add(doc)
        return -1

    address = customer_details["address"]
    state = address["state"]
    country = address["country"]
    line1 = address["line1"]
    line2 = address["line2"]
    name = customer_details["name"]
    email = metadata["user_email"]
    quantity = metadata["product_quantity"]
    product = metadata["product_name"]
    phone = customer_details["phone"]
    doc = {
        "name": name,
        "email": email,
        "quantity": quantity,
        "state": state,
        "country": country,
        "line1": line1,
        "line2": line2,
        "phone": phone,
        "product": product,
    }

    client_email = {
        "to": email,
        "message": {
            "subject": "Order Confirmation",
            "text": f"Thank you {name} for your order of {quantity} {product}(s)! \n\n(this is a test email generated by the server)",
        },
    }
    internal_email = {
        "to": "abdullabloushi@gmail.com",
        "message": {
            "subject": f"New Order",
            "text": f"New order from {name} for {quantity} {product}(s)! With location {line1}, {line2}, {state}, {country}",
        },
    }

    # test_email(client_email)
    # db.collection("orders").add(doc)


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
        proc_payment(event.data)
        return Response(status=200, response="payment successful")
    elif isinstance(event, stripe.Event) and event.type == "payment_intent.created":
        return Response(status=200, response="payment intent started")

    return Response(status=200, response="Event processed")


# Exposing the flask app
@https_fn.on_request()
def webhook_runner(req: https_fn.Request) -> https_fn.Response:
    with app.request_context(req.environ):
        return app.full_dispatch_request()
