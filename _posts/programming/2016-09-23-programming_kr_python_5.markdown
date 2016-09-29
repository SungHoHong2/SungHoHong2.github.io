---
published: true
title: 파이썬 중급 5일차
layout: post
category: programming_kr
permalink: /programming_kr/python_5
---

### Web Crawling

1. html 파일을 가져오는 단계 = scraping, crawling
2. html 파일을 텍스트만 추출  = parsing
3. Web crawling이 안되는 경우
- ip: Server를 차단했을 가능성 존재
- ncount: 초당 request 수를 제한
- requests.get 패키지 HTTP Request Headers에 탐색하여 차단 (Headers :: User-Agent에 사용자 기기 나옴 )

``` python

post_elements = bs.select("ul#elThumbnailResultArea li.sh_blog_top")
#print(len(post_elements))

#HEADERS에 들어갈 내용
IPAD_USER_AGENT = 'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10'
response = requests.get(
    "https://search.naver.com/search.naver?where=post&sm=tab_jum&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"
    , headers = {
       "User-Agent": IPAD_USER_AGENT
    }
)

bs = BeautifulSoup(response.text, "html.parser")
post_elements = bs.select("ul#addParemt li.api_bx")

#print(len(post_elements))
#print([post for post in post_elements])

#텍스트 조회
for post in post_elements:
    print(post.select_one("div.dsc_txt").text)

```

<br>

### Daum 블로그 페이지별 Crawling 

``` python

# dict의 리스트
# [{}, {}, {}]
# 1 - 10 페이지


import requests
from bs4 import BeautifulSoup

response = requests.get("http://search.daum.net/search?w=blog&nil_search=btn&DA=NTB&enc=utf8&q=%ED%8C%8C%EC%9D%B4%EC%8D%AC")
bs = BeautifulSoup(response.text, "html.parser")

#post_elements = bs.select("ul#blogResultUl li")

post_elements = bs.select("ul#blogResultUl > li")


#print(len(post_elements))

#for post in post_elements:
#    print(post.select_one("div.wrap_tit").text.replace("\n",""))


print([{
         "title" : post.select_one("div.wrap_tit").text.replace("\n","")
        ,"detail" : post.select_one("p.f_eb").text.replace("\n","")
         } for post in post_elements])

# pagination


result =  []
for i in range(10)[1::]:
    response = requests.get("http://search.daum.net/search?w=blog&nil_search=btn&DA=PGD&enc=utf8&q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&page={page}&m=board".format(page=i))
    bs = BeautifulSoup(response.text, "html.parser")
    post_elements = bs.select("ul#blogResultUl > li")
    result.append([{
                    "title": post.select_one("div.wrap_tit").text.replace("\n", "")
                  , "detail": post.select_one("p.f_eb").text.replace("\n", "")
                   } for post in post_elements])


for pages in result:
    for page in pages:
        print(page)

```


<br>

### Iterator 

1. Django Generator를 만들 떄 사용된다. 
2. Iterable의 뜻은 반복하다 
3. iter() : iterator가 조회된다.
4. next() : element가 조회된다. 

- List :: element
- Dict :: key
- Tuple :: element
- Set :: element
- String :: char(str) 

```python

animals = ['dog','cat', 'monkey']

for animal in animals:
    print(animal)

#Iterator
#print(animals.__iter__())           # List_iterator 객체 조회
#print(iter(animals))

animals_iterator = animals.__iter__()
print(animals_iterator.__next__())
print(next(animals_iterator))

#elements - > element iterator로 바꾼 다음에 -> next로 조회한다.



# Iterator 생성 -> __next__
# Iterable -> __iter__

class myrange:
    def __init__(self, n):
        self.i, self.n = (0, n)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


#for i in myrange(5):
#    print(i)

#for i in range(5):
#    print(i)


m1 = myrange(10)

# 데이터 조회
print(list(m1))

# 데이터 손실
print(list(m1))


class myrange_basic:      #iterable
    def __init__(self, n):
        self.n = n

    # 데이터가 중도에 소실되는 것을 방지
    def __iter__(self):
        return myrange_iterator(self.n)


class myrange_iterator:   #iterator
    def __init__(self, n):
        self.i, self.n = (0, n)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


m1 = myrange_basic(10)

# 데이터 조회
print(list(m1))

# 데이터 손실없음
print(list(m1))

```

<br>

### Generator 

