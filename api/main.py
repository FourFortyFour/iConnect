# from dotenv import load_dotenv
from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route("/")
def root():
    return send_from_directory("../iconnect-frontend/src", "app.html")


# @app.route("/<path:path>")
# def assets(path):
#     return send_from_directory("../iconnect-frontend/dist", path)


# @app.route("/<path:path>")
# def home(path):
#     return send_from_directory("iconnect-frontend/public", path)


# @app.route("/time")
# def get_current_time():
#     return {"time": time.time()}
