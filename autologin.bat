@echo off
set "RESOURCE_FILE=creds.txt"
set "PYTHON_PATH=C:\Program Files\Python311\python.exe"
"%PYTHON_PATH%" autologin.py "%RESOURCE_FILE%"
exit