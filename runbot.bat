@ECHO off
python beta.py
python main.py >> log.txt
python editquote.py


pause
python openclose.py
pause