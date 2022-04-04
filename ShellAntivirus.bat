@echo off
title Shell Antivirus
echo Antivirus
echo Created by Toshan
:start
IF EXIST Virus.bat goto infected
IF NOT EXIST Virus.bat goto clean
cd C:Windowssystem32
:infected
echo WARNING !!! VIRUS DETECTED !!!
del Virus.bat
pause
goto start
:clean
echo System Secure!!!
pause
exit