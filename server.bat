@echo off
SET FLASK_APP=app
SET FLASK_ENV=development
python -m flask run -p 5000
echo Serveurs en fonctionnement
echo Flask en http://127.0.0.1:5000/
