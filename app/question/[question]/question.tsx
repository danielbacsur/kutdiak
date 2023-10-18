"use client";

import { DocumentData, doc, getDoc } from "firebase/firestore";
import { firestore } from "@/lib/utils/firestore";
import { useTeam } from "@/lib/contexts/team";
import { useRouter } from "next/navigation";
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
  teamcode: z.string().min(2, {
    message: "Username must be at least 2 characters.",
  }),
});

interface Question {
  question: DocumentData;
}

export default function Question({ question }: Question) {
  const [team, setTeam] = useTeam();
  const router = useRouter();

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      teamcode: team,
    },
  });

  async function onSubmit(values: z.infer<typeof formSchema>) {
    setTeam(values.teamcode);

    const reference = doc(firestore, "teams", values.teamcode);
    const snapshot = await getDoc(reference);

    if (snapshot.exists()) {
      router.push(`/question/${question.id}/${values.teamcode}`);
    } else {
      toast.error("A kód nem érvényes!");
    }
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
            name="teamcode"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Csapat Kódja</FormLabel>
                <FormControl>
                  <Input placeholder="000000" type="number" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <Button type="submit" className="w-full">
            Belépés
          </Button>
        </form>
      </Form>
    </div>
  );
}
