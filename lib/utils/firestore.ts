import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyAClORJu6OIPPwYyEYKWhJ04jgVcE93F6g",
  authDomain: "kutdiak-69420.firebaseapp.com",
  projectId: "kutdiak-69420",
  storageBucket: "kutdiak-69420.appspot.com",
  messagingSenderId: "498681888318",
  appId: "1:498681888318:web:cfdbb96c2a86ab7cf4db6f",
  measurementId: "G-NB4GF82XGG",
};

export const app = initializeApp(firebaseConfig);
export const firestore = getFirestore(app);
