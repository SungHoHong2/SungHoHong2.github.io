---
published: true
title: 파이썬 중급 3일차
layout: post
category: programming_kr
permalink: /programming_kr/python_3
---

### 함수 

함수를 리턴하는 함수 중에서 decorator가 존재
<br> 함수의 실행 시간을 측정하는 함수 
<br> Decorator 사용 방법 

``` python

import time

# 실행 시간 맞추기

def hello():
    print("hello")


start_time = time.time()
hello()
end_time = time.time()
exec_time = end_time - start_time
print("Execute time : {time}".format(time = exec_time))



# 문제가 있는 함수
# 1. 시간을 계속 새롭게 체크해야 한다.
# 2. 인자를 명시적으로 모든 함수에 대해서 정의해 줘야 한다.

def new_hello():
    start_time = time.time()
    hello()
    end_time = time.time()
    exec_time = end_time - start_time
    print("Execute time : {time}".format(time=exec_time))


def get_multiply_by(n):
    def return_function(x):
        return x * n
    return return_function


double = get_multiply_by(2)
print(double(100))
print(get_multiply_by(2)(100))


```


<br> 

### Decorator 

함수를 input으로 받아서 새로운 함수를 만들어서 리턴하는 것 
<br> wrapper라고도 한다. 

``` python 

def start_time(func):
    print("start function")
    def wrapper(*args, **kwargs):
        print("========start function======")
        return func(*args, **kwargs)
    return wrapper


def end_time(func):
    print("end function")
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("========end function======")
        return result
    return wrapper


def track_time(func):
     print("tack_time")
     def new_func(*args, **keyargs):
         start_time = time.time()
         func([args][0][0])
         end_time = time.time()
         exec_time = end_time - start_time
         print("Execute time : {time}".format(time=exec_time))

     return new_func


@track_time
@end_time
@start_time
def hello(name):
    print("안녕하세요 {name} 입니다.".format(name=name))


#hello = track_time(hello)
hello("안수찬")

#wrapper 실행 순서

    #start_function 선언
    #end_function 선언 
    #track_function 선언 
 
    #start_inner_function의 함수 실행 -> print한 다음에 함수 
    #end_inner_function 함수 실행 -> 함수 실행 후 print 
    #track_inner_function 함수 실행  -> 함수 실행 후 prin

```


<br>

### List, Dict 예제 
1. 배열 타입을 입력할 것 ["fast", "campus", "fast", "campus", "school", "fast", "fast"]
2. for 
3. lambda 
4. comprehensive 
5. 가장 많이 누적된 점수 순서로 출력할 것
 
```python

data = ["fast", "campus", "fast", "campus", "school", "fast", "fast"]


# fast      ====
# campus    =
# school    =


def parameter(arg):

    argdict = {
        "fast" : 0,
        "campus" : 0,
        "school" : 0
    }
    
    for i in data:
        argdict[i] +=1

    for key, value in argdict.items():
        rtn = key+'\t'
        rtn+=''.join(['#' for i in range(value)])
        print(rtn)
    return argdict

parameter(data)


data = ["fast", "campus", "fast", "campus", "school", "fast", "fast"]


# fast      ====
# campus    =
# school    =


def parameter(arg):

    argdict = {
        "fast" : 0,
        "campus" : 0,
        "school" : 0
    }

    for i in data:
        argdict[i] +=1

    for key, value in argdict.items():
        rtn = key+'\t'
        rtn+=''.join(['#' for i in range(value)])
        #print(rtn)
    return argdict

parameter(data)



ele = ["fast", "campus", "fast", "campus", "school", "fast", "fast"]

def histogram(elements):
    hist = {}
    for key in elements:
        hist[key] = 0

    for key in elements:
        hist[key]+=1

    for key, value in hist.items():
        rtn = "{key}{space}{histogram}".format(key=key, space= " "*(10-len(key)),histogram="#"*value)
    #   print(rtn)


    #list comprehension
    print("\n".join(["{key}{space}{histogram}".format(key=key, space= " "*(10-len(key)),histogram="#"*value) for key, value in hist.items()]))


    #lambda
    print("\n".join(list(map(lambda key:"{key}{space}{histogram}".format(key=key, space= " "*(10-len(key)), histogram="#"*hist[key]), hist))))


    #sort
    print(sorted(hist))
    print(sorted(hist, key=lambda key: hist[key]))
    print(sorted(hist, key=lambda key: hist[key])[::-1])
    
print(histogram(ele))


```


<br>