```python

# Generator

# Iterable => __iter__() iterator expected
# Iterator -> __next__() element .. stopIteration
# Generator -> function, Iterator 처럼 동작하는 것



class myrange:      #iterable
    def __init__(self, n):
        self.n = n

    # 데이터가 중도에 소실되는 것을 방지
    def __iter__(self):
        def myrange_iterator(n):
            i = 0
            while i < n:
                yield i
                i += 1

        return myrange_iterator(self.n)



myr = myrange(5)

for i in myrange(5):
    print(i)


def onetwothreefour():
    yield 1
    yield 2
    yield 3

g = onetwothreefour()
print(next(g))
print(next(g))
print(next(g))

```

<br>

### eval 

```python

def hello(n):
    return "hello"+n

print(eval("hello('howdy')"))

```

<br>

### ZIGBANG Web Crawling


```python

# 직방 ,요기요
import matplotlib as matplotlib
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


#자바스크립트로 동적으로 조회하기 떄문에 data crawling 불가능

#동적인 사이트
#== ajax (Async Javascript and XML)
response = requests.get("https://api.zigbang.com/v1/items?detail=true&item_ids=5985974&item_ids=5793633&item_ids=5555080&item_ids=5409409&item_ids=5972371&item_ids=5861743&item_ids=5993628&item_ids=5992354&item_ids=5813973&item_ids=5917050&item_ids=5903678&item_ids=5930937&item_ids=5858510&item_ids=5969042&item_ids=5743201&item_ids=5833579&item_ids=5935541&item_ids=5722862&item_ids=5787543&item_ids=5969192&item_ids=5840644&item_ids=5969060&item_ids=5859401&item_ids=5977848&item_ids=5778974&item_ids=5927356&item_ids=5943157&item_ids=5878975&item_ids=5784078&item_ids=5699557&item_ids=5991054&item_ids=5725391&item_ids=5959937&item_ids=5722828&item_ids=5812772&item_ids=5792026&item_ids=5961598&item_ids=5943522&item_ids=5764613&item_ids=5971627&item_ids=5886699&item_ids=5974668&item_ids=5744452&item_ids=5620726&item_ids=5978170&item_ids=5940459&item_ids=5599580&item_ids=5892167&item_ids=5893804")#print(response.text)

#JSON API
# JavaScript Object Notation
# Javascript Object = Key - Value : Dictionary


#DIC -> JSON
student = {"name": "hello"}
student_text = json.dumps(student)
#print(student_text)

#JSON -> DIC
student = json.loads(student_text)
#print(student)

dic = json.loads(response.text)
#print(dic)

#{"deposit": 3000, "rent":300}


zigbang = json.loads(response.text)

rooms = [
    {
        "room_id": item.get("item").get("id"),
        "deposit": item.get("item").get("deposit"),
        "rent": item.get("item").get("rent"),
    }
    for item
    in zigbang.get("items")
]

#print(rooms)

fp = open("zigbang.csv","w")
fp.write("room_id, deposit, rent \n")
fp.write("\n".join(["{room}, {deposit}, {rent}".format(room=room.get("room_id"), deposit = room.get("deposit"), rent=room.get("rent")) for room in rooms]))
fp.close()


# noSQL - JSON DATA가 고스란히 저장이 가능
# JSON DATA 자체를 파일형태로 저장

json.dump(
    zigbang,
    open("zigbang.json", "w"),
)
# json.load(open("zigbang.json", "r"))



#PANDAS 사용

df = pd.DataFrame(rooms)

#print(df)
#print(df.head())
#print(df.describe())

#print(df.deposit) #COL
#print(df.loc[0])  #ROW

print(pd.DataFrame(
    item.get("item") for item in zigbang.get("items")
))

```

<br>

### Yogiyo Web Crawling

```python

import requests
from bs4 import BeautifulSoup

import json
import pandas as pd



response = requests.get(
    "https://www.yogiyo.co.kr/api/v1/restaurants-geo/?items=20&lat=37.5157252&lng=127.02130830000002&order=rank&page=0&search=&zip_code=137030",
    headers={
        "X-ApiKey": "iphoneap",
        "X-ApiSecret": "fe5183cc3dea12bd0ce299cf110a75a2",
    }
)

#yogiyo = json.loads(response.text)
yogiyo = response.json()
rtn = pd.DataFrame(yogiyo.get("restaurants"))

rtn.to_excel("yogiyo.xls")

print(rtn)

```

