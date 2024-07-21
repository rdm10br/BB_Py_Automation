import React, { useState } from 'react';
import Link from "next/link";
import styles from "./AppSideBar.module.css";
import homeIcon from "../styles/icon/home.png";
import {
  FaBars,
  FaChartPie,
  FaHistory,
  FaPlug,
  FaRegChartBar,
  FaRegCircle,
  FaSearch,
  FaSignOutAlt,
  FaTable,
  FaTh,
  FaUser,
  FaChevronDown,
  FaChevronUp,
} from "react-icons/fa";

const AppSideBar = () => {
  const [dropdown, setDropdown] = useState({
    category: false,
    posts: false,
    plugins: false,
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
          <Link href="/next" className={styles.link}>
            <img src="../styles/icon/home.png" />
            Double Check
          </Link>
          {dropdown.DoubleCheck ? <FaChevronUp className="menu-icon" /> : <FaChevronDown className="menu-icon" />}
        </li>
        {dropdown.DoubleCheck && (
                    <ul className="dropdown">
                        <li>Master</li>
                        <li>Mescla Veteranos</li>
                        <li>Mescla Digital</li>
                    </ul>
                )}
        <li>
          <Link href="/run" className={styles.link}>
            <img src="../styles/icon/home.png" />
            Cópia
          </Link>
        </li>
        <li>
          <Link href="/home" className={styles.link}>
            <img src="../styles/icon/home.png" />
            Data
          </Link>
        </li>
        <li>
          <Link href="/home" className={styles.link}>
            <img src="../styles/icon/home.png" />
            X9
          </Link>
        </li>
        <li>
          <Link href="/home" className={styles.link}>
            <img src="../styles/icon/home.png" />
            Teste
          </Link>
        </li>
        <li className={styles.settings_span}></li>
        <li>
          <Link href="/home" className={styles.link}>
            <img src="../styles/icon/home.png" />
            Configuração
          </Link>
        </li>
      </ul>
    </div>
  );
};

export default AppSideBar;
