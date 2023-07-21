import { redirect } from "@sveltejs/kit"
// import dotenv from "dotenv";
import { Stripe } from "stripe";

export const prerender = false;
export function load({ params }) {

}

const stripe = Stripe('sk_test_51KxejGD27b5b7CLZonHYNPNf3a4YGSYFGSo7qGThNX9ryPZDumT1eaTbQgiplH6G0A6RsWDwDqpP8nnbsNGNnLMb00iqmNuqza')
export const actions = {
    pay: async ({ request }) => {
        
        const data = await request.formData();
        const email = data.get('email')
        const quantity = data.get('quantity')
        const session = await stripe.checkout.sessions.create({
            line_items: [
                {
                    price_data: {
                        currency: 'aed',
                        product_data: {
                            name: 'ic-card',
                        },
                        unit_amount: 200,
                    },
                    quantity: quantity,
                },
            ],
            mode: 'payment',
            customer_email : email,
            success_url: 'http://localhost:5173/placed',
            cancel_url: 'http://localhost:5173/',
            shipping_address_collection: {
                allowed_countries: ['AE']
            }
        });
        throw redirect(303, session.url);
    }
}