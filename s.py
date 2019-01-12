import json
from urllib.request import urlopen


url = "http://be.wizzair.com/9.3.0/Api/asset/map?languageCode=en-gb"
aliaslist=[]
stop=0
data = json.load(urlopen(url))
for k,v in data.items():
    stop=1
    print(k, 'corresponds to', v)
    print(type(v))
    for z in v:
        for key,value in z.items():
            print(key, 'corresponds to', value)
            if key == "aliases":
                aliaslist.append(value)
    if stop == 1:
        break
print(aliaslist)