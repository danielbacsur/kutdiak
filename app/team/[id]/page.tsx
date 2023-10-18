import { firestore } from "@/lib/utils/firestore";
import { doc, getDoc } from "firebase/firestore";
import Prediction from "./prediction";
import Rename from "./rename";

interface Team {
  params: { id: string };
}

export default async function Team({ params }: Team) {
  const reference = doc(firestore, "teams", params.id);
  const snapshot = await getDoc(reference);

  if (snapshot.exists()) {
    const team = snapshot.data();
    const question = team.questions[team.current];

    if (team.name === "") {
      return <Rename team={team} />;
    } else {
      return <Prediction team={team} question={question} />;
    }
  }
}
