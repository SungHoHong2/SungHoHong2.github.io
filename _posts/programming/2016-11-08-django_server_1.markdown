---
published: true
title: Deploy Server with Amazon 
layout: post
category: programming
permalink: /programming/django_server_1
---


|  name  |  description | 
| --  | -- | 
| Ubuntu Linux | the OS of the server |
| Nginx| Web server. respond with static page and files by receiving HTTP request |
| Django  | Web application. respond with dynamic data by receiving HTTP request | 
| uWSGI | connects between the web server Nginx and the web application Django |
| WSGI, Webserver Gateway Interface | manage the actions performed by the Web server and the Web application |


<br> 

### Nginx

Nginx (pronounced "engine x") is software to provide a web server. It can act as a reverse proxy server for TCP, UDP, HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer and an HTTP cache.
Created by Igor Sysoev in 2002, Nginx runs on Unix, Linux, BSD variants, OS X, Solaris, AIX, HP-UX, and Windows.[6] Released under the terms of a BSD-like license, Nginx is free and open source software. A company of the same name was founded in 2011 to provide support.[8]
 
<br>
 
2002년부터 러시아의 프로그래머 이고르 시쇼브(Игорь Сысоев)가 Apache(아파치)를 코딩하다 Apache의 C10K 문제[1]를 보고 이를 극복하면서 네이티브 Win32환경에도 돌아갈 무설치 웹 서버 프로그램에 대한 개발을 시작하여 2004년 스푸트니크 1호 발사일에 발표한 오픈소스 서버 프로그램. 현재 이고르 시쇼브와 그가 설립한 회사인 Nginx Inc.가 이 프로젝트를 운영중에 있다. 목표는 가벼우면서도 강력한 프로그램이라고... HTTP와 리버스 프록시, IMAP/POP3등의 서버를 구동가능하다. 
읽을때는 엔진엑스라고 읽는다. 역사가 그렇게까진 오래되진 않아서 점유율 면에서 Apache에게 많이 밀린다. 하지만 신규서비스를 중심으로 점유율에 가속이 붙는 중이며, 이미 Apache가 여러가지면에 한계를 많이 보였으므로 특별히 큰 사유가 없다면 nginx로 갈아타는 추세다. 다만 확장 모듈이 Apache에 비해 적다는 것이 흠인데, 어차피 Apache의 이 많은 확장 모듈을 제대로 쓰는 사람은 드물다. 오히려 쓰지도 않으면서 괜히 덕지덕지 리소스만 낭비하는 모듈이 대부분이다. 따라서 호환성 확인 후 별다른 문제가 없다면 Nginx로 갈아타는 것이 현추세. 이미 필수적인 모듈은 Nginx에도 존재하고 그중 몇개는 Apache보다 50배 이상 빠르다(...) 마이크로소프트에게는 GUI관리가 쉬운 IIS에 밀리지만, 이쪽은 취향과 돈의 문제라서 1:1 비교가 힘들다.
구조적으로는 Apache에서 사용하는 스레드/프로세스 기반 구조 대신 비동기 이벤트 기반 구조를 가진다. 이로 인해서 서버 부하시 성능 예측이 쉽다. 덤으로 이로 인하여 10000개의 동시 접속을 하면 그 10000개에 드는 메모리 점유는 2.5MB다(....) 사용하는 리눅스 웹서버의 경우 LAMP(Linux + Apache + MySQL + PHP or Python or Perl)대신 LEMP를 쓴다. Nginx는 여러 서드파티 기능들(SSL, GeoIP등)을 모듈로 덧 붙이는 방식을 쓰고 있으며, 그래서 모듈을 쓰지 않을 경우 제외해 놓을 수 있다, 단, 소스 컴파일시 모듈을 추가하지 않으면, 그 이후에 추가가 안되지만...
 
- 웹 서버를 구현하기 위한 소프트웨어이다. 
- Software for providing Web services 
- Nginx vs Apache  


<br>

### WSGI
Between the server and the application, there may be a WSGI middleware, which implements both sides of the API. The server receives a request from a client and forwards it to the middleware. After processing, it sends a request to the application. The application's response is forwarded by the middleware to the server and ultimately to the client.

<br> 

기존의 파이선 웹 애플리케이션 프레임워크는 웹서버를 선택하는데 있어서 제약이 있었다. 보통 CGI, FastCGI, mod_python 과 같은 커스텀API 중에 하나만 사용할 수 있도록 디자인 되었는데, WSGI는 그에 반하여 low-level로 만들어져서 웹서버와 웹 어플리케션,프레임워크간의 벽을 허물었다.
WSGI는 서버와 게이트웨이 , 애플리케이션과 프레임워크 양단으로 나눠져있다. WSGI 리퀘스트를 처리하려면, 서버단에서 환경정보와 콜백함수를 애플리케이션단을 제공해야한다. 애플리케이션은 그 요청을 처리하고 미리 제공된 콜백함수를 통해 서버단에 응답한다. WSGI 미들웨어(라고 불린다.)가 WSGI 서버와 애플리케이션 사이를 보충해주는데, 이 미들웨어는 서버의 관점에서는 애플리케이션으로, 애플리케이션의 관점에서는 서버로 행동한다. 이 미들웨어는 다음과 같은 기능을 가진다.

