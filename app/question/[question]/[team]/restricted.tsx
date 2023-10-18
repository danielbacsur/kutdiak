"use client";

import { DocumentData } from "firebase/firestore";
import { useRouter } from "next/navigation";
import { useState } from "react";

interface Restricted {
  team: DocumentData;
}

export default function Restricted({ team }: Restricted) {
  const router = useRouter();

  const handleSubmit = async () => {
    router.push(`/team/${team.id}`)
  };

  return (
    <div className="h-full flex flex-col items-center justify-center space-y-4">
      Nem jó állomásnál vagy
      <button onClick={handleSubmit}>Feladat megtekintése</button>
    </div>
  );
}
