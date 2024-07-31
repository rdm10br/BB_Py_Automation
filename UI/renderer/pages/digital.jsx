import React from "react";
import Head from "next/head";
import Link from "next/link";
import Runner from "../components/runner.js";

export default function NextPage() {
  return (
    <React.Fragment>
      <Head>
        <title>Digital</title>
      </Head>
      <div>
        {/* <p>
          Master - <Link href="/home">Go to home page</Link>
        </p> */}
        <h2>Double Check - Digital</h2>
        <div className="card">
          <h3>Tutorial</h3>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
          </p>
        </div>
        <Runner></Runner>
      </div>
    </React.Fragment>
  );
}
