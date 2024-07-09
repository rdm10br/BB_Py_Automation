import '../styles/global.css'
import '../components/AppSideBar'
// renderer/pages/_app.js
// import {globals as Style} from 'UI/renderer/styles'

function MyApp({ Component, pageProps}) {
  return <Component {...pageProps} />;
}

export default MyApp;