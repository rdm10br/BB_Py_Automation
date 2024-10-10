' Set WshShell = CreateObject("WScript.Shell")
' WshShell.Run "\run_update_checker.bat", 0, False
' Get the full path of the VBScript

Dim scriptPath
scriptPath = WScript.ScriptFullName

' Get the project directory by extracting the path from the full script path
Dim projectDir
projectDir = Left(scriptPath, InStrRev(scriptPath, "\"))

' Construct the path to the batch file
Dim batchFilePath
batchFilePath = projectDir & "run_update_checker.bat" ' Adjust the batch file name if needed

' Run the batch file silently
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run batchFilePath, 0, False