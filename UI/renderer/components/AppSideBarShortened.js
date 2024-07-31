import React, { useState } from "react";
import Link from "next/link";
import Image from "next/image";
import styles from "./AppSideBar.module.css";
import { FaChevronDown, FaChevronUp } from "react-icons/fa";
// import { ipcRenderer } from 'electron';
import { AppSideBar } from './AppSideBar.js';

const AppSideBarShortened = () => {
  // const [transition, setTransition] = useState(false);
  const [dropdown, setDropdown] = useState({
    DoubleCheck: false,
    Cópia: false,
    Data: false
  });

  const [menu, setMenu] = useState(false);

  const openExcelFile = async () =>{
    window.ipc.send('open-excel-file', '../../Planilhas/SALAS.xlsx')
  };

  const toggleDropdown = (menu) => {
    setDropdown((prevState) => ({
      ...prevState,
      [menu]: !prevState[menu],
    }));
  };

  return (
    <div className={styles.sideMenu}>
      <div className={styles.header}>
        <div className={styles.titleHead}>
          <Image
            className={styles.icon_menus}
            src="/icon/automated-process.png"
            height={20}
            width={20}
          />
        </div>
        <div className={styles.menu} onClick={() => setMenu(!menu)}>
          <Image
            className={styles.icon_menu}
            src="/icon/menu-bar.png"
            height={20}
            width={20}
          />
          {menu.Menu ? (
            <AppSideBar/>
          ) : (
            <AppSideBarShortened/>
          )}
        </div>
      </div>
      <ul>
        <li>
          <Link href="/home" className={styles.link}>
            <Image
              className={styles.icon_menus}
              src="/icon/home.png"
              height={20}
              width={20}
            />
          </Link>
        </li>
        <li onClick={() => toggleDropdown("DoubleCheck")}>
          <Image
            className={styles.icon_menus}
            src="/icon/double-check.png"
            height={20}
            width={20}
          />
          {dropdown.DoubleCheck ? (
            <FaChevronUp className={styles.icon} />
          ) : (
            <FaChevronDown className={styles.icon} />
          )}
        </li>
        {dropdown.DoubleCheck && (
          <ul className={styles.dropdown}>
            <li>
              <Link href="/master" className={styles.link}>
                Master
              </Link>
            </li>
            <li>
              <Link href="/veteranos" className={styles.link}>
                Veteranos
              </Link>
            </li>
            <li>
              <Link href="/digital" className={styles.link}>
                Digital
              </Link>
            </li>
          </ul>
        )}
        <li onClick={() => toggleDropdown("Cópia")}>
          <Image
            className={styles.icon_menus}
            src="/icon/copy.png"
            height={20}
            width={20}
          />
          {dropdown.Cópia ? (
            <FaChevronUp className={styles.icon} />
          ) : (
            <FaChevronDown className={styles.icon} />
          )}
        </li>
        {dropdown.Cópia && (
          <ul className={styles.dropdown}>
            <li>
              <Link href="/material" className={styles.link}>
                Material
              </Link>
            </li>
            <li>
              <Link href="/sala" className={styles.link}>
                Sala Nova
              </Link>
            </li>
          </ul>
        )}
        <li onClick={() => toggleDropdown("Data")}>
          <Image
            className={styles.icon_menus}
            src="/icon/calendar.png"
            height={20}
            width={20}
          />
          {dropdown.Data ? (
            <FaChevronUp className={styles.icon} />
          ) : (
            <FaChevronDown className={styles.icon} />
          )}
        </li>
        {dropdown.Data && (
          <ul className={styles.dropdown}>
            <li>
              <Link href="/datas" className={styles.link}>
                item_1
              </Link>
            </li>
            <li>
              <Link href="/teste" className={styles.link}>
                item_2
              </Link>
            </li>
          </ul>
        )}
        <li>
          <Link href="/x9" className={styles.link}>
            <Image
              className={styles.icon_menus}
              src="/icon/detective.png"
              height={20}
              width={20}
            />
          </Link>
        </li>
        <li>
          <Link href="/teste" className={styles.link}>
            <Image
              className={styles.icon_menus}
              src="/icon/experiment.png"
              height={20}
              width={20}
            />
          </Link>
        </li>
        <li className={styles.plan}>
          <Link href='#' className={styles.link} onClick={openExcelFile}>
          {/* href='javascript:;' */}
            <Image
              className={styles.icon_menus}
              src="/icon/spreadsheet.png"
              height={20}
              width={20}
            />
          </Link>
        </li>
      </ul>
      <div className={styles.settings_container}>
        <li className={styles.settings}>
          <Link href="/settings" className={styles.link}>
            <Image
              className={styles.icon_menus}
              src="/icon/settings.png"
              height={20}
              width={20}
            />
            Configuração
          </Link>
        </li>
      </div>
    </div>
  );
};

export default AppSideBarShortened;
