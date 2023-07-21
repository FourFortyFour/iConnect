# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app, db
from flask import Flask, jsonify, request, Response
import stripe

initialize_app()
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
        #have to import stripe
        event = stripe.Event.construct_from(
            event_payload, stripe.api_key
        )
    except ValueError as e:
        print("Something went wrong")
        return Response(status=404, response="Invalid payload")
        # Invalid payload

    if event.type == "payment_intent.succeeded":
        #make a new order doc in firestore, will have to extract data
        #email the user, will have to collect info here
        print("Payment intent successful")
        pass
    elif event.type == "payment_intent.attached":
        pass
    else:
        #unhandled event
        pass

    return  Response(status=200, response="Something happened")
    

#Exposing the flask app
@https_fn.on_request()
def flask_endpoints(req):
    with app.request_context(req.environ):
        return app.full_dispatch_request()