import { db } from '../../lib/firebase.js';
import { collection, addDoc } from "firebase/firestore";


export const actions = {
    default: async ({ request }) => {
        const data = await request.formData();
        const name = data.get('name');
        const email = data.get('email');   
        const msg = data.get('msg');

        const contact_msg = {name, email, msg} 
        const message_collection = collection(db, 'messages');
        await addDoc(message_collection, contact_msg);

    }
}