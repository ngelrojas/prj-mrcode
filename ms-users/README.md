### installation
- copy file called cot-env from fenv folder, paste and renamed to .cot-env to
  root folder
- copy file called cot-envdb from fenv folder, paste and renamed to .cot-envdb
  to root folder
 
### build docker
```
  docker-compose build
```

### up docker
```
  docker-compose up -d 
```

### migrate db
```
  docker-compose exec api python manage.py migrate --noinput 
```

### in case not working migration, inside the docker images database 
```
  docker-compose exec db psql --username=myuser --dbname=mydatabase 
```

### next create app
```
 - docker-compose exec api python manage.py startapp core 
```
- create a file user.py inside core/user.py
- doing makemigrations and migrate again
```
  docker-compose exec api python manage.py makemigrations core 
  docker-compose exec api python manage.py migrate --noinput  
```
### create superuser
```
  docker-compose exec api python manage.py createsuperuser 
```
### collect static
```
  docker-compose exec api python manage.py collectstatic --no-input --clear 
```

### list volumes docker 
### display a list of volumes
```
  docker volume ls 
```

### inspect a volume 
```
  docker volume inspect my-volume-listed 
```

### build a docker using tag 
```
  docker build -f ./app/Dockerfile -t mytagfordocker:latest ./app
```

### run another images in other port 
### docker is running on port localhost:9002
```
docker run -d \                                     
-p 9002:9001 \
-e "SECRET_KEY=mysecretkey" -e "DEBUG=1" -e "ALLOWED_HOSTS=*" \
api python /usr/src/app/manage.py runserver 0.0.0.0:9001
```

### show docker logs
```
  docker-compose -f docker-compose.prod.yml logs -f
```
