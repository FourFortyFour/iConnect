import { db } from '../../lib/firebase.js';
import { doc, getDoc } from "firebase/firestore";
import { redirect } from "@sveltejs/kit";
import { Stripe } from "stripe";
import { STRIPE_LIVE_KEY } from "$env/static/private";

export const prerender = false;
export async function load({ params }) {

  const productRef = doc(db, "products", "ic-1");
  const docSnap = await getDoc(productRef);

  if (docSnap.exists()) {
    return { product: docSnap.data() }
  } else {
    console.log('Product data not found');
  }

}

const stripe = Stripe(STRIPE_LIVE_KEY);

const baseUrl = import.meta.env.MODE === "development" ? "http://localhost:5173" : "https://iconnectae.web.app"
export const actions = {
  pay: async ({ request }) => {
    const data = await request.formData();
    const email = data.get("email");
    const quantity = data.get("quantity");
    const nameOrUrl = data.get("companyURL");
    const session = await stripe.checkout.sessions.create({
      line_items: [
        {
          price_data: {
            currency: "aed",
            product_data: {
              name: "ic-card",
            },
            unit_amount: 40000,
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
          company_name_url: nameOrUrl,
          product_quantity: quantity,
          product_name: "ic-card",
        },
      },
      success_url: `${baseUrl}/placed`,
      cancel_url: `${baseUrl}/bad_checkout`,
      shipping_address_collection: {
        allowed_countries: ["AE"],
      },
    });
    throw redirect(303, session.url);
  },
};
