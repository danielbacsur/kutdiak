"use client";

import { DocumentData, doc, updateDoc } from "firebase/firestore";
import { firestore } from "@/lib/utils/firestore";
import { useRouter } from "next/navigation";
import { useState } from "react";

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
  teamname: z.string().min(2, {
    message: "Username must be at least 2 characters.",
  }),
});


interface Rename {
  team: DocumentData;
}

export default function Rename({ team }: Rename) {
  const router = useRouter();

  
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      teamname: "",
    },
  });

  async function onSubmit(values: z.infer<typeof formSchema>) {
    const reference = doc(firestore, "teams", team.id);
    await updateDoc(reference, { name: values.teamname });
    router.refresh();
  }

  return (
    <div className="h-full grid place-items-center p-4">
      <Form {...form}>
        <form
          onSubmit={form.handleSubmit(onSubmit)}
          className="space-y-4 w-full"
        >
          <FormField
            control={form.control}
            name="teamname"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Csapat Neve</FormLabel>
                <FormControl>
                  <Input placeholder="Kutcsapat" type="text" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <Button type="submit" className="w-full">
            Átnevezés
          </Button>
        </form>
      </Form>
    </div>
  );
}
