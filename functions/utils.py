from firebase_admin import initialize_app, firestore, credentials
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
                <body>
                    <h2>Thank you {name} for your order!</h2>
                    <p>
                        You've ordered <strong>{product_quantity} {product_name}(s)</strong>.
                    </p>
                    <p>
                        Your order will be shipped to:
                        <br>{line1}, {line2}.
                    </p>
                    <p>
                        Provided contact details: {phone}, {user_email}.
                        <br>
                        For any queries regarding your order, please contact us at <a href="mailto:iconnect@pathfinder.ink">iconnect@pathfinder.ink</a>, or call +971506691656.
                    </p>
                </body>
            </html>
        """,
    },
}

INTERNAL_EMAIL_TEMPLATE = {
    "to": [],
    "message": {
        "subject": "New Order Alert!",
        "html": """
            <html>
                <body>
                    <h2>New order from {name}</h2>
                    <p>
                        Order details: <strong>{product_quantity} {product_name}(s)</strong>.
                    </p>
                    <p>
                        Delivery location:
                        <br>{line1}, {line2}, {state}, {country}.
                    </p>
                    <p>
                        Contact details: {phone}, {user_email}.
                    </p>
                </body>
            </html>
        """,
    },
}


def initialize_firebase():
    cred = credentials.Certificate(os.environ.get("FIREBASE_ADMIN_CRED"))
    initialize_app(credential=cred)
    return firestore.client()


def initialize_stripe():
    stripe.api_key = os.environ.get("STRIPE_SECRET_KEY_E")
    return stripe


webhook_sk = os.environ.get("STRIPE_WEBHOOK_KEY_E")
db = initialize_firebase()
initialized_stripe = initialize_stripe()


def is_arabic(text: str) -> bool:
    arabic_pattern = re.compile(
        r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]+"
    )
    return bool(arabic_pattern.search(text))
