import React from "react";
import Link from "next/link";
import styles from "./AppSideBar.module.css";
import homeIcon from '../styles/icon/home.png';

const AppSideBar = () => {
  return (
    <div className={styles.sideMenu}>
      <ul>
        <li className={styles.titleHead}>
          <img src={homeIcon}/>
          <p>APP ICON</p>
        </li>
        <li className={styles.menu}>
          <p>Menu</p>
        </li>
        <li>
          <Link href="/home" className={styles.link}>
              <img src='assets/icon/home.png'/>
              Home
          </Link>
        </li>
        <li>
          <Link href="/next" className={styles.link}>
              <img src="../styles/icon/home.png"/>
              Double Check
          </Link>
        </li>
        <li>
          <Link href="/run" className={styles.link}>
              <img src="../styles/icon/home.png"/>
              Cópia
          </Link>
        </li>
        <li>
          <Link href="/home" className={styles.link}>
              <img src="../styles/icon/home.png"/>
              Data
          </Link>
        </li>
        <li>
          <Link href="/home" className={styles.link}>
              <img src="../styles/icon/home.png"/>
              X9
          </Link>
        </li>
        <li>
          <Link href="/home" className={styles.link}>
              <img src="../styles/icon/home.png"/>
              Teste
          </Link>
        </li>
        <li className={styles.settings_span}></li>
        <li>
          <Link href="/home" className={styles.link}>
              <img src="../styles/icon/home.png"/>
              Configuração
          </Link>
        </li>
      </ul>
    </div>
  );
};

export default AppSideBar;
