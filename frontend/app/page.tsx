"use client";

import { useState } from "react";

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState<any>(null);

  async function runInference() {
    const res = await fetch("http://YOUR_BACKEND_URL/infer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });
    setResult(await res.json());
  }

  return (
    <main>
      <h1>AIDP Verifiable Inference</h1>
      <textarea onChange={e => setPrompt(e.target.value)} />
      <button onClick={runInference}>Run on AIDP GPU</button>

      {result && (
        <pre>{JSON.stringify(result, null, 2)}</pre>
      )}
    </main>
  );
}
