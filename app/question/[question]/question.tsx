"use client";

import { DocumentData, doc, getDoc } from "firebase/firestore";
import { firestore } from "@/lib/utils/firestore";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { toast } from "sonner";

interface Question {
  question: DocumentData;
}

export default function Question({ question }: Question) {
  const [code, setCode] = useState("000000");
  const router = useRouter();

  const handleSubmit = async () => {
    const reference = doc(firestore, "teams", code);
    const snapshot = await getDoc(reference);

    if (snapshot.exists()) {
      router.push(`/question/${question.id}/team/${code}`);
    } else {
      toast.error("A kód nem érvényes!");
    }
  };

  return (
    <div className="h-full flex flex-col items-center justify-center space-y-4">
      <input
        className="text-black text-center"
        placeholder="000000"
        onChange={(e) => setCode(e.target.value)}
      />
      <button onClick={handleSubmit}>Azonosítás</button>
    </div>
  );
}
