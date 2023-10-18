import { firestore } from "@/lib/utils/firestore";
import { doc, getDoc } from "firebase/firestore";
import Question from "./question";

import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";

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
    return (
      <div className="h-full grid place-items-center p-4 text-center">
        Hiba történt.
        <br /> Hívj +36301999340 és kitalálunk valamit 🫠
      </div>
    );
  }
}
