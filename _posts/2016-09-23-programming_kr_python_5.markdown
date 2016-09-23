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


### Iterator 

1. Django Generator를 만들 떄 사용된다. 
2. Iterable의 뜻은 반복하다 

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

```




