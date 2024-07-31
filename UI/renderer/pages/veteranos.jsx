import React from 'react'
import Head from 'next/head'
import Link from 'next/link'

export default function NextPage() {
  return (
    <React.Fragment>
      <Head>
        <title>Veteranos</title>
      </Head>
      <div>
        <p>
            Veteranos - <Link href="/home">Go to home page</Link>
        </p>
      </div>
    </React.Fragment>
  )
}