@echo off
rem Start the patched Inky. Put this file in the Inky source folder (the one that contains "app") and double-click it.
cd /d "%~dp0app"
if not exist node_modules call npm install
call npm start
