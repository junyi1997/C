import pandas
def getRef(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')
    dfs = pandas.read_html(res.text)
    votes = dfs[2] 
    votes.columns = votes.loc[1] 
    votes.drop([0,1,3,4], inplace = True)
    votes.reset_index(drop = True ,inplace = True)
    totalvotes = dfs[3] 
    totalvotes.columns = votes.loc[0] 
    totalvotes.drop([0,2,3], inplace = True) 
    totalvotes.reset_index(drop=True, inplace = True)
    m = pandas.concat([votes, totalvotes], axis = 1)
    area = soup.select_one('b').text
    m["投票地區"] = area
    return m
getRef('http://referendum.2018.nat.gov.tw/pc/zh_TW/01/63000000100000000.html')

domain = 'http://referendum.2018.nat.gov.tw/pc/zh_TW'
results = []
for ele in links[0:3]:
    try:
        results.append(getRef(ele.get(domain + ele.get('href').strip('.'))))
    except:
        print(domain + ele.get('href').strip('.'))

pandas.concat(results) #資料合併


"""
import requests
res = requests.get('http://referendum.2018.nat.gov.tw/pc/zh_TW/01/63000000100000000.html')
#res = requests.get('網址')
res.text

from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')

driver.get('http://referendum.2018.nat.gov.tw/pc/zh_TW/01/63000000100000000.html')

from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source,'lxml')
links = soup.select('dic[id^=item] a')

domain = 'http://referendum.2018.nat.gov.tw/pc/zh_TW'
for ele in links:
    print(ele.get(domain + ele.get('href').strip('.')))

import pandas
dfs = pandas.read_html('http://referendum.2018.nat.gov.tw/pc/zh_TW/01/63000000100000000.html')

#第一個爬蟲(爬資料)
votes = dfs[2] 
votes.columns = votes.loc[1] #1是指第一行為標題列,欄位名稱為第一列數據
votes.drop([0,1,3,4], inplace = True) #[]內指這些列我不要,把0,1,3,4拿掉
votes.reset_index(drop = True ,inplace = True) #drop以後直接生效就打 inplace = True
#索引重新編排
#votes #指把votes打開,查看內容

totalvotes = dfs[3] 
totalvotes.columns = votes.loc[0] #0是指第0行為標題列,欄位名為第0個欄位
totalvotes.drop([0,2,3], inplace = True) #[]內指這些列我不要
totalvotes.reset_index(drop=True, inplace = True)
totalvotes

#合併 索引編號要一樣
m = pandas.concat([votes, totalvotes], axis = 1)
#兩筆資料作合併,原為用行合併,加上axis = 1,會整合為一行,並列合併再一起

#第二個爬蟲(爬地區)
res = requests.get('http://referendum.2018.nat.gov.tw/pc/zh_TW/01/63000000100000000.html')
soup = BeautifulSoup(res.text,'lxml')
area = soup.select_one('b').text #地區是粗體字放在<b><|b>裡面,所以抓b
#select_one 是要抓第一個b ;.text取文字
m["投票地區"] = area
m


"""