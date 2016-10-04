---
published: true
title: Django 기초 1일차 - pyenv 설정하기
layout: post
category: programming
permalink: /programming_kr/django_1

---

### pyenv 사용법

1. pyenv install 3.4.3
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

