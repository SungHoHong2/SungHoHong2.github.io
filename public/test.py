import requests
from bs4 import BeautifulSoup

response = requests.get("https://search.naver.com/search.naver?where=post&sm=tab_jum&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC")
bs = BeautifulSoup(response.text, "html.parser")

post_elements = bs.select("ul#elThumbnailResultArea li.sh_blog_top")
#print(len(post_elements))

#HEADERS에 들어갈 내용
IPAD_USER_AGENT = 'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10'
response = requests.get(
    "http://money.cnn.com/2016/08/30/technology/obama-wired-magazine/index.html"
    , headers = {
       "User-Agent": IPAD_USER_AGENT
    }
)

print(response.text)















