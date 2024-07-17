import path from 'path'
import { app, ipcMain } from 'electron'
import serve from 'electron-serve'
import { createWindow } from './helpers'

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
  console.log(`${arg} World!`)
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