@echo off
SET FLASK_APP=app
SET FLASK_ENV=development
start cmd /k serve front_app/dist -l 5000
start cmd /k python -m flask run -p 5001
echo Serveurs en fonctionnement:
echo flask en http://127.0.0.1:5001/
echo vue en http://192.168.68.140:5000/
pause
