import React, { useState } from "react";
import Link from "next/link";
import Image from "next/image";
import styles from "./AppSideBar.module.css";
import { FaChevronDown, FaChevronUp } from "react-icons/fa";
// import { ipcRenderer } from 'electron';
import AppSideBarShortened from "./AppSideBarShortened.js";

const AppSideBar = () => {
  // const [transition, setTransition] = useState(false);
  const [dropdown, setDropdown] = useState({
    DoubleCheck: false,
    Cópia: false,
    Data: false,
  });

  const [menu, setMenu] = useState(false);

  const openExcelFile = async () => {
    window.ipc.send("open-excel-file", "../../Planilhas/SALAS.xlsx");
  };

  const [result, setResult] = useState('');
  const runPython = () => {
    // ipcRenderer.send('run-python', '../../src/Main_Test.py');
    // window.ipc.send('run-python');
    window.ipc.send('run-python', 'Main_Test.py');
    window.ipc.on('python-result', (event, data) => {
      setResult(data);
    });
    window.ipc.on('python-error', (event, error) => {
      console.error(error);
    });
  };

  const toggleDropdown = (menu) => {
    setDropdown((prevState) => ({
      ...prevState,
      [menu]: !prevState[menu],
    }));
  };

  return (
    <div className={styles.sideMenu}>
      <ul className={styles.header}>
        <li className={styles.titleHead}>
          <Image
            className={styles.icon_menus}
            src="/icon/automated-process.png"
            height={20}
            width={20}
          />
          <p>BB Py Automation</p>
        </li>
        <li className={styles.menu} onClick={() => setMenu(!menu)}>
          {menu ? (
            <Image
              className={styles.icon_menu}
              src="/icon/recycle-bin.png"
              height={20}
              width={20}
            />
          ) : (
            <Image
              className={styles.icon_menu}
              src="/icon/menu-bar.png"
              height={20}
              width={20}
            />
          )}
        </li>
      </ul>
      <ul>
        <li className={styles.home}>
          <Link href="/home" className={styles.link}>
            <Image
              className={styles.icon_menus}
              src="/icon/home.png"
              height={20}
              width={20}
            />
            Home
          </Link>
        </li>
        <li onClick={() => toggleDropdown("DoubleCheck")}>
          <Image
            className={styles.icon_menus}
            src="/icon/double-check.png"
            height={20}
            width={20}
          />
          Double Check
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
          Cópia
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
          Surtos
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
                Datas
              </Link>
            </li>
            <li>
              <Link href="/teste" className={styles.link}>
                Ajuste AV1
              </Link>
            </li>
            <li>
              <Link href="/teste" className={styles.link}>
                Ajuste AV2
              </Link>
            </li>
            <li>
              <Link href="/teste" className={styles.link}>
                Remove S.M.
              </Link>
            </li>
            <li>
              <Link href="/teste" className={styles.link}>
                Link E-Book
              </Link>
            </li>
            <li>
              <Link href="/teste" className={styles.link}>
                Open Mescla
              </Link>
            </li>
          </ul>
        )}
        <li>
          <Link href="/bq" className={styles.link}>
            <Image
              className={styles.icon_menus}
              src="/icon/fill.png"
              height={20}
              width={20}
            />
            BQ
          </Link>
        </li>
        <li>
          <Link href="/x9" className={styles.link}>
            <Image
              className={styles.icon_menus}
              src="/icon/detective.png"
              height={20}
              width={20}
            />
            X9
          </Link>
        </li>
        <li>
          <Link href="/teste" className={styles.link} onClick={runPython}>
            <Image
              className={styles.icon_menus}
              src="/icon/experiment.png"
              height={20}
              width={20}
            />
            Teste
          </Link>
        </li>
        <li className={styles.plan}>
          <Link href="#" className={styles.link} onClick={openExcelFile}>
            {/* href='javascript:;' */}
            <Image
              className={styles.icon_menus}
              src="/icon/spreadsheet.png"
              height={20}
              width={20}
            />
            Planilha
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

export default AppSideBar;
