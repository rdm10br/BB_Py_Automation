import React from "react";
import Link from "next/link";
// import { FaHome, FaInfoCircle, FaEnvelope } from 'react-icons/fa';
import styles from "./AppSideBar.module.css";

const AppSideBar = () => {
  return (
    <div className={styles.sideMenu}>
      <ul>
        <li>
          <Link href="/home">
          <img src="/styles/icon/home.png"/>
          Home</Link>
        </li>
        <li>
          <Link href="/next">
          <img src="/styles/icon/home.png"/>
          Next</Link>
        </li>
        <li>
          <Link href="/run">
          <img src="/styles/icon/home.png"/>
          Run</Link>
        </li>
      </ul>
    </div>
  );
};

export default AppSideBar;
