import requests
import re
import prettytable
import json
from flight_address import Address

from_city = input('出发城市:')
to_city = input('到达城市:')
date = input('日期:')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/69.0.3497.100 Safari/537.36",
    "Content-Type": "application/json",  # 声明文本类型为 json 格式,
    'Cookie': '__DAYU_PP=fbffA7JMjfFQYEJvq3yV285fa84ef3bb; _abtest_userid=14f10ca5-5fe5-4b90-8994-a9a2a8289725; _ga=GA1.2.1823657567.1547218198; _RSG=jB4_phNRhw9fNvhoLy8_29; _RDG=28f1ebd8af073928c800c3c3726b485bce; _RGUID=9eab6d7a-f3fc-42ed-90bf-23c572af95e9; _geoinfo=CN%26%e6%b7%b1%e5%9c%b3; _bfa=1.1547218195619.296wjo.1.1547625090247.1554179025352.5.60; _bfs=1.1; Hm_lvt_cdce8cda34e84469b1c8015204129522=1554179026; Hm_lpvt_cdce8cda34e84469b1c8015204129522=1554179026; gad_city=31f35a60e938dff697ddea628b5bea7c; _RF1=14.153.237.134; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _gid=GA1.2.1875696831.1554179028; _gat=1; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1554179028552%7D%5D; _jzqco=%7C%7C%7C%7C1547625095764%7C1.1997966906.1547218199380.1547636825575.1554179028593.1547636825575.1554179028593.0.0.0.59.59; __zpspc=9.5.1554179028.1554179028.1%232%7Csp0.baidu.com%7C%7C%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; MKT_Pagesource=PC; Union=OUID=i&AllianceID=4897&SID=155952&SourceID=&Expires=1554783828996; MKT_OrderClick=ASID=4897155952&CT=1554179029004&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D155952%26allianceid%3D4897%26ouid%3Dindex&VAL={"pc_vid":"1547218195619.296wjo"}; _bfi=p1%3D100101991%26p2%3D100101991%26v1%3D60%26v2%3D59'
}
request_payload = {"flightWay": "Oneway",
                       "army": "false",
                       "classType": "ALL",
                       "hasChild": 'false',
                       "hasBaby": 'false',
                       "searchIndex": 1,
                       "portingToken": "3fec6a5a249a44faba1f245e61e2af88",
                       "airportParams": [
                           {"dcity": Address.city.get(from_city), "acity": Address.city.get(to_city), "dcityname": from_city, "acityname": to_city,
                            "date": date}]}

response = requests.post('https://flights.ctrip.com/international/search/api/lowprice/calendar/getCalendarDetailList?v=0.43030378904044686',
                         data=json.dumps(request_payload))
print(response.content)