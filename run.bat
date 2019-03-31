@echo off

set /p dungs="Podaj lochy: "

call sfdungs\Scripts\activate.bat
python main.py %dungs% 
pause