---
published: true
title: 파이썬 중급 2일차
layout: post
category: programming_kr
permalink: /programming_kr/python_2
---

### 예제 문제

1. n input을 받아서 n개의 짝수 리스트를 생성하기 (100 -> 0..198)

2. n input으로 받아서 n보다 작은 짝수 리스트를 만드는 함수 (0..98)


``` python

#1번 문제
def get_even_list(n):
    result = []
    n = 100
    for i in range(n):
        element = i * 2
        result.append(element)

    return result

print(get_even_list(100))


#2번 문제
def is_even(num):
    return True if num%2 == 0 else False

returnList = []

for i in range(100)[1::]:
    returnList.append(i) if is_even(i) else False

print(returnList)


# 한줄로 if절 해결하기
# 3의 배수 5의 배수 리스트
#  100 개의 element가 들어간 list 2개 만들기
#  1. list : ["","","fast","","","fast"]
#  2. list : ["","","","","campus",]
#  3. list : [","","fast", ","campus,"fast",..."fastcampus"]


n = 100
result = []
for i in range(n):
    result.append("fast") if (i+1) % 3 == 0 else result.append("")

# print(result)


result2 = []
for i in range(n):
    result2.append("campus") if (i+1) % 5 == 0 else result2.append("")

#print(result2)

result3 = []
for i in range(n):
        element = ('fast' if (i+1) % 3 == 0 else "") + ('campus' if (i+1) % 5 == 0 else "")
        result3.append(element)

print(result3)


#함수 형태로 만들기
def insert_data(list1, list2):

    returnList = []
    paramTuple = (list1, list2)

    for i in range(100)[1::]:
        element = ""
        for p in paramTuple:
            name, num = p
            element+= name if (i)%num==0 else ""
        returnList.append(element)

    return returnList

print(insert_data(("fast", 3), ("campus",5)))




#n 까지의 소수 (100)  =  [2,3,5,7,11, ... 97]

result = []
for i in range(100)[2::]:
      check = 0
      for s in range(i)[2::]:
            if s!=0:
                check += (1 if i%s ==0 else 0)

      if check == 0:
          result.append(str(i))
print(result)


def is_prime(n):
    for i in range(2,n):
        if n % i == 0 :
            return False
    return True


result1 = []
for i in range(100)[2::]:
    result1.append(i) if is_prime(i) else False

print(result1)

```

<br>

### function의 argument와 kwargs (pack, unpack)

``` python

def get_awesome_list(n, rule1, rule2):
        result =  []
        for i in range(n):
            element = ""
            for rule in [rule1, rule2]:
                div, text = rule
                element += text if (i+1)%div == 0 else ""
            result.append(element)
        return result



print(get_awesome_list(100, (3, "fast"), (5, "campus")))


```

<br>


### Functional Programming
1. Lambda
2. Labmda Operator = map, filter, reduce

``` python

# map - element에 대해서 동일한 함수를 적용

def get_sum(paramList):
    sum = 0;
    for i in paramList:
        sum+=i
    return sum


def get_max(paramList):
    max = paramList[0]
    for i in paramList:
            max = i if(max<i) else max
    return max


def double(x):
    return x * 2
print(list(map(double, range(100))))

def checkNum(n):
    return n if (n+1) % 3 else ""
print(list(map(checkNum, range(100))))


# ... fast

def checkFast(n):
    return "fast" if (n+1) % 3 == 0  else ""
print(list(map(checkFast, range(100))))


# Lambda Operator
print(list(map(lambda x : x*2, range(100) ) ) )
print(list(
        map(
           lambda x: "fast" if (x+1)%3==0 else ""
        , range(100) )
       ) )


# List Comprehension
# [1,2,3]
# [___________ for ______ in _________] # == MAP

print([i for i in range(5)])

print([i*2 for i in range(5)])

print(["fast" if (i+1)%3==0 else "" for i in range(100)])

```


### 추가 의문사항

1. Reflection 가능여부 확인하기


