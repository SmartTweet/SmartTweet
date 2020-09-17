@echo off
SET FLASK_APP=app
SET FLASK_ENV=development
start cmd /k python -m flask run -p 5000
start cmd /k "cd front_app && npm run serve"

echo Serveurs en fonctionnement
echo Flask en http://127.0.0.1:5000/
echo Vue en http://192.168.68.140:8080/
pause "Veuillez fermer les serveurs vous-même"
