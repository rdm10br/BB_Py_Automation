import React from 'react'
import Head from 'next/head'
import Link from 'next/link'

export default function NextPage() {
  return (
    <React.Fragment>
      <Head>
        <title>X9</title>
      </Head>
      <div>
        <p>
          X9 - <Link href="/home">Go to home page</Link>
        </p>
      </div>
    </React.Fragment>
  )
}