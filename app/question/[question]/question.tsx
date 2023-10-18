"use client";

import { DocumentData, doc, getDoc } from "firebase/firestore";
import { firestore } from "@/lib/utils/firestore";
import { useTeam } from "@/lib/contexts/team";
import { useRouter } from "next/navigation";
import { toast } from "sonner";
import { useEffect } from "react";

interface Question {
  question: DocumentData;
}

export default function Question({ question }: Question) {
  const [team, setTeam] = useTeam();
  const router = useRouter();

  const handleSubmit = async (debug = false) => {
    const reference = doc(firestore, "teams", team);
    const snapshot = await getDoc(reference);

    if (snapshot.exists()) {
      router.push(`/question/${question.id}/${team}`);
    } else if (debug) {
      toast.error("A kód nem érvényes!");
    }
  };

  useEffect(() => {
    handleSubmit(false);
  }, [team]);

  return (
    <div className="h-full flex flex-col items-center justify-center space-y-4">
      <input
        value={team}
        className="text-black text-center"
        placeholder="123456"
        onChange={(e) => setTeam(e.target.value)}
      />
      <button onClick={() => handleSubmit(true)}>Azonosítás</button>
    </div>
  );
}
