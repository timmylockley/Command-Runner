@echo off
cd /d "%~dp5"
rem Locate pythonw or python interpreter silently and run script
start /b pythonw background_runner.py
exit
