import requests #產生HTTP的請求
from bs4 import BeautifulSoup 
#r=requests.get('https://www.cwb.gov.tw/V7/forecast/taiwan/New_Taipei_City.htm')
r=requests.get('https://www.cwb.gov.tw/V7/forecast/taiwan/New_Taipei_City.htm')
#r.encoding='big5'
#r.encoding='cp950'
r.encoding='utf8'
#print(r.text)
soup = BeautifulSoup(r.text,"html.parser")
#sel = soup.select('table.FcstBoxTable01 td')
#sel1 = soup.select('table.FcstBoxTable01 th')
#set_ad = soup.select('select.menu1 option')
set_ad = soup.select('div.CenterMenu select')
#dic = []
#dic1 = []
#dic_ad = []
#dic_ad1 = []
dic_ad = str(set_ad).strip("[]")
dic_ad = dic_ad.strip('<select name="menu1" onchange="MM_jumpMenu(\'self\',this,0)">')
dic_ad = dic_ad.split(" <option value=\"")
#dic_ad = dic_ad.split("value=\"")
#dic_ad = dic_ad.split("</option>")
#print(dic_ad)
dic_ad_1 = dic_ad[0].split("<option selected=\"selected\" value=\"")
dic_ad[0]=dic_ad_1[0].strip("value=\"")
dic_ad.append(dic_ad_1[1])
mydict={}
for i in dic_ad:
    data = i.split("\">")
    data[1]=data[1].split("<")
    print(data[0] ,"\n",data[1][0],"\n")
    mydict[data[1][0]]=data[0]
print(mydict)

#for i in set_ad:
#    dic_ad.append(i.text)
#    dic_ad1.append(i)
#    print(i)
#    print(i.get('value'))
#print(dic_ad[:])
#print(dic_ad1[:])
#print(type(dic_ad1))
#print('地區資訊：',dic_ad1[0:6])

#for i in sel:
#    dic.append(i.text)
#    #print(i.text)
#
#for j in sel1:
#    dic1.append(j.text)
#
#print("其他資訊為：",dic1[0:4])
#print("氣溫為：",dic[0])
