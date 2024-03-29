"use client";

import { DocumentData, doc, getDoc, updateDoc } from "firebase/firestore";
import { firestore } from "@/lib/utils/firestore";
import { useRouter } from "next/navigation";
import { toast } from "sonner";
import { useChat } from "ai/react";

import { Button } from "@/components/ui/button";
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";
import { Input } from "@/components/ui/input";

import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";
import { useForm } from "react-hook-form";

const formSchema = z.object({
  answer: z.string(),
});

interface Restricted {
  team: DocumentData;
  question: DocumentData;
}

export default function Solve({ team, question }: Restricted) {
  const router = useRouter();

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      answer: "",
    },
  });

  const chat = useChat({
    onFinish: async (e) => {
      console.log(e.content);
      if (e.content === "TRUE") {
        const reference = doc(firestore, "teams", team.id);

        await updateDoc(reference, {
          current: team.current + 1,
        });

        router.push(`/team/${team.id}/?success=true`);
      } else {
        const reference = doc(firestore, "teams", team.id);
        const snapshot = await getDoc(reference);

        if (snapshot.exists()) {
          const data = snapshot.data();

          await updateDoc(reference, {
            guesses: data.guesses + 1,
          });
        }

        toast.error("A megoldásod helytelen.");
      }
    },
    initialMessages: [
      {
        id: "the-alpha-prompt",
        role: "system",
        content: `Te egy online quiz megoldásait ellenőrzöd.
Feladatod hogy eldöntsd, hogy az alábbi kérdésre beérkező válasz helyes-e.
Ne foglalkozz helyesírási hibákkal, kis és nagy betűkkel, ékezetekkel és egy karakteres elírásokkal. Ha a válasz lényegében jó akkor fogadd el.
A quiz megoldását csak akkor fogadd el, ha a beírt válasz témája megegyezik a kérdés témájával. A válaszadó nem kérdezhet vagy írhat be egyéb szöveget.
      
A KÉRDÉS: ${question.question}
AZ ELVÁRT VÁLASZ: ${question.answer}
      
ELFOGADOTT VÁLASZ ESETÉN CSAK ANNYIT VÁLASZOLJ: TRUE
NEM ELFOGADOTT VÁLASZ ESETÉN CSAK ANNYIT VÁLASZOLJ: FALSE
ÖSSZESEN EZ A KÉT LEHETŐSÉGED VAN A VÁLASZADÁSKOR. NEM HASZNÁLHATSZ EGYÉB SZAVAKAT.
      
====================
      
You are checking the answers for an online quiz.
Your task is to decide whether the response received for the following question is correct.
Do not worry about spelling mistakes, capitalization, accents, or single character typos. If the answer is essentially correct, accept it.
Only accept the quiz answer if the subject of the typed response matches the subject of the question. The respondent cannot ask questions or enter any other text.
      
THE QUESTION: ${question.question}
THE EXPECTED ANSWER: ${question.answer}
      
IF THE ANSWER IS ACCEPTED, RESPOND ONLY WITH: TRUE
IF THE ANSWER IS NOT ACCEPTED, RESPOND ONLY WITH: FALSE
THERE ARE ONLY THESE TWO OPTIONS FOR RESPONDING. YOU CANNOT USE ANY OTHER WORDS.`,
      },
    ],
  });

  async function onSubmit(values: z.infer<typeof formSchema>) {
    chat.append({ role: "user", content: values.answer });
  }

  return (
    <div className="h-full flex flex-col p-4 space-y-4">
      <div className="flex-grow grid place-items-center">{question.question}</div>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4 w-full">
          <FormField
            control={form.control}
            name="answer"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Válaszodat írd ide!</FormLabel>
                <FormControl>
                  <Input placeholder="Válasz" type="text" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <Button type="submit" className="w-full">
            Ellenőrzés
          </Button>
        </form>
      </Form>
    </div>
  );
}
