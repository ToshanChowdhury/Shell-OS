@echo off
title System File Scanner
color 2f

:startpage
echo Welcome to System File Scanner
echo 1. Scan A File
echo 2. Exit
echo.
set /p answer=Option: 
if %answer%==1 goto filename
if %answer%==2 exit
echo.
goto startpage

:filename
set /p filename=Enter File Name: 
if EXIST %filename% goto infected
if NOT EXIST %filename% goto clean

:infected
echo WARNING!! VIRUS DETECTED!!!
echo.
pause
del %filename%
exit
goto startpage

:clean
echo SYSTEM CLEAN!!!
echo.
pause
exit
goto clean