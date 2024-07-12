import Head from 'next/head'
import Link from 'next/link'
import React from 'react'

export default function NextPage() {
  return (
    <React.Fragment>
      <Head>
        <title>Run</title>
      </Head>
      <div>
        <p>
          Teste Run - <Link href="/home">Go to home page</Link>
        </p>
      </div>
    </React.Fragment>
  )
}