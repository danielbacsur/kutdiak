"use client";

import React, {
  createContext,
  useState,
  useEffect,
  ReactNode,
  useContext,
} from "react";

type TeamContextType = [string, React.Dispatch<React.SetStateAction<string>>];

export const teamContext = createContext<TeamContextType>(["", () => {}]);

export const useTeam = () => useContext(teamContext);

export const TeamProvider = ({ children }: { children: ReactNode }) => {
  const [team, setTeam] = useState<string>(() => {
    if (typeof window !== "undefined") {
      const savedTeam = localStorage.getItem("team");
      return savedTeam ? JSON.parse(savedTeam) : "";
    } else return "";
  });

  useEffect(() => {
    if (typeof window !== "undefined") {
      localStorage.setItem("team", JSON.stringify(team));
    }
  }, [team]);

  return (
    <teamContext.Provider value={[team, setTeam]}>
      {children}
    </teamContext.Provider>
  );
};
