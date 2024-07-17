import Head from "next/head";
import Image from "next/image";
import Link from "next/link";
import React from "react";

export default function HomePage() {
  const [message, setMessage] = React.useState("No message found.");
  try{
    React.useEffect(() => {
      window.ipc.on("message", (message) => {
        setMessage(message);
      });
    }, []);
  } catch{
    React.useEffect(() => {
      window.ipc.on("title", (message) => {
        setMessage(message);
      });
    }, []);
  }
  return (
    <React.Fragment>
      <Head>
        {/* <meta httpEquiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'"/> */}
        <title
        onLoad={() => {
          window.ipc.send("title", title);
        }}
        >Home</title>
      </Head>
      <div className="optional">
        {/* <p>
          ⚡ Electron + Next.js ⚡ - <Link href="/next">Go to next page</Link>
        </p> */}
        <p>
          The Next page - <Link href="/next">Go to next page</Link>
        </p>
        <p>
          The page that the program runs and shows other scripts -{" "}
          <Link href="/run">Go to Run page</Link>
        </p>
        <p>
          The page to configure all program settings -{" "}
          <Link href="/settings">Go to Settings page</Link>
        </p>
        <p>
          The page that teaches how to run the scripts -{" "}
          <Link href="/tutorial">Go to tutorial page</Link>
        </p>
        <p>
          The page that shows the terminal of the script that's running -{" "}
          <Link href="/terminal">Go to terminal page</Link>
        </p>
        <Image
          src="/images/logo.png"
          alt="Logo image"
          width={256}
          height={256}
        />
      </div>
      <div className="card">
        <p>
          The page that the program runs and shows other scripts -{" "}
          <Link href="/run">Go to Run page</Link>
        </p>
        <button
          onClick={() => {
            window.ipc.send("message", "Batata");
          }}
        >
          Test IPC Button
        </button>
        <p>Message: </p>
        <div className="message_recieved">
          <p>{message}</p>
        </div>
      </div>
    </React.Fragment>
  );
}