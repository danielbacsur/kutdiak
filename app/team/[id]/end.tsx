"use client"

import useWindowSize from 'react-use/lib/useWindowSize'
import Confetti from 'react-confetti'

export default function End() {
    const { width, height } = useWindowSize()
    return  <div className="h-full flex flex-col items-center justify-center space-y-4">
    Gratulálok, győztetek!
    <Confetti
width={width}
height={height}
/>
  </div>
}