import path from 'path'
import { app, ipcMain } from 'electron'
import serve from 'electron-serve'
import { createWindow } from './helpers'
// import ExcelJS from 'exceljs'
import { exec } from 'child_process'

const isProd = process.env.NODE_ENV === 'production'

if (isProd) {
  serve({ directory: 'app' })
} else {
  app.setPath('userData', `${app.getPath('userData')} (development)`)
}

;(async () => {
  // app.setActivationPolicy(policy='prohibited')
  await app.whenReady()
  

  const mainWindow = createWindow('main', {
    width: 1000,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
    },
  })
  
  if (isProd) {
    await mainWindow.loadURL('app://./home')
  } else {
    const port = process.argv[2]
    await mainWindow.loadURL(`http://localhost:${port}/home`)
    // await mainWindow.loadURL('https://sereduc.blackboard.com/ultra/admin')
    // mainWindow.webContents.openDevTools()
  }
})()

app.on('window-all-closed', () => {
  app.quit()
})

ipcMain.on('message', async (event, arg) => {
  event.reply('message', `${arg} World!`)
  // console.log(`${arg} World!`)
})

// ipcMain.on('title', async (event, arg) => {
//   event.reply('title', `BBAutoPy - ${arg}`)
//   console.log(`BBAutoPy - ${arg}`)
//   // event.sender()
//   // event.returnValue()
//   // event.processId()
//   // event.frameId()
// })

ipcMain.on('set-title', (event, title) => {
  console.log(`BBAutoPy - ${title}`)
  mainWindow.webContents.executeJavaScript(`document.title = "BBAutoPy - ${title}"`);
});

// ipcMain.handle('read-excel-file', async () => {
//   const filePath = path.join(__dirname, 'path', 'to', 'your', 'file.xlsx'); // Replace with the fixed path to your Excel file

//   const workbook = new ExcelJS.Workbook();
//   await workbook.xlsx.readFile(filePath);

//   const sheet = workbook.worksheets[0];
//   const data = [];
//   sheet.eachRow({ includeEmpty: true }, (row, rowNumber) => {
//     data.push({ rowNumber, values: row.values });
//   });

//   return data;
// });

ipcMain.on('open-excel-file', (event, filePath) => {
  const fullPath = path.resolve(__dirname, filePath);
  exec(`start "" "${fullPath}"`, (error) => {
    if (error) {
      console.error(`Error opening file: ${error.message}`);
    }
  });
});

ipcMain.on('run-python', (event, arg) => {
  const workingDirectory = path.resolve(__dirname, '../src');
  const pythonPath = path.resolve(__dirname, '../../venv/Scripts/python.exe');
  const scriptPath = path.resolve(__dirname, `../src/${arg}`);
  // exec(`python '${arg}'`, (error, stdout, stderr) => {
    // console.log(`${path.resolve(__dirname, "../../venv/Scripts/python.exe")} ${path.resolve(__dirname, arg)}`)
  exec(`start ${pythonPath} ${scriptPath}`, { cwd: workingDirectory }, (error, stdout, stderr) => {
    if (error) {
      event.reply('python-error', stderr);
      return;
    }
    event.reply('python-result', stdout);
  });
});