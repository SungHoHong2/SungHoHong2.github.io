---
published: true
title: Django 기초 1일차 - 과제
layout: post
category: programming
permalink: /programming_kr/django_2

---

### DJango 버전 확인하기 

현재 설치가 된 django 버전을 알려준다. 만약에 Django가 설치가 안 되어 있으면 에러 메시지가 발생한다. 

```python 

python -m django --version 

```


### 프로젝트 생성하기

|  이름    |   설명     | 
| -- | -- |
| root |   mysite에 의해서 만들어진 바깥쪽 mysite/는 root directory라고 한다. 이름은 변경되어도 상관없다. |
| manage.py | Django 프로젝트를 동작하기 위해 명령어이다.  | 
| inner folder | 실제 프로젝트 패키지이다. 실제 프로젝트에서 내부 클래스를 import 하기 위해선 mysite.url과 같이 이름을 사용해서 주소를 작성한다. | 
| __init__py | Python package라는 것을 알려주는 빈 파일이다. |
| settings.py | Django 프로젝트의 settings 정보가 들어가 있는 파일 | 
|  urls.py  | url 주소 요청을 view로 이어주는 역할 |
| wsgi.py |  web server와 python으로 작성된 web application 또는 framework들 간의 인터페이스를 정의해 놓은 규칙이다. PEP333  |     
    
    





``` 

django-admin startproject mysite 

```



