export function load({ params }) {

}

export const actions = {
    pay: async ({ cookies, request }) => {
        const data = await request.formData();
        console.log(`${data.get("name")} your payment is complete`);
    }
}