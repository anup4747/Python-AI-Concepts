// app/layout.tsx
import React from "react";
import "../globals.css"; // Import your main css here

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <title>Chat App</title>
        <meta name="description" content="A simple chat application" />
      </head>
      <body>
        <header style={{ padding: "1rem", background: "#f1f1f1" }}>
          <h1>Chatbot</h1>
        </header>
        <main style={{ padding: "2rem" }}>
          {children}
        </main>
        <footer style={{ padding: "1rem", background: "#f1f1f1", textAlign: "center" }}>
          <small>© 2025 My Chatbot</small>
        </footer>
      </body>
    </html>
  );
}
