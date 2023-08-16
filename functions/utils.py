from firebase_admin import initialize_app, firestore
import stripe
import re
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_EMAIL_TEMPLATE = {
    "to": "",
    "message": {
        "subject": "Order Confirmation from iConnect",
        "html": """
            <html>
                <head>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            padding: 20px;
                            background-color: #f5f7f9;
                        }}
                        .container {{
                            background-color: #ffffff;
                            padding: 20px;
                            border-radius: 8px;
                        }}
                        h2 {{
                            color: #2c3e50;
                        }}
                        p {{
                            font-size: 16px;
                            color: #2c3e50;
                        }}
                        strong {{
                            color: #FF8A33;
                        }}
                        a {{
                            color: #2980b9;
                        }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h2>Thank you {name} for your order of our google review cards!</h2>
                        <p>
                            You've ordered <strong>{product_quantity} {product_name}(s)</strong>.
                            The company name or URL you provided is: <strong>{company_name_url}</strong>.
                        </p>
                        <p>
                            Your order will be shipped to: {line1}, {line2}.
                        </p>
                        <p>
                            Provided contact details: {phone}, {user_email}.
                            <br>
                            For any queries regarding your order, please contact us at <a href="mailto:iconnect@pathfinder.ink">iconnect@pathfinder.ink</a>, or call <a href="tel:+971506691656">+971506691656</a>.
                        </p>
                    </div>
                </body>
            </html>
        """,
    },
}

INTERNAL_EMAIL_TEMPLATE = {
    "to": "",
    "message": {
        "subject": "New Order Alert!",
        "html": """
            <html>
                <head>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            padding: 20px;
                            background-color: #f5f7f9;
                        }}
                        .container {{
                            background-color: #ffffff;
                            padding: 20px;
                            border-radius: 8px;
                        }}
                        h2 {{
                            color: #2c3e50;
                        }}
                        p {{
                            font-size: 16px;
                            color: #34495e;
                        }}
                        strong {{
                            color: #FF8A33;
                        }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h2>New order from {name}</h2>
                        <p>
                            Order details: <strong>{product_quantity} {product_name}(s)</strong>.
                        </p>
                        <p>
                            Delivery location:
                            <br><strong>{line1}, {line2}, {state}, {country}</strong>.
                        </p>
                        <p>
                            Customer's provided Company name and/or URL: <strong>{company_name_url}</strong>.<br>
                            Customer Contact details: <strong><a href="tel:{phone}">{phone}</a>, {user_email}</strong>.
                        </p>
                    </div>
                </body>
            </html>
        """,
    },
}


def initialize_firebase():
    # cred = credentials.Certificate(os.environ.get("FIREBASE_ADMIN_CRED"))
    initialize_app()
    return firestore.client()


def initialize_stripe():
    stripe.api_key = os.environ.get("STRIPE_LIVE_KEY_E")
    return stripe


webhook_sk = os.environ.get("STRIPE_LIVEWEBHOOK_KEY")
db = initialize_firebase()
initialized_stripe = initialize_stripe()


def is_arabic(text: str) -> bool:
    arabic_pattern = re.compile(
        r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]+"
    )
    return bool(arabic_pattern.search(text))
