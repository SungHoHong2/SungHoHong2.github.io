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




