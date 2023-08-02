import { db } from '../../lib/firebase.js';
import { doc, getDoc } from "firebase/firestore";
import { redirect } from "@sveltejs/kit";
import { Stripe } from "stripe";
import { STRIPE_SECRET_KEY } from "$env/static/private";


export const prerender = false;
<<<<<<< HEAD
export async function load({ params }) {

    const productRef = doc(db, "products", "ic-1");
    const docSnap = await getDoc(productRef);

    if (docSnap.exists()) {
        return {product: docSnap.data()}
    } else {
        console.log('Product data not found');
    }

}
=======

// export function load({ params }) { }
// This will need to be changed securely to the live secret key in production
>>>>>>> f8f11d73d0e3adf6db4898a860d03aa0da8fa975

const stripe = Stripe(
  STRIPE_SECRET_KEY
);

console.log(process.env.STRIPE_SECRET_KEY)

export const actions = {
  pay: async ({ request }) => {
    const data = await request.formData();
    const email = data.get("email");
    const quantity = data.get("quantity");

    const session = await stripe.checkout.sessions.create({
      line_items: [
        {
          price_data: {
            currency: "aed",
            product_data: {
              name: "ic-card",
            },
            unit_amount: 20000,
          },
          quantity: quantity,
        },
      ],
      phone_number_collection: {
        enabled: true,
      },
      mode: "payment",
      customer_email: email,
      payment_intent_data: {
        metadata: {
          user_email: email,
          product_quantity: quantity,
          product_name: "ic-card",
        },
      },
      success_url: "http://localhost:5173/placed",
      cancel_url: "http://localhost:5173/bad_checkout",
      shipping_address_collection: {
        allowed_countries: ["AE"],
      },
    });
    throw redirect(303, session.url);
  },
};
