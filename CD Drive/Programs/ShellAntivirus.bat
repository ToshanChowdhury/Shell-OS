@echo off
color 2f
title Shell Antivirus

:startpage
echo Welcome to Antivirus, select an option to begin scanning
echo 1. Scan Your Computer
echo 2. Exit
set /p answer=Option: 
if %answer%==1 goto scanning
if %answer%==2 Exit
echo.
goto startpage

:scanning
echo Scanning Your Computer...
echo.
if EXIST Virus.bat goto infected
if NOT EXIST Virus.bat goto clean
pause
goto scanning

:infected
echo WARNING VIRUS DETCTED!!!
echo.
pause
del
exit
goto infected

:clean
echo VIRUS NOT DETCTED!!!
echo.
pause
exit
goto clean