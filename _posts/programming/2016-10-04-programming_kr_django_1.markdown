---
published: true
title: Django 기초 1일차 - pyenv 설정하기
layout: post
category: programming
permalink: /programming_kr/django_1

---

### pyenv 사용법

> 1. pyenv install 3.4.3
   - Python 버전 3.4.3d을 다운받아서 pyenv에서 사용할 수 있게 한다. 
2. pyenv pyenv virtualenv 3.4.3 fc-blog
   - fc-blog라는 이름가진 가상머신을 생성한다. 
3. 가상환경을 설정해주고 싶은 폴더 안에서 pyenv local fc-blog
   - 특정 폴더 안에서 
4. vi ~/.bash_profile에서 경로설정
5. pip install django 
   - 가상 머신형태에서 django 버전 설치하기 
   - pip list로 현재 설치되어 있는 정보 확인할 수 있다. 
6. django-admin startproject blog 
   - blog 폴더 안에 django 프로젝트 생성 
7. pycharm에서 preference의 interpretor를 fc-blog의 python파일로 설정

<br>

#### .bash_profile에 들어가는 정보 

```

export PYENV_ROOT=/usr/local/var/pyenv
if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi


```


<hr>


### MTV Structure 

Django는 소프트웨어 공학에서 사용되는 MVC(Model-View-Controller)패턴과 유사한, Model-Template-View(MTV)패턴을 사용합니다.

1. python manage.py startapp post
   - 애플리케이션을 실행하기 위한 준비작업. 실질적으로 필요한 MTV 구조를 자동 생성한다. 
   - 애플리케이션은 각각 기능 당 필요한 묶음을 의미한다. 
   - 현 예제는 post 기능을 대표하는 기능들의 묶음을 말한다. 
   

<br> 

#### model

1. model 생성
2. settings.py에서 post 등록
3. python manage.py makemigrations 입력  
4. python manage.py migrate 입력 
5. python manage.py startapp post <- post의 App 생성 (Project > Apps) 

- models.py 

```python

from django.db import models

# Class
# 데이터베이스에서 table 단위
class Post(models.Model):

    # post columns
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    content = models.TextField()                        # 길이 제한이 없음
    like_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)   # auto_now_add는 ROW 생성 순간에 자동으로 생성


    def __str__(self):
        return self.title

```
   
- settings.py 
   
```python
 
 INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'post',
]
 
```


- admin 페이지에 데이터 모델 적용 
    - admin 페이지에서 별도로 모델 테이블에 정보를 등록할 수 있다. 

```python

from django.contrib import admin

# models 안쪽의 포스트 클래스를 import 한다.
from .models import Post


# Django 어드민 사이트에 Post 모델을 등록한다.
admin.site.register(Post)


```


<hr> 

### Super User 만들기

```

python manage.py createsuperuser

```


### Shell 사용

- database를 클래스처럼 사용하는 것을 ORM이라고 한다. 


``` python

from post.models import Post
Post.objects.all() 
Post.objects.first()
Post.objects.last()
Post.objects.filter(title__contains='first')

```


### View 

1. os.path는 파일 경로를 생성하고 수정하고 파일 정보를 쉽게 다룰 수 있게 해주는 모듈 

- settings.py 

```python 

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR  = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

...
 
 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ TEMPLATE_DIR ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


... 



STATICFILES_DIRS = [
    STATIC_DIR,
]


```


- views.py 

```python

from django.shortcuts import render, render_to_response
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    rtn = {
        'posts' : posts
    }
    return render_to_response('post_list.html', rtn)

```


- urls.py

``` python

from django.conf.urls import url
from django.contrib import admin
from post.views import post_list


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^post/list/', post_list),
]

```


- post_list.html 

```

{% load staticfiles %}

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="{% static '/css/post_list.css' %}">
  <title>Document</title>
</head>
<body>

  <h1>{{ title }}</h1>

  {% for post in posts %}

  <article>
  <h1 class="post_title">{{ post.title }}</h1>
  <h2 class="post_description">{{ post.description }}</h2>
  <p class="post_created">{{ post.created }}</p>
  </article>

  {% endfor %}

</body>
</html>

```


### 과제 


1일 
django project
tutorial  1, 2, 3, 4 


2일 
model 
--
