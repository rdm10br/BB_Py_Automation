import Head from 'next/head'
import Link from 'next/link'
import React from 'react'

export default function NextPage() {
  return (
    <React.Fragment>
      <Head>
        <title>Terminal</title>
      </Head>
      <div>
        <p>
          Here will be the terminal - <Link href="/home">Go to home page</Link>
        </p>
      </div>
    </React.Fragment>
  )
}