import { redirect } from "@sveltejs/kit"

export function load({ params }) {

}

export const actions = {
    pay: async ({ request }) => {
        const data = await request.formData();
        console.log(`${data.get("name")} your payment is complete`);
        throw redirect(303, '/placed');   
    }
}