import React from "react";
import Head from "next/head";
import Link from "next/link";

export default function NextPage() {
  return (
    <React.Fragment>
      <Head>
        <title>Settings</title>
      </Head>
      <div>
        <p>
          <h2>Settings</h2>
        </p>
      </div>
      <div className="card">
        <h3>Credential & Cookies :</h3>
        {/* Save your AVA Credentials : */}
        <button
        // onClick={() => {
        //   window.ipc.send("message", "Batata");
        // }}
        >
          Save Credentials
        </button>
        <button
          // onClick={() => {
          //   window.ipc.send("message", "Destructive");
          // }}
          className="destructive"
        >
          Delete Cookies
        </button>
        <button
          // onClick={() => {
          //   window.ipc.send("message", "Destructive");
          // }}
          className="destructive"
        >
          Delete Cretendials & Cookies
        </button>
      </div>
    </React.Fragment>
  );
}
