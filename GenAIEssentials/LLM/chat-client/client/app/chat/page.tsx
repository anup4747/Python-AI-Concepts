'use client'
import { useState, FormEvent } from "react";

export default function Home() {
  const [messages, setMessages] = useState<{ from: string; text: string }[]>([]);
  const [input, setInput] = useState("");

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    if (!input) return;

    setMessages((prev) => [...prev, { from: "user", text: input }]);

    // Call your Flask API
    const res = await fetch("http://localhost:5000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input }),
    });
    const data = await res.json();

    setMessages((prev) => [...prev, { from: "bot", text: data.reply }]);
    setInput("");
  }

  return (
    <div>
      <h1>Chatbot</h1>
      <div style={{ minHeight: "200px", border: "1px solid #ccc", padding: 10 }}>
        {messages.map((msg, i) => (
          <p key={i}><b>{msg.from}:</b> {msg.text}</p>
        ))}
      </div>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message"
          style={{ width: "80%" }}
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}