### 피보나치 수열 
1. 숫자를 입력할 것 
2. 해당 숫자만큼의 마지막 피보나치 수자를 리턴할 것 
3. for 문 
4. recursive 

``` python

# 0, 1, 1, 2, 3, 5, 8
def fibo(n):
    #n 번째 피보나치 수열을 return

    first, second = (0, 1)
    rtn = 0
    #print(first)
    #print(second)

    for i in range(n):
        temp = second
        second = second + first
        first = temp
        #print(second)
        rtn = second
    return rtn

print(fibo(10))

```

<br>

### Recursive 

``` python

def fibo_recur(n):
    return n if n < 2 else fibo_recur(n-1)+fibo_recur(n-2)

print(fibo_recur(10))





def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
    
    
# f(5) = f(4) + f(3)
#      = (f(3) + f(2)) + (f(2) + f(1))
#      = ((f(2) + f(1))) ...

```

<br>

### 동적 계획법 Memoization 

- 결과값을 저장해두는 방법 - memoization
- 동적 계획법 - 기억하며 풀기
- recursive로 작성된 함수에다가 decoration을 사용해서 memoization 적용하기

``` python

def fibo_recur(n):
    return n if n < 2 else fibo_recur(n-1)+fibo_recur(n-2)

__fibo_recursive_cache = {}

def fibo_cache(n):
    if n in __fibo_recursive_cache:
        return __fibo_recursive_cache[n]
    else:
        result = n if n < 2 else fibo_recur(n - 1) + fibo_recur(n - 2)
        __fibo_recursive_cache[n] = result
        return result

print(fibo_cache(10))


def memoize(func):
    __cache = {}
    def wrapper(*args):
        print(__cache)
        if args in __cache:
            return __cache[args]
        else:
            __cache[args]= func(*args)
            return __cache[args]
    return wrapper


@memoize
def fibo_recur(n):
    return n if n < 2 else fibo_recur(n-1)+fibo_recur(n-2)

print(fibo_recur(10))



# Refractor 과정 1 

def memoize(func):
    __cache = {}
    def wrapper(*args):
        print(__cache)
        if args in __cache:
            return __cache[args]
        else:
            __cache[args]= func(*args)
            return __cache[args]
            #return __cache.update({args: func(*args)}) or __cache[args]
    return wrapper


# Refractor 과정 2 

def memoize(func):
    __cache = {}
    return lambda *args: __cache[args] if args in __cache else __cache.update({args: func(*args)}) or __cache[args]


@memoize
def fibo_recur(n):
    return n if n < 2 else fibo_recur(n-1)+fibo_recur(n-2)

print(fibo_recur(10))

```

<br>

### 클래스 

1. 절차 지향적 프로그래밍 data, function
2. 객체 제향 프로그래밍, Object - 상태, 행동(Behavior == Function) 
3. 함수형 프로그래밍, Function(stateless), CommonList(Scheme), o'Camal - 굉장히 희귀한 언어 
4. SICP 컴퓨터 프로그램의 구조와 해석 - 이색적인 시각으로 컴퓨터를 다시 해석   

``` python

# Class, Object, Instance
# A는 Object이다.
# A는 사람 Class의 Instance이다

# 클래스를 객체로 실체화 하는 과정
class Person():
    #name = "Nonamed"
    #age = 0

    def __init__(self, name, age):
        print("사람 생성했습니다.")
        self.name = name
        self.age = age

    def __add__(self, other):
        print("{myname}이 {partner}와 적극적으로 만난다.".format(myname = self.name, partner = other.name))

    def hello(self):
        print("안녕하세요 {age}살 {name} 입니다.".format(name=self.name, age = self.age))

    def meet(self, another):
        print("{myname}이라는 사람이 {another_name}을 만났습니다.".format(myname= self.name, another_name =another.name))

    def __str__(self):
        return self.name


a = Person("",0)

print(Person) #Class
print(a) #Object
print(a.name)
print(a.age)


# 클래스에 값 입력 가능
a.name = "안수찬"
a.age = 30

print(a.name)
print(a.age)


# Class내 Function 실행하기
a.hello()


# 기본적으로 변수의 은닉 개념이 있는가?
b = Person("홍성호", 29)
b.hello()


# 타 클래스 입력
a.meet(b)
a.__add__(b)
print(a)



# Triangle
# width , height
# get_area, is_bigger_than

class Triangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        self.area = int((self.width*self.height)/2)
        return self.area

    def is_bigger_than(self, other):
        return self.area if self.area>other.area else other.area


a = Triangle(10,20)
b = Triangle(20,30)

print(a.get_area())
print(b.get_area())
print(a.is_bigger_than(b))

```