- middleware for python web application 
- low-level 
- Python framework 
- uWSGI
  - It doesn't specifically say, but I'm guessing that uWSGI is one of these middlewares. My understanding is that uWSGI acts as an adapter around your Flask app so that Flask (or any other framework you want to use) doesn't have to know specifically how to implement the app side of the WSGI specification. So to answer my own question, uWSGI and Flask together form the app side of WSGI and nginx is the web server side.


### Zsh 

Zsh is a shell designed for interactive use, although it is also a powerful scripting language. More information can be found on the "Zsh Web Pages" sites.
The Z shell (zsh) is a Unix shell that can be used as an interactive login shell and as a powerful command interpreter for shell scripting. Zsh is an extended Bourne shell with a large number of improvements, including some features of bash, ksh, and tcsh.


### pip list vs pip freeze 

| pip list | pip freeze | 
| -- | -- | 
| List installed packages, including editables. | Output installed packages in requirements format. | 


<br>

```

# Use the pem to connect to the amazon server 
    $ chmod 400 ssh_test_2.pem
    $ ssh -i /Users/hongdavid/Documents/FastCampus/ssh_test_2.pem ubuntu@ec2-52-78-230-12.ap-northeast-2.compute.amazonaws.com


# Install Language pack 
    $ sudo apt-get install language-pack-ko
    $ sudo locale-gen ko_KR.UTF-8


# python pip install 
    $ sudo apt-get install python-pip
 

# installing zsh 
  - the console interface shoud change after this install 
    $ sudo apt-get install zsh
    $ sudo curl -L http://install.ohmyz.sh | sh
    $ sudo chsh ubuntu -s /usr/bin/zsh


# install pyenv 
    $ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \ libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
    $ curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash


# list the pyenv configuration to .zshrc 
    $ vi ~/.zshrc
        export PATH="/home/ubuntu/.pyenv/bin:$PATH"
        eval "$(pyenv init -)"
        eval "$(pyenv virtualenv-init -)" 


# install pillow 
    $ sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev \ libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
    
    
# Update authority of Django Directory 
    $ sudo chown -R ubuntu:ubuntu /srv/ 


# create django project in local
    $ pyenv install 3.4.3 
    $ pyenv virtualenv 3.4.3 mysite 
    $ pyenv local { name }

    $ pip install django 
    $ pip freeze > requirements.txt 
    $ django-admin startproject { name }
    $ vi settings.py 
      ALLOWED_HOSTS = ['.amazonaws.com', ]



# clone the django project to server 
    $ git clone { address }
    $ export LC_ALL=C
    $ pip install -r requirements.txt 
    $ python manage.py runserver 0:8080


# add 8080 port in amazon server 
  - (Bottom UI) Security groups / launch-wizard-3 
  - (BOTTOM UI) Inbound -> add protocol 8080



# add user for managing the web application 
   - the root should not manage the application 
    $ sudo adduser nginx

   
    /* there may be a error in the pyenv mainly caused by the server  */  
        - exit the server and enter it again 
        - you might have to install the whole process regarding to pip  



# create mysite.ini for uWSGI site connection 
    $ pip install uwsgi
    $ uwsgi --http :8080 --home ~/.pyenv/versions/mysite --chdir /srv/mysite_tutorial_2/mysite -w mysite.wsgi


# create uWSGI site file for easy access 
    $ sudo mkdir /etc/uwsgi
    $ sudo mkdir /etc/uwsgi/sites
    $ sudo vi /etc/uwsgi/sites/mysite.ini
    
    [uwsgi]
    project = mysite
    base = /srv
    chdir = %(base)/%(project)/django_app
    module = %(project).wsgi:application
    home = /home/ubuntu/.pyenv/versions/mysite
    
    uid = nginx
    gid = nginx
    
    socket = /tmp/mysite.sock
    chmod-socket = 666
    
    enable-threads = true
    master = true
    pidfile = /tmp/mysite.pid


# Run wsgi file 
    $ uwsgi --http :8080 -i /etc/uwsgi/sites/mysite.ini


# add uWSGI init ifle 
    $ sudo vi /etc/systemd/system/uwsgi.service

    [Unit]
    Description=uWSGI Emperor service
    After=syslog.target
    
    [Service]
    ExecPre=/bin/sh -c 'mkdir -p /run/uwsgi; chown nginx:nginx /run/uwsgi'
    ExecStart=/home/ubuntu/.pyenv/versions/mysite/bin/uwsgi --uid nginx --gid nginx --master --emperor /etc/uwsgi/sites
    
    Restart=always
    KillSignal=SIGQUIT
    Type=notify
    StandardError=syslog
    NotifyAccess=all
    
    [Install]
    WantedBy=multi-user.target

```






