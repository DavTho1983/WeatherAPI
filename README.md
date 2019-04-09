<h1>To run this project:</h1>

I used RabbitMQ as the broker, and connected to the default at 

    amqp://guest:**@127.0.0.1:5672//.

so I didn't need to specify a username or password for rabbit. I used Windows 10, so I did need to install Erlang as 
admin and then install RabbitMQ via the Bintray link.

<h4>Install Erlang</h4>

    https://www.erlang.org/downloads
    
<h4>Install RabbitMQ</h4>

    https://www.rabbitmq.com/install-windows.html

Celery > 4.1 does not work with Windows 10 properly, so I used eventlet.

<h3>Cloning the repo</h3>
In a Mac terminal or Windows Powershell, cd into the directory where you want to put the project and use:

    git clone https://github.com/DavTho1983/WeatherAPI.git
    
<p>Now immediately cd into Weather</p>

    cd Weather

<h3>Creating a superuser</h3>
<p>To use the admin section you will need to create a superuser with:</p>

    python manage.py createsuperuser

<h3>Running the Worker</h3>
<p>In a separate terminal, cd into Weather and, run the celery worker with:</p>

    celery -A Weather worker -l info -P eventlet

<h3>Start celerybeat</h3>
<p>This project uses django-celery-beat to schedule periodic tasks. In a separate terminal, cd into Weather and start 
the celerybeat scheduler with:</p>

<code>celery -A Weather  beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler</code>

<h3>Run the development server</h3>
To serve the project backend use:

    python manage.py runserver

<h3>Navigate to the api</h3>
<p>Open up your browser and navigate to</p>

    localhost:8000/api
    
<p>The scheduler should update the LondonWeather model immediately and once at the start of every hour.</p>
<p>Uncommenting line 23 in Weather/celery.py will schedule a task for every 10 secs so you can see more data.</p>
