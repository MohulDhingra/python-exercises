'''data={"a":1}
#data["b"]=1
data.update({"b":1})
#del data["b"]
x=data.pop("b")
print(data)'''

'''
from collections import defaultdict
x=defaultdict(lambda:"sky")
x[1]="room"
x[2]="sham"
print(dict(x))
'''

import requests
import json

city=input("ENTER CITY: ")
url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=686b8199a9752d622674874b11d11654"


#url="https://newsapi.org/v2/top-headlines?country=in&apiKey=5dd3a411f2d04a85b439a029266eb5ff"

text= requests.get(url).text
data = json.loads(text)


i=0
while i<len(data["weather"]):
                 print(data["weather"][i]["description"])
                 print(data["weather"][i]["main"])
                 print()
                 i=i+1
while i<len(data["main"]):
                 print(data["main"][i]["temp"])
                 print()
                 i=+1
'''
i=0

while i<len(data["articles"]):
    print(data["articles"][i]["title"])
    print()
    i=i+1
          
'''
