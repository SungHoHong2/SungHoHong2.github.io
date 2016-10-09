---
published: true
title: Django 기초 3일차
layout: post
category: programming
permalink: /programming_kr/django_3

---


### Model에 대해서 

settings.py에 model이 포함된 application을 추가한다. 
```

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'model',
]

```


application의 model에 클래스를 추가한다. 

``` python

from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


```


console 명령어에서 입력을 한다. 

```

python manage.py makemigrations
python manage.py migrate 

```



### 다 : 다 관계 

```python


from django.db import models

# Create your models here.


class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

class Topping(models.Model):
    title = models.CharField(max_length=200)


class Pizza(models.Model):
    title = models.CharField(max_length=200)
    topping = models.ManyToManyField(Topping)

```


### 1 : 다 관계 


``` python 

class Manufacture(models.Model):
    title = models.CharField(max_length=50)

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacture, on_delete= models.CASCADE)
    model_name = models.CharField(max_length=40)
    nickname = models.CharField(max_length=20)

```








