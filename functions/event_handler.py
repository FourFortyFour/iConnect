from utils import (
    initialized_stripe as stripe,
    db,
    CLIENT_EMAIL_TEMPLATE,
    INTERNAL_EMAIL_TEMPLATE,
)


def add_doc(collection: str, data: dict) -> None:
    db.collection(collection).add(data)


def extract_data(data: dict) -> dict:
    try:
        customer_shipping_details = data.get("object").get("shipping")
        metadata = data.get("object").get("metadata")
        address = customer_shipping_details.get("address")

        order_data_keymap = {
            "name": customer_shipping_details,
            "user_email": metadata,
            "company_name_url": metadata,
            "product_quantity": metadata,
            "state": address,
            "country": address,
            "line1": address,
            "line2": address,
            "product_name": metadata,
        }
        order_data = {
            key: source.get(key)
            for key, source in order_data_keymap.items()
            if key in source
        }

        checkout_session = stripe.checkout.Session.list(
            payment_intent=data.get("object").get("payment_intent")
        )
        order_data["phone"] = checkout_session["data"][0]["customer_details"]["phone"]

        if all(order_data.values()):
            return order_data
    except Exception as e:
        print(f"- Error extracting data: {str(e)}")
    print("- Error retrieving all the required data from event payload")
    return None


def proc_payment(data: dict, live: bool = False) -> None:
    order_data = extract_data(data)
    print(f"Extracted data: {order_data}")
    if order_data is None:
        return None

    client_email = CLIENT_EMAIL_TEMPLATE.copy()
    client_email["to"] = order_data["user_email"]
    client_email["message"]["html"] = client_email["message"]["html"].format(
        **order_data
    )

    internal_email = INTERNAL_EMAIL_TEMPLATE.copy()
    internal_email["message"]["html"] = internal_email["message"]["html"].format(
        **order_data
    )
    internal_recipients = [
        "iconnect@pathfinder.ink",
        "eaaa1875@gmail.com",
        "suhaib.athar@gmail.com",
    ]

    if live:
        print(f"Sending confirmation mail to {client_email['to']}")
        add_doc("icon_mail", client_email)
        add_doc("orders", order_data)
        for r in internal_recipients:
            internal_email["to"] = r
            add_doc("icon_mail", internal_email)
