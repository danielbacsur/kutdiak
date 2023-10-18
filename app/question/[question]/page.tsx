import { firestore } from "@/lib/utils/firestore";
import { doc, getDoc } from "firebase/firestore";
import Question from "./question";

interface QuestionLoader {
  params: { question: string };
}

export default async function QuestionLoader({ params }: QuestionLoader) {
  const reference = doc(firestore, "questions", params.question);
  const snapshot = await getDoc(reference);

  if (snapshot.exists()) {
    const question = snapshot.data();
    return <Question question={question} />;
  } else {
    return <p>Valami hiba történt.</p>
  }
}
