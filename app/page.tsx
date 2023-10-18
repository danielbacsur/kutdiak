"use client";

import { firestore } from "@/lib/utils/firestore";
import { doc, getDoc } from "firebase/firestore";
import { useTeam } from "@/lib/contexts/team";
import { useRouter } from "next/navigation";
import { toast } from "sonner";

export default function Start() {
  const [team, setTeam] = useTeam();
  const router = useRouter();

  const handleSubmit = async () => {
    const reference = doc(firestore, "teams", team);
    const snapshot = await getDoc(reference);

    if (snapshot.exists()) {
      router.push(`/team/${team}`);
    } else {
      toast.error("A kód nem érvényes!");
    }
  };

  return (
    <div className="h-full flex flex-col items-center justify-center space-y-4">
      <input
        value={team}
        className="text-black text-center"
        placeholder="123456"
        onChange={(e) => setTeam(e.target.value)}
      />
      <button onClick={handleSubmit}>Start</button>
    </div>
  );
}
