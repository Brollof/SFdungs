@echo off

set /p completed="Liczba ukonczonych: "
set /p dungs="Podaj lochy: "

call sfdungs\Scripts\activate.bat
python main.py %completed% %dungs% 
pause