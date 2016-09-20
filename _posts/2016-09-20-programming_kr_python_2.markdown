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

def get_even_list(n):
    result = []
    n = 100
    for i in range(n):
        element = i * 2
        result.append(element)

    return result

print(get_even_list(100))


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

### List Comprehension

``` python


# get_sum


# get_max




```


