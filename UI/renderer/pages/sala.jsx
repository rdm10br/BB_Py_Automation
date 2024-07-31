import React from 'react'
import Head from 'next/head'
import Link from 'next/link'

export default function NextPage() {
  return (
    <React.Fragment>
      <Head>
        <title>Sala</title>
      </Head>
      <div>
        <p>
          Sala Nova - <Link href="/home">Go to home page</Link>
        </p>
      </div>
    </React.Fragment>
  )
}