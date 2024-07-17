import React from "react";
import AppSideBar from '../components/AppSideBar';
import '../styles/global.css'

// function MyApp({ Component, pageProps}) {
//   return (<Component {...pageProps} />
    
//   )
// }


function MyApp({ Component, pageProps }) {
  return (
    <>
      <AppSideBar />
      <div style={{ marginLeft: '200px', padding: '20px' }}>
        <Component {...pageProps} />
      </div>
    </>
  );
}

export default MyApp;