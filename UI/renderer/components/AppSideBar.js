import React from "react";
import Link from "next/link";
// import { FaHome, FaInfoCircle, FaEnvelope } from 'react-icons/fa';
import styles from "./AppSideBar.module.css";
// import { Icon } from '@mui/material';


const AppSideBar = () => {
  return (
    <div className={styles.sideMenu}>
      <ul>
        <li className="title-head">
          <img src="https://www.flaticon.com/free-icon/hamburger_2516745" />
          <p>
            APP ICON
          </p>
        </li>
        <li>
          <Link href="/home">
            <img src="../style/icon/home.png" />
            Home
          </Link>
        </li>
        <li>
          <Link href="/next">
            <img src="../style/icon/home.png" />
            Next
          </Link>
        </li>
        <li>
          <Link href="/run">
            <img src="../style/icon/home.png" />
            Run
          </Link>
        </li>
      </ul>
    </div>
  );
};

export default AppSideBar;
