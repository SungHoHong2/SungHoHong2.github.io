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

### Django Projects vs Apps 

Project contains several apps 

<br> Project > Apps 

<br>


### Preparing Django 

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








