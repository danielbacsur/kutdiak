"use client";

import { DocumentData, doc, getDoc, updateDoc } from "firebase/firestore";
import { firestore } from "@/lib/utils/firestore";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { toast } from "sonner";

interface Restricted {
  team: DocumentData;
  question: DocumentData;
}

export default function Solve({ team, question }: Restricted) {
  const [answer, setAnswer] = useState("");
  const router = useRouter();

  const handleSubmit = async () => {
    if (answer === question.answer) {
      const reference = doc(firestore, "teams", team.id);

      await updateDoc(reference, {
        current: team.current + 1,
      });

      router.push(`/team/${team.id}/?success=true`)
    } else {
      toast.error("A megoldásod helytelen.");
    }
  };

  return (
    <div className="h-full flex flex-col items-center justify-center space-y-4">
      <h1>{question.question}</h1>
      <input
        className="text-black text-center"
        placeholder="Answer.."
        onChange={(e) => setAnswer(e.target.value)}
      />
      <button onClick={handleSubmit}>Start</button>
    </div>
  );
}
