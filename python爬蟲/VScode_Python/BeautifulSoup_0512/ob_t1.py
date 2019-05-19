# -*- coding: utf-8 -*-
import requests #產生HTTP的請求
from bs4 import BeautifulSoup
import time
from flask import Flask, request, abort
from selenium import webdriver
def Taoyuan(url,city):
    target_url = url
    driver = webdriver.PhantomJS(executable_path=r'.\phantomjs-2.1.1-windows\bin\phantomjs.exe')#導入PhantomJS路徑
    driver.get(target_url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    content = ""
    for data in soup.select('#ftext'):
        title = str(data)
        content = title.split("<br/><br/>")[2]
    print(city+"：\n"+content)
    return content

def my_weather(url):
    r=requests.get(url)
    r.encoding='utf8'
    soup = BeautifulSoup(r.text,"html.parser")
    sel = soup.select('table.FcstBoxTable01 td')#抓地址
    sel1 = soup.select('table.FcstBoxTable01 th')#抓溫度
    dic = []
    dic1 = []
   
    for i in sel:
        dic.append(i.text)
    for j in sel1:
        dic1.append(j.text)
#    print("其他資訊為：",dic1[0:4])
#    print("氣溫為：",dic[0])
    print(dic1[0]+"：\n")#氣溫為： "+dic[0])
           
mydict={}
def add(url):
    r=requests.get(url)
    r.encoding='utf8'
    soup = BeautifulSoup(r.text,"html.parser")
    set_ad = soup.select('div.CenterMenu select')#抓各縣市網址
    dic_ad = str(set_ad).strip("[]")
    dic_ad = dic_ad.strip('<select name="menu1" onchange="MM_jumpMenu(\'self\',this,0)">')
    dic_ad = dic_ad.split(" <option value=\"")
    dic_ad_1 = dic_ad[0].split("<option selected=\"selected\" value=\"")
    dic_ad[0]=dic_ad_1[0].strip("value=\"")
    dic_ad.append(dic_ad_1[1])
    
    for i in dic_ad:
        data = i.split("\">")
        data[1]=data[1].split("<")
#        print(data[0] ,"\n",data[1][0],"\n")
        mydict[data[1][0]]=data[0]
    print(mydict)
'''    
add('https://www.cwb.gov.tw/V7/forecast/taiwan/New_Taipei_City.htm')
#新北市

my_weather('https://www.cwb.gov.tw/V7/forecast/taiwan/'+mydict['新北市'])
Taoyuan('https://www.cwb.gov.tw/V7/forecast/taiwan/'+mydict['新北市'])
#台北市
my_weather('https://www.cwb.gov.tw/V7/forecast/taiwan/'+mydict['臺北市'])
Taoyuan('https://www.cwb.gov.tw/V7/forecast/taiwan/'+mydict['臺北市'])
#桃園市
my_weather('https://www.cwb.gov.tw/V7/forecast/taiwan/'+mydict['桃園市'])
Taoyuan('https://www.cwb.gov.tw/V7/forecast/taiwan/'+mydict['桃園市'])
'''
if __name__ == "__main__":
    add('https://www.cwb.gov.tw/V7/forecast/taiwan/New_Taipei_City.htm')
    city=input("請輸入你所在的城市：")
    Taoyuan('https://www.cwb.gov.tw/V7/forecast/taiwan/'+mydict[city],city)
"""
{
'臺北市': 'Taipei_City.htm', 
'桃園市': 'Taoyuan_City.htm', 
'臺中市': 'Taichung_City.htm', 
'臺南市': 'Tainan_City.htm', 
'高雄市': 'Kaohsiung_City.htm', 
'基隆市': 'Keelung_City.htm', 
'新竹市': 'Hsinchu_City.htm', 
'新竹縣': 'Hsinchu_County.htm', 
'苗栗縣': 'Miaoli_County.htm', 
'彰化縣': 'Changhua_County.htm', 
'南投縣': 'Nantou_County.htm', 
'雲林縣': 'Yunlin_County.htm', 
'嘉義市': 'Chiayi_City.htm', 
'嘉義縣': 'Chiayi_County.htm', 
'屏東縣': 'Pingtung_County.htm', 
'宜蘭縣': 'Yilan_County.htm', 
'花蓮縣': 'Hualien_County.htm', 
'臺東縣': 'Taitung_County.htm', 
'澎湖縣': 'Penghu_County.htm', 
'金門縣': 'Kinmen_County.htm', 
'連江縣': 'Lienchiang_County.htm', 
'新北市': 'New_Taipei_City.htm'
}
"""