<h1>To run this project:</h1>

I used RabbitMQ as the broker, and connected to the default at amqp://guest:**@127.0.0.1:5672//., so I didn't need to specify
a username or password for rabbit. I used Windows 10, so I did need to install Erlang as admin and then install RabbitMQ via the Bintray link.

Celery > 4.1 does not work with Windows 10 properly, so I installed eventlet in the terminal with

<code>pip install eventlet</code>


run the celery worker in the terminal with

<code>celery -A Weather  worker -l info -P eventlet</code>

create superuser with

<code>python manage.py createsuperuser</code>

run development server with

<code>python manage.py runserver</code>

start celerybeat scheduler with:

<code>celery -A Weather  beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler</code>