from firebase_functions import https_fn
from firebase_admin import initialize_app, firestore, credentials
from flask import Flask, jsonify, request, Response
import stripe

# "C:\\Users\\AsusOne\\iconnect-86ebb-firebase-adminsdk-15haq-aac73db15f.json"

cred = credentials.Certificate("")

fire_app = initialize_app(cred)
db = firestore.client()
stripe.api_key = "sk_test_51KxejGD27b5b7CLZonHYNPNf3a4YGSYFGSo7qGThNX9ryPZDumT1eaTbQgiplH6G0A6RsWDwDqpP8nnbsNGNnLMb00iqmNuqza"
app = Flask(__name__)


@app.get("/test")
def test_get():
    data = request.get_json()

    if "name" in data.keys():
        response = {"response": f"Hello {data['name']}"}
        response = jsonify(response)
        return response
    else:
        return Response(status=200, response="Hello wonderful person")


@app.post("/payment_done")
def payment_webhook():
    event_payload = request.get_json()
    try:
        # have to import stripe
        event = stripe.Event.construct_from(event_payload, stripe.api_key)
    except ValueError as e:
        print("Something went wrong")
        return Response(status=404, response="Invalid payload")
        # Invalid payload

    if event.type == "payment_intent.succeeded":
        # make a new order doc in firestore, will have to extract data
        # email the user, will have to collect info here
        amount = event.data["object"]["amount"]
        charges = event.data["object"]["charges"]["data"][0]
        billing_details = charges["billing_details"]
        name = billing_details["name"]
        email = billing_details["email"]

        doc = {"name": name, "email": email, "price": amount / 100}

        print(
            f"Payment intent successful for {name} of amount {amount / 100} with email {email}"
        )
        db.collection("orders").add(doc)

        pass
    elif event.type == "payment_intent.attached":
        pass
    else:
        # unhandled event
        pass

    return Response(status=200, response="Something happened")


# Exposing the flask app
@https_fn.on_request()
def flask_endpoints(req):
    with app.request_context(req.environ):
        return app.full_dispatch_request()
