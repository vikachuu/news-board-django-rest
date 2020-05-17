# News board Django REST API  

## Getting started  

### Clone repository
```
git clone https://github.com/vikachuu/news-board-django-rest.git
```
### Create `.env` file  

Create `.env` file in root directory (next to `docker-compose.yml` file.) with such variables:  
```
NAME=<db_name>
USER=<db_user>
PASSWORD=<db_password>
HOST=<db_host>  # usually `127.0.0.1` or `db`
PORT=<db_port>  # 5432 for postgresql
```

## Run locally

### Install requirements

```
pip install -r requirements.txt
```

### Go inside project folder
```
cd news_board
```

### Database migrations  
Make sure database with the name you wrote in the `.env` file exists. Then run migrations:
```
python manage.py migrate
```

### Run server  
```
python manage.py runserver
```

## Run in Docker

### Create `db.env` file

Create `env/` folder in the root directory. Move `.env` file to the folder.  
Create `db.env` file in the `env/` directory with such variables:  
```
POSTGRES_DB=<postgres_db_name>
POSTGRES_USER=<postgres_db_user>
POSTGRES_PASSWORD=<postgres_db_password>
```
These variables' values should be the same as in `.env` NAME, USER and PASSWORD fields in order the application could connect to the right database.

### Build and run containers
```
docker-compose build
docker-compose up -d --build
```

### Run migrations
```
docker-compose exec web python manage.py migrate --noinput
```
Then API should be running.

### To drop containers use
```
docker-compose down -v
```

## Run deployed on Heroku application  
Follow the link: [news-board-django-rest](http:://).

## Postman collection

Copy the link to Postman collection 
```
https://www.getpostman.com/collections/857dec584ad3a64b5d3a
``` 
Don't forget to add `{{base_url}}` variable to the environment.
