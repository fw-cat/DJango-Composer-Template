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

# Login to Docker Containor
~~~sh
$ docker compose exec web /bin/bash
~~~

# DJango Commands
* DJango Frameworkの利用手順のまとめになります

## DJangoの起動コマンド
~~~sh
$ python manage.py runserver 0.0.0.0:8000
~~~

## DJangoのアプリの追加コマンド
~~~sh
$ python manage.py startapp [app名、DB名]
~~~
