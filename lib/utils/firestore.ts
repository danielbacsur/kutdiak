import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyC34HT-y7TSWoa0_h7iyxg6gUyvEoVbCcg",
  authDomain: "kutdiak-74f58.firebaseapp.com",
  projectId: "kutdiak-74f58",
  storageBucket: "kutdiak-74f58.appspot.com",
  messagingSenderId: "844280105997",
  appId: "1:844280105997:web:788f291a9b23e67d991944",
  measurementId: "G-C6ZRGJ61ZM"
};

export const app = initializeApp(firebaseConfig);
export const firestore = getFirestore(app);
