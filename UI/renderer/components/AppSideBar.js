import React from "react";
import Link from "next/link";
import styles from "./AppSideBar.module.css";

const AppSideBar = () => {
  return (
    <div className={styles.sideMenu}>
      <ul>
        <li className="title-head">
          <img src="../styles/icon/home.png"/>
          <p>APP ICON</p>
        </li>
        <li>
          <Link href="/home" className={styles.link}>
              <img src="../styles/icon/home.png"/>
              Home
          </Link>
        </li>
        <li>
          <Link href="/next" className={styles.link}>
              <img src="../styles/icon/home.png"/>
              Next
          </Link>
        </li>
        <li>
          <Link href="/run" className={styles.link}>
              <img src="../styles/icon/home.png"/>
              Run
          </Link>
        </li>
      </ul>
    </div>
  );
};

export default AppSideBar;
