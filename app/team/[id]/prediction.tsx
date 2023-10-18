"use client";

import { DocumentData, doc, updateDoc } from "firebase/firestore";
import { useRouter, useSearchParams } from "next/navigation";
import { firestore } from "@/lib/utils/firestore";

interface Prediction {
  team: DocumentData;
  question: DocumentData;
}

export default function Prediction({ team, question }: Prediction) {
  const router = useRouter();
  const searchParams = useSearchParams();
  const success = searchParams.get("success");

  const revealImage = async () => {
    const reference = doc(firestore, "teams", team.id);

    await updateDoc(reference, {
      ...team,
      questions: [
        ...team.questions.slice(0, team.current),
        {
          ...team.questions[team.current],
          revealed: true,
        },
        ...team.questions.slice(team.current + 1),
      ],
    });

    router.refresh();
  };

  return (
    <div className="h-full flex flex-col items-center justify-center space-y-4">
      <h1>{question.location}</h1>
      {question.revealed && (
        <img src={question.image} alt={question.question} className="h-1/2" />
      )}
      <button onClick={revealImage}>Segítség</button>
    </div>
  );
}
