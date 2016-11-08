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



<br>

```

# unsupported LOCAL settings while using pip list 

$ export LC_ALL=C

$ locale
LANG=en_US.UTF-8
LANGUAGE=
LC_CTYPE="C"
LC_NUMERIC="C"
LC_TIME="C"
LC_COLLATE="C"
LC_MONETARY="C"
LC_MESSAGES="C"
LC_PAPER="C"
LC_NAME="C"
LC_ADDRESS="C"
LC_TELEPHONE="C"
LC_MEASUREMENT="C"
LC_IDENTIFICATION="C"
LC_ALL=C

```






