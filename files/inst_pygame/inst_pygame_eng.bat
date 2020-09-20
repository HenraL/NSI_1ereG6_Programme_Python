REM sets the color to background black, writing green
color 0A
REM hides C:\... and just shows the required text
echo off
REM if your volume name is D it will go to D:\
cd D:\
REM if your volume name is  C it will not go to D:\ but to C:\
cd C:\
REM clears screen
cls
REM code mark, goes to it if asked in the code
:choice
echo If the shell shows the message "WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x04A394D0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed')': /simple/pygame/"
echo try to run the program with admin writes or make sure you have an active connection.
REM question
echo Do you whant to install pygame? [(y)es/(n)o/(U)update]:
REM variable to remember youre choice
set /p choice=
REM instructions
if %choice%==y goto i
REM instructions
if %choice%==Y goto i
REM instructions
if %choice%==n goto n
REM instructions
if %choice%==N goto n
REM instructions
if %choice%==u goto m
REM instructions
if %choice%==U goto m
REM error message
echo Please make sure you've entered either "y" for yes or "n" for no or "u" for update.
REM instructions
goto choice
REM code mark, goes to it if asked in the code
:i
REM text
echo Installing...:
REM shows C:\....
echo on
REM first try to install pygame
py -m pip install -U pygame --user
REM hides C:\... and just shows the required text
echo off
REM testing to see if pygame is installed
echo keys to lay the game:
echo    - space to shoot
echo    - right arrow to go right
echo    - left arrow to go left
REM we pause the code until a key is hit
pause
REM we start pygame
py -m pygame.examples.aliens
REM text
echo Pygame has succefully been installed on your computer.
REM code mark, goes to it if asked in the code
:q
REM question
echo Do you whant to update pygame? [(Y)es/(N)o]:
set /p choice=
REM instructions
if %choice%==y goto m
REM instructions
if %choice%==Y goto m
REM instructions
if %choice%==n goto n
REM instructions
if %choice%==N goto n
REM error message
echo Please make sure you've entered either "y" for yes or "n" for no.
REM instruction
goto q
REM code mark, goes to it if asked in the code
:m
REM shows C:\....
echo on
REM line of code to update pygame
py -m pip install -U pygame --user
REM n'affiche pas C:\... mais juste la comande
echo off
REM testing to see if pygame is installed
echo keys to lay the game:
echo    - space to shoot
echo    - right arrow to go right
echo    - left arrow to go left
REM we pause the code until a key is hit
pause
REM we start pygame
py -m pygame.examples.aliens
REM hides C:\... and just shows the required text
echo off
REM Text
echo Pygame has been updated on youre computer.
REM instructions
goto n
REM code mark, goes to it if asked in the code
:n
REM text
echo Goodbye.
REM text
echo created by Henry Letellier
REM text
echo " ._____. "
REM text
echo " |.   .| "
REM text
echo " |  |  | "
REM text
echo " |\___/| "
REM text
echo " |_____| "
REM sleep time
timeout 3
REM we pause the code until a key is hit
pause
REM we pause the code until a key is hit
pause