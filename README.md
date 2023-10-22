# DJango Framework to Docker Composer Template

# Outline
* 本プロジェクトはDocker Compose上にDJango Frameworkを設定するデフォルトテンプレートになります。

# Startup
~~~sh
$ docker compose up
or
$ docker compose up -d
~~~

## Recompile Startup
~~~sh
$ docker compose up --build
or
$ docker compose up --build -d
~~~

# Create Project
~~~sh
$ docker compose exec web django-admin startproject app
$ docker compose exec web python app/manage.py migrate
$ docker compose exec web python app/manage.py createsuperuser
## 空文字でroot、パスワードは何でも可
~~~

# Start DJango Project
~~~sh
$ docker compose exec web python app/manage.py runserver 0.0.0.0:8888
~~~

# Create Application
~~~sh
$ docker compose exec web /bin/bash
$ cd app/
$ python manage.py startapp [アプリケーション名,DB名]
