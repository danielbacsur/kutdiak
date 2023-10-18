"use client";

import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog";
import { DocumentData, doc, updateDoc } from "firebase/firestore";
import { useRouter, useSearchParams } from "next/navigation";
import { AspectRatio } from "@/components/ui/aspect-ratio";
import { firestore } from "@/lib/utils/firestore";
import { Button } from "@/components/ui/button";
import Image from "next/image";

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
    <div className="h-full flex flex-col p-4 space-y-4">
      <div className="flex-grow grid grid-rows-2 space-y-4">
        <div className="grid place-items-center">{question.location}</div>
        {question.revealed ? 
        <div
        className="bg-cover bg-center rounded-md"
        style={{ backgroundImage: `url(${question.image})` }}
        />
      : <div className="grid place-items-center rounded-md bg-foreground text-background ">A kép zárolva van</div>}
      </div>

      <AlertDialog>
        <AlertDialogTrigger asChild>
          <Button variant="default">Kép Feloldása</Button>
        </AlertDialogTrigger>
        <AlertDialogContent>
          <AlertDialogHeader>
            <AlertDialogTitle>Biztos vagy ebben?</AlertDialogTitle>
            <AlertDialogDescription>
              Ha csapatotok használja a segítséget az pontlevonással jár.
              Gondolkodjatok még egy kicsit!
            </AlertDialogDescription>
          </AlertDialogHeader>
          <AlertDialogFooter>
            <AlertDialogCancel>Vissza</AlertDialogCancel>
            <AlertDialogAction onClick={revealImage}>
              Feloldás
            </AlertDialogAction>
          </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>
  );
}
