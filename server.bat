@echo off
SET FLASK_APP=app
SET FLASK_ENV=development
start cmd /k serve front_app/dist -l 5000
start cmd /k python -m flask run -p 5001
echo Serveurs en fonctionnement.
