import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';
import { getAuth } from 'firebase/auth';

// Initialize Firebase
const firebaseConfig = {
  apiKey: "AIzaSyBgxvX4PDXCeX_2MeLTqaH2kKGRNs8c4GU",
  authDomain: "iconnect-86ebb.firebaseapp.com",
  projectId: "iconnect-86ebb",
  storageBucket: "iconnect-86ebb.appspot.com",
  messagingSenderId: "481399262820",
  appId: "1:481399262820:web:a33cb740323f10cec75971",
  measurementId: "G-H7X487MHW7"
};
const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);
export const auth = getAuth(app);