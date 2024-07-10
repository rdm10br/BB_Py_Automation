import React from "react";
import Head from "next/head";
import Link from "next/link";
import Image from "next/image";

export default function HomePage() {
  const [message, setMessage] = React.useState("No message found");

  React.useEffect(() => {
    window.ipc.on("message", (message) => {
      setMessage(message);
    });
  }, []);
  return (
    <React.Fragment>
      <Head>
        <title>BBAutoPy</title>
      </Head>
      <body>
        <div className="optional">
          <p>
            ⚡ Electron + Next.js ⚡ - <Link href="/next">Go to next page</Link>
          </p>
          <Image
            src="/images/logo.png"
            alt="Logo image"
            width={256}
            height={256}
          />
        </div>
        <div className="card">
          <button
            onClick={() => {
              window.ipc.send("message", "Hello");
            }}
          >
            Test IPC
          </button>
          <p>{message}</p>
        </div>
      </body>
    </React.Fragment>
  );
}
