import React from "react";
import AppSideBar from '../components/AppSideBar';
import '../styles/global.css'

function MyApp({ Component, pageProps }) {
  return (
    <>
      <AppSideBar/>
      <div>
        <Component {...pageProps} />
      </div>
    </>
  );
}

export default MyApp;