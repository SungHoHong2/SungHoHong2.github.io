---
published: true
title: Django Basic
layout: post
category: programming
permalink: /programming/
---

### what is django

django is an open-source MVC framework written in Python for building web application
<br> Today, most web applications including Django send data to the server to validate, process and render HTML

1. User requests a URL
2. Django process (Controller)
3. Validation (Model)
4. Django process (Controller)
5. Rendering (Template)
6. User views the HTML

<br> By making this progress with seperate components makes it easier to maintain and collaborate on the project

<br>

### Django Framework
The validation, rendering, processing is taken care of by seperate components in Django
<br> Django is called MTV rathern than MVC because it has Model, Template and View

1. User
2. View <Controller> (Process data)
3. Model (Stores and Validate data)
4. Template (Renders HTML)

<br>


### Installing Django

Using pip after installing python  

```
pip install django

```

<br> Creating Django project

```

django-admin startproject Treasuregram

```

<br> Running project in the Server

```

python manage.py runserver

```

<br> Creating an App inside the project

```

python manage.py startapp main_app

```

<br>


### Basic Idea of View

view is like a controller in spring framework <br>
A view is simply a Python function that takes in a web request and returns a web response

<br> project/main_app/views.py

``` python

from django shortcuts import render
from django.http import httpResponse

# updating views
def index(request):
	return HttpResponse('<h1>Hello Explorers</h1>')

```

<br> project/project/urls.py
<br> linking hte url to the specific response

``` python

from django.conf.urls import url
from django.contrib import admin
from main_app import views

# this url pattern checks the url that has written '/index' and maps to the function named 'index' in the views.py
urlpatterns = [
	url(r'^admin/', admin.site.urls)
	    , url(r'^index/', views.index)
	]

```

<br>

<hr>

### Refactoring the Project's URL Dispatcher

First remove the index/ from the regex and match the empty path

<br> project/project/urls.py

``` python

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', admin.site.urls)
	url(r'^', include('main_app.urls'))
]

```

<br> project/main_app/urls.py

``` python

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index)
]

```

<br>

<hr>

###  MTV Model with Templates

Django projects automatically create and look for  template files in the app, if the app is registered with the Django project in settings

<br> project/project/settings.py

``` python

INSTALLED APPS = [
	'main_app'
	...
]

```

<br> view should redner an HTML template
<br> project/main_app/views.py

``` python

from django.sorthcuts import render

def index(requests):
	name = 'Gold Nugget'
	value = 1000.0
	context = {
		'treasure_name' : name
	       ,'treasure_value' : value
	}
	return render(requests, 'index.html', context )

```

<br> template

``` python

<html>
	<head>
		<title>TreasureGram</title>
	</head>
	<body>
		<h1>TreasureGram</h1>
		<p><< treasure_name >></p>
		<p><< treasure_val >></p>
	</body>
</html>

```

<hr>

<br>

### Passing More data in Dictionary Context

Use a class to define more information about the context object

<br> project/main_app/views.py

``` python

from django.shortcuts import render

def index(request):
	return render(request, 'index.html', {'treasures' : treasures})

class Treasure:
	def __init__(self, name, value, material, location):
		self.name = name
		self.value = value
		self.material = material
		self.location = location

treasures = [ ... ]

```

<br> html file
<br> adding files

``` python

<< for treasure in treasures >>
<p>{{ treasure.name }}</p>

	<< if treasure.value > 0 >>
		<p>{{ treasure.value }}</p>
	<< else >>
		<p>unknown</p>
	<< endif >>
<< endfor >>

```

<br>

### Adding Static files

Django will also look for static folder like the templates.
<br> Static folder are for CSS, javascript and static images
<br> after adding the style.css in static folder

``` python

<< load staticfiles >>
<!DOCTYPE html>
<html>
	<link rel='stylesheet' type="text/css" href="<< static 'style.css>>">
	<link rel='stylesheet' type="text/css" href="<< static 'bootstrap.min.css'>>">

<img src = "<< static 'images/materials-icon.png'>>">

</html>

```

<hr>

<br>

### Adding Model

project/main_app/models.py

| Django | Python | SQL |
|--------|--------|-----|
| models.CharField() | string | VARCHAR |
| models.IntegerField() | int | INTEGER |  
| models.FloatField() | float | FLOAT |
| models.DecimalField() | decimal | DECIMAL |

``` python

from django.db import models
class Treasure(models.Model):
	name = models.CharField(max_length=100)
	value = models.DecimalField(max_digits=10, decimal_places=2)
	material = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	img_url = models.CharField(max_length=100)

```

<br> add migrations

``` python

python manage.py makemigrations

```

<br> Applies the migration to the database

``` python

python manage.py migrate

```

<br> Checking the migration file

``` python

python manage.py sqlmigrate main_app 0001

```

<br> Django interactive shell

```

python manage.py shell
>>> from main_app.models import Treasure
>>> Treasure.objects.all()
[]
>>> t = Treasure(name='Coffee can', value=20.00, location='Acme, CA')
>>> t.save()
>>> Treasure.objects.all()
[<Treasure: Treasure object>]

```
