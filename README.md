<h2 align="center">4RC</h2>

## Старт

#### Запустить сервер

    docker-compose build
    docker-compose up -d
    docker exec 4rc-vtb python manage.py initadmin
    
    or

    docker-compose up --build -d 
    docker exec 4rc-vtb python manage.py initadmin
