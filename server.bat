@echo off
SET FLASK_APP=app
SET FLASK_ENV=development
start cmd /k "cd front_app && npm run serve"
start cmd /k python -m flask run -p 5000
echo Serveurs en fonctionnement
echo flask en http://127.0.0.1:5000/
echo vue en http://192.168.68.140:8080/
pause Veuillez fermer les serveurs vous-même
