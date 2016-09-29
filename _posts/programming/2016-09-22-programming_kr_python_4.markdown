---
published: true
title: 파이썬 중급 4일차
layout: post
category: programming
permalink: /programming_kr/python_4
---

### 클래스
1. Animal Class
2. State type(string): "dog", "cat", "fish"
3. State type weight :
4. Behavior "먹이를 먹습니다."


``` python

class Animal:
    def __init__(self, name, weight):
        self.weight = weight
        self.name = name

    # polymorphism
    # 함수가 다른 형태로 사용할 수 있을 떄
    # - Parametic Polymorphism

    def eat(self, *args):
        #print([i for i in args])
        if not args:
            print("먹이를 먹습니다.")
        else:
            print("\n".join(i+"를 먹이를 먹습니다." for i in args))

    def swim(self):
        print("swim" if self.name=="fish" else "dead")


    def weight_is_heavier_than(self, other):
        print(self.name+"이 더 무겁습니다." if self.weight > other.weight else other.name+'이 더 무겁습니다.' )



d4 = Animal("dog", 4)
d4 = Animal("dog", 4)
c6 = Animal("cat", 6)
c3 = Animal("cat", 3)
f1 = Animal("fish", 1)


f1.eat("소세지","햄버거")
f1.swim()
d4.swim()

```

<br>

### 상속

1. 삼각형 사각형
2. width, height를 가진다.
3. area = w * h / 2, area = w * h

``` python

class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def is_bigger_than(self, other):
        return True if self.area() > other.area() else False


class Rect(Shape):
    def area(self):
        return self.width * self.height


class Tri(Shape):
    def area(self):
        return (self.width * self.height) / 2


r1 = Rect(10,20)
t1 = Tri(10,20)

print(r1.area())
print(t1.area())
print(r1.is_bigger_than(t1))

```

<br>

### 클래스 비교

``` python

# method overriding

class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # area 선언 안 했을 경우 문제를 해결
    def area(self):
        return "오류"

    def is_bigger_than(self, other):

        # Shape를 상속받지 않는 다른 객체와 비교 시
        if not isinstance(other, Shape):
            return "오류"
        return True if self.area() > other.area() else False


class Rect(Shape):
    def area(self):
        return self.width * self.height


class Tri(Shape):
    def area(self):
        return (self.width * self.height) / 2


r1 = Rect(10,20)
t1 = Tri(10,20)

print(r1.area())
print(t1.area())
print(r1.is_bigger_than(t1))

# instance 비교
print(type(t1) is Tri)

# instance 비교2
print(isinstance(t1, Tri))

# instance 비교3 하위 클래스 여부 확인
print(issubclass(Tri, Shape))

# instance or 비교
print(isinstance("string", (str, int)))
print(isinstance("string", (int)))



class Animal:
    def __init__(self, weight):
        self.weight = weight

    # polymorphism
    # 함수가 다른 형태로 사용할 수 있을 떄
    # - Parametic Polymorphism

    def eat(self, *args):
        # print([i for i in args])
        if not args:
            print("동물이 먹이를 먹습니다.")
        else:
            print("\n".join(i + "를 동물이 먹습니다." for i in args))


    def weight_is_heavier_than(self, other):

        if type(self) is type(other):
            print(True if self.weight > other.weight else False)
        else:
            print("Different anmial")


class Dog(Animal):

    # Method overriding
    def eat(self, *args):
        # print([i for i in args])
        if not args:
            print("개가 먹이를 먹습니다.")
        else:
            print("\n".join(i + "를 개가 먹습니다." for i in args))

class Cat(Animal):
    pass

class Fish(Animal):

    def swim(self):
        print("fish is swimming")


d4 = Dog(4)
d4 = Dog(4)
c6 = Cat(6)
c3 = Cat(3)
f1 = Fish(1)

f1.weight_is_heavier_than(c6)
c6.weight_is_heavier_than(c3)

f1.eat("소세지", "햄버거")
d4.eat("피자")
f1.swim()
#d4.swim()



# 1. 객체 클래스 인스턴스
# 2. tri  = triangle ==True
# 2. tri  = Shape == Fale

```

<br>

### Instance, Class, Static method

``` python

class Awesome():

    def what():                     #self equals no instance
        return "what"

    def my_instance_method(self):   #instance method
        return self

    @classmethod
    def my_class_method(cls):       #class method
        return cls

    @staticmethod
    def my_static_method():         #static method
        return "static"

awsome = Awesome()

#instance method
print(awsome.my_instance_method())

#class method
print(awsome.my_class_method())

#static method
print(awsome.my_static_method())
print(Awesome.my_static_method())

print(Awesome.what())
#error
print(awsome.what())

```

<br>

### 실습 예제 - 로그인

``` python

# login_required    유저 정보가 포함되어 있는지
# is_admin          유저가 관리자인지



# user_class : username, is_admin
# Request      user instance ( user 0 => login  user X => invalid login)
#
# Response     사용자에게 줄 메시지


class Request:
    def __init__(self, url, user=None):
        self.url = url
        self.user = user

class Response:
    def __init__(self, body):
        self.body = body
    pass

    def __repr__(self):
        return "Response :: {body}".format(body=self.body)

class User:
    def __init__(self, name , is_admin = False):
        self.name = name
        self.is_admin = is_admin


def home(request):
    pass


def mypage(request):
    if request.user:
        response = Response("정상적으로 접속")
    else :
        response = Response("로그인 필요")
    return response




user1 = User("sunghohong")
user2 = User("sunghohong2", is_admin= True)


request = Request("/mypage", user1)
request2 = Request("/mpage")


#print(mypage(request))
#print(mypage(request2))


#decoration
def login_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user:
            #print(request.user.is_admin)
            response = func(request, *args, **kwargs)
        else:
            response = Response("로그인이 필요합니다.")
        return response
    return wrapper


@login_required
def mypage(request):                            # decorator :: login_required !!!
    return Response("성공적으로 MyPage 에 접속했습니다.")


request = Request("/mypage/")
print(mypage(request))

request = Request("/mypage/", user1)
print(mypage(request))


def is_admin(func):
    def wrapper(request,*args, **kargs):
        if request.user and request.user.is_admin:
            response = func(request, *args, **kargs)
        else:
            response = Response("관리자 권한이 필요합니다.")
        return response
    return wrapper


@is_admin
@login_required
def admin(request):
    return Response("admin에 성공적으로 접속했습니다.")


request = Request("/admin/", user2)
print(admin(request))

# 현재는 로그인 권한과 관리자 권한 두개 다 작동한다.
request = Request("/admin/")
print(admin(request))


#home(request) #response의 객체 (body => home)

```

<br>

### Web Crawling

1. 정적인 사이트 - 네이버 홈페이지
2. 동적인 사이트 - client에서 data가 rendering, ajax 등으로 javascript로 data를 받는다.
3. 국내 사이트 (Javascript) - 사내 인트라넷 등 등
4. 한국형 사이트 : iFrame - 네이버 카페, 옛날 사이트

``` python

# web crawling
import requests
from bs4 import BeautifulSoup

response = requests.get("http://naver.com")

#print(response.text)
#print("윤보미" in response.text)

# tag= ol id = realrank
# 10 lists inside the tag
# css selector ol #realrank li

# tag 파일들을 보기 좋게 parsing
result = BeautifulSoup(response.text)

# ol tag만 별도로 추출
elements = result.select("ol#realrank li")


#element = elements[0]
#print(element.select_one("a").attrs["title"])
print([element.select_one("a").attrs["title"] for element in elements[:-1:]])

```
