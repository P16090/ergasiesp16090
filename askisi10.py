import urllib2
import json
dt=raw_input("Hmnia:")
response = urllib2.urlopen("https://www.cryptocompare.com/api/Drawsdata/coinlist/drawDate/%s.json'%dt")
html = response.read()
draws=json.loads(html)["draw"]["draws"]
print html
k=0
t=0
templist=list[html(k,t)]
templist = [k,t]
sorted(templist, key=int)
print templist 
