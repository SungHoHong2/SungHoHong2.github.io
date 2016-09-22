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


# 1. 정적인 사이트 - 네이버 홈페이지
# 2. 동적인 사이트 - client에서 data가 rendering, ajax 등으로 javascript로 data를 받는다.
# 3. 국내 사이트 (Javascript) - 사내 인트라넷 등 등
# 4. 한국형 사이트 : iFrame - 네이버 카페, 옛날 사이트


