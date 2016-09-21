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


### 데이터 분석 



