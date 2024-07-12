import React from 'react'
import Head from 'next/head'
import Link from 'next/link'

export default function NextPage() {
  return (
    <React.Fragment>
      <Head>
        <title>Settings</title>
      </Head>
      <div>
        <p>
          Here will be the Settings <Link href="/home">Go to home page</Link>
        </p>
      </div>
    </React.Fragment>
  )
}