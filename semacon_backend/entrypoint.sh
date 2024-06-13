#!/bin/sh

if [ "$DATABASE" = "postgres" ] 
then
    echo "verifique se banco de dados está rodando..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done 

    echo "Banco de dados está rodando =)"
fi

python manage.py makemigrations
python manage.py migrate

exec "$@"