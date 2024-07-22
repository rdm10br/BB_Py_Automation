import React, { useState } from 'react';
import Link from "next/link";
import styles from "./AppSideBar.module.css";
import homeIcon from "../styles/icon/home.png";
import {
  FaChevronDown,
  FaChevronUp,
} from "react-icons/fa";

const AppSideBar = () => {
  const [dropdown, setDropdown] = useState({
    DoubleCheck: false,
    Cópia: false,
    Data: false,
  });

  const toggleDropdown = (menu) => {
    setDropdown((prevState) => ({
      ...prevState,
      [menu]: !prevState[menu],
    }));
  };
  return (
    <div className={styles.sideMenu}>
      <ul>
        <li className={styles.titleHead}>
          <img src={homeIcon} />
          <p>APP ICON</p>
        </li>
        <li className={styles.menu}>
          <p>Menu</p>
        </li>
        <li>
          <Link href="/home" className={styles.link}>
            <img src="assets/icon/home.png" />
            Home
          </Link>
        </li>
        <li onClick={() => toggleDropdown('DoubleCheck')}>
            <img src="../styles/icon/home.png" />
            Double Check
          {dropdown.DoubleCheck ? <FaChevronUp className={styles.icon}/> : <FaChevronDown className={styles.icon}/>}
        </li>
        {dropdown.DoubleCheck && (
                    <ul className={styles.dropdown}>
                        <li>
                          <Link href="/teste" className={styles.link}>
                            Master
                          </Link>
                        </li>
                        <li>
                          <Link href="/teste" className={styles.link}>
                            Veteranos
                          </Link>
                        </li>
                        <li>
                          <Link href="/teste" className={styles.link}>
                            Digital
                          </Link>
                        </li>
                    </ul>
                )}
        <li onClick={() => toggleDropdown('Cópia')}>
            <img src="../styles/icon/home.png"/>
            Cópia
          {dropdown.Cópia ? <FaChevronUp className={styles.icon}/> : <FaChevronDown className={styles.icon}/>}
        </li>
        {dropdown.Cópia && (
                    <ul className={styles.dropdown}>
                        <li>
                          <Link href="/teste" className={styles.link}>
                            Material
                          </Link>
                        </li>
                        <li>
                          <Link href="/terminal" className={styles.link}>
                            Sala Nova
                          </Link>
                        </li>
                    </ul>
                )}
        <li onClick={() => toggleDropdown('Data')}>
            <img src="../styles/icon/home.png"/>
            Data
          {dropdown.Data ? <FaChevronUp className={styles.icon}/> : <FaChevronDown className={styles.icon}/>}
        </li>
        {dropdown.Data && (
                    <ul className={styles.dropdown}>
                        <li>
                          <Link href="/teste" className={styles.link}>
                            Place_Holder_item_1
                          </Link>
                        </li>
                        <li>
                          <Link href="/teste" className={styles.link}>
                            Place_Holder_item_2
                          </Link>
                        </li>
                    </ul>
                )}
        <li>
          <Link href="/run" className={styles.link}>
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
      </ul>
      <div className={styles.settings_container}>
        <li className={styles.settings}>
          <Link href="/settings" className={styles.link}>
            <img src="../styles/icon/home.png"/>
            Configuração
          </Link>
        </li>
      </div>
    </div>
  );
};

export default AppSideBar;