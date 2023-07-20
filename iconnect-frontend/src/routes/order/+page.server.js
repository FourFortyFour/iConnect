import { redirect } from "@sveltejs/kit"
// import dotenv from "dotenv";
import { Stripe } from "stripe";

export const prerender = false;
export function load({ params }) {

}

const stripe = Stripe('sk_test_51NVJiRGxLFc3zCwXgKNjIQd7MVZ7v7DYXWDic8fwAhbKmU2EKFVEiuzIHofq4wWG22GWVTCQYqg0fyOM2DQQBLAw00i07d5S17')
export const actions = {
    pay: async ({ request }) => {
        // dotenv.config();
        // console.log(process.env["STRIPE_PUBLISHABLE_KEY"]);
        // let baseUrl = request.headers['x-forwarded-proto'] + '://' + request.headers.host;
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
                    quantity: 1,
                },
            ],
            mode: 'payment',
            success_url: 'http://localhost:5173/placed',
            cancel_url: 'http://localhost:5173/',
        });
        throw redirect(303, session.url);
    }
}