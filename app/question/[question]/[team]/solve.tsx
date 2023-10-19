"use client";

import { DocumentData, doc, getDoc, updateDoc } from "firebase/firestore";
import { firestore } from "@/lib/utils/firestore";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
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

  async function onSubmit(values: z.infer<typeof formSchema>) {
    if (values.answer === question.answer) {
      const reference = doc(firestore, "teams", team.id);

      await updateDoc(reference, {
        current: team.current + 1,
      });

      router.push(`/team/${team.id}/?success=true`);
    } else {
      const reference = doc(firestore, "teams", team.id);

      await updateDoc(reference, {
        guesses: team.guesses + 1,
      });

      router.refresh()

      toast.error("A megoldásod helytelen.");
    }
  }

  return (
    <div className="h-full flex flex-col p-4 space-y-4">
      <div className="flex-grow grid place-items-center">
        {question.question}
      </div>
      <Form {...form}>
        <form
          onSubmit={form.handleSubmit(onSubmit)}
          className="space-y-4 w-full"
        >
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
