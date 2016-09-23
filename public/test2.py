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

import matplotlib as inline



