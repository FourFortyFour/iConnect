from dotenv import load_dotenv
from flask import Flask, send_from_directory, render_template, request, jsonify
import stripe
import os

load_dotenv()
app = Flask(__name__)

stripe_keys = {
    "pub_key": os.environ.get("STRIPE_PUBLISHABLE_KEY"),
    "secret_key": os.environ.get("STRIPE_SECRET_KEY"),
}
stripe.api_key = stripe_keys["secret_key"]
# print(os.environ.get("STRIPE_PUBLISHABLE_KEY"))


@app.route("/")
def root():
    return send_from_directory("../iconnect-frontend/src", "app.html")


@app.route("/pay", methods=["POST"])
def process_payment():
    ...


# @app.route("/<path:path>")
# def assets(path):
#     return send_from_directory("../iconnect-frontend/dist", path)


# @app.route("/<path:path>")
# def home(path):
#     return send_from_directory("iconnect-frontend/public", path)


# @app.route("/time")
# def get_current_time():
#     return {"time": time.time()}
