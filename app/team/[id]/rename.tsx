"use client";

import { DocumentData, doc, updateDoc } from "firebase/firestore";
import { firestore } from "@/lib/utils/firestore";
import { useRouter } from "next/navigation";
import { useState } from "react";

interface Rename {
  team: DocumentData;
}

export default function Rename({ team }: Rename) {
  const [name, setName] = useState("");
  const router = useRouter();

  const handleSubmit = async () => {
    if (name === "") return;

    const reference = doc(firestore, "teams", team.id);
    await updateDoc(reference, { name });
    router.refresh();
  };

  return (
    <div className="h-full flex flex-col items-center justify-center space-y-4">
      <input
        className="text-black text-center"
        placeholder="Rename"
        onChange={(e) => setName(e.target.value)}
      />
      <button onClick={handleSubmit}>Start</button>
    </div>
  );
}
