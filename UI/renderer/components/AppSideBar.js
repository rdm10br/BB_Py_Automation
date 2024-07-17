import React from "react";
import Link from "next/link";
// import { FaHome, FaInfoCircle, FaEnvelope } from 'react-icons/fa';
import styles from "./AppSideBar.module.css";

const AppSideBar = () => {
  return (
    <div className={styles.sideMenu}>
      <ul>
        <li>
          <img src="/styles/icon/home.png"/>
          <Link href="/home">Home</Link>
        </li>
        <li>
          <img src="/styles/icon/home.png"/>
          <Link href="/next">Next</Link>
        </li>
        <li>
          <img src="/styles/icon/home.png"/>
          <Link href="/run">Run</Link>
        </li>
      </ul>
    </div>
  );
};

export default AppSideBar;
