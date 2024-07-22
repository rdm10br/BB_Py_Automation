import React from 'react'
import Head from 'next/head'
import Link from 'next/link'

export default function NextPage() {
  return (
    <React.Fragment>
      <Head>
        <title>Test</title>
      </Head>
      <div>
        <p>
          Teste - <Link href="/home">Go to home page</Link>
        </p>
      </div>
    </React.Fragment>
  )
}