import { doc, getDoc } from "firebase/firestore";
import { firestore } from "@/lib/utils/firestore";
import Restricted from "./restricted";
import Solve from "./solve";

interface Answer {
  params: { question: string; team: string };
}

export default async function Answer({ params }: Answer) {
  const reference = doc(firestore, "teams", params.team);
  const snapshot = await getDoc(reference);

  if (snapshot.exists()) {
    const team = snapshot.data();
    const question = team.questions[team.current];

   if (question.id !== params.question) {
      return <Restricted team={team} />;
    } else {
      return <Solve team={team} question={question} />;
    }
  }
}
