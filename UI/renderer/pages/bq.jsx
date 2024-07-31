import React from 'react'
import Head from 'next/head'
import Link from 'next/link'

export default function NextPage() {
  return (
    <React.Fragment>
      <Head>
        <title>BQ</title>
      </Head>
      <div>
        <p>
          BQ - <Link href="/home">Go to home page</Link>
        </p>
      </div>
    </React.Fragment>
  )
}