from bs4   import  BeautifulSoup
import  pandas  as pd
# 进度条的包
from tqdm import  tqdm  #进度条库
import  math
import time
import requests

# 1 设置的请求头
headers = {
    "host":'hrb.lianjia.com',
     "User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0',
    "Cookie":'lianjia_uuid=3ba97d34-084d-44f2-8b4e-f1da1a5e1dc7; _ga=GA1.2.393827655.1592459559; _smt_uid=5eeb0125.2c8e3895; _jzqx=1.1592982943.1604546090.3.jzqsr=sjz%2Elianjia%2Ecom|jzqct=/ershoufang/%7b%7d/pg%7b%7d/.jzqsr=tj%2Elianjia%2Ecom|jzqct=/ershoufang/beichen/; UM_distinctid=176750cdfa261d-0c51ad3201d8e3-c7d6957-166e30-176750cdfa3341; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1617722515,1617767697,1617981192,1618149951; _jzqc=1; _jzqy=1.1604214200.1618149953.3.jzqsr=baidu.jzqsr=baidu|jzqct=python%20%20%20%E7%8E%AB%E7%91%B0%E9%A5%BC%E5%9B%BE%E7%9A%84%E7%BB%98%E5%88%B6; _jzqckmp=1; _gid=GA1.2.140047370.1618149955; _qzjc=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172c5fc7afcdc9-0a5d9ee69eb2b1-4d045769-1500000-172c5fc7afda19%22%2C%22%24device_id%22%3A%22172c5fc7afcdc9-0a5d9ee69eb2b1-4d045769-1500000-172c5fc7afda19%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wyshenzhen%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; lianjia_ssid=d08ce39f-d153-4024-b747-71a0aad0334a; _jzqa=1.599749127707461200.1592459557.1618149953.1618186424.119; select_city=230100; CNZZDATA1255849634=1702326710-1618149966-https%253A%252F%252Fwww.lianjia.com%252F%7C1618187841; CNZZDATA1254525948=2109013328-1618148472-https%253A%252F%252Fwww.lianjia.com%252F%7C1618185970; CNZZDATA1255633284=1556575427-1618145235-https%253A%252F%252Fwww.lianjia.com%252F%7C1618184190; CNZZDATA1255604082=323530854-1618144583-https%253A%252F%252Fwww.lianjia.com%252F%7C1618185791; login_ucid=2000000163591021; lianjia_token=2.00157c96fa7527c87b04d1bfcb493effba; lianjia_token_secure=2.00157c96fa7527c87b04d1bfcb493effba; security_ticket=FfMSaF/whiq/plhPHOSrrzeSRHlq9wRUvPQNFA20BsSqhCdKB0TJinONpA/dPCn4+vo+309/TMjyWXvO5exj0BJJl2POtG81XgR7vjpFOSYpH5SjrwzGhvf2+64NdRxYfez85heHuBFOUunCiDYligOxNMUEjRsH2hRJN6Ken5k=; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1618189469; _qzja=1.1775258717.1618149967229.1618149967230.1618187842528.1618189337231.1618189471058.0.0.0.10.2; _qzjb=1.1618187842528.6.0.0.0; _qzjto=6.1.0; _jzqb=1.7.10.1618186424.1; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiNzllN2YxNzVhNWNmN2QxNDg4N2VkMmIxNzFmY2ZmNmFjN2IwNGYzOTYwMTRkNDQ4NGRiZGZjNGMwMDhjYmJiODdjNjAxMTliMTUxNjYyZWU4OGQyNmE5NzUxNDU1NTY2YWY3NjVkYmE2OTEzMzc1MzNlNDViNzdmNzdlYTExYWJkM2ZmNDU3OTY3OGJiMTRlMjNkZjIxM2M2OGY1ZjJkZTBhZWFkMDBmNmQ4ODIwYjUzZDNhMzdmNzYxYzJjODJiOWJiYmYxOGU5MjA5MDlmMjI5ZWQxOTA4YWJmMzg4ZjhhMjM1YmFjYWRmZjM5MGJmMWFmZTMxODQwYmQwZDg3OWM3YWQyOWM0ZDJhMjkxYmRjOWVlNDVkNGQ4YjlmMWU2ODJlODExMDA1MzA4NjRkMWI2NTUyNzQyYjJiYzE4MDBiZWM0YzFmNGU3ZjU0ODJiOTY5NjcyZGU2ZmUxZTgyZFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIwZDYzNTAwYVwifSIsInIiOiJodHRwczovL2hyYi5saWFuamlhLmNvbS9lcnNob3VmYW5nLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1'

}
# 请求链家的网址
baseUrl = "https://hrb.lianjia.com/ershoufang/"
#各个行政区域，每一页的地址
#region_url = "https://hrb.lianjia.com/ershoufang/%s/pd%d"
#得到响应
resp=requests.get(baseUrl,headers=headers)
print(resp.status_code)
#输出网页源码
#c

#解析网页
bs = BeautifulSoup(resp.content,"lxml")
# 得到哈尔滨房源区域的信息
div_hrb = bs.find("div",attrs={"data-role":"ershoufang"})

# 输出哈尔滨各个区域的元素标签
print(div_hrb)
# 需要获取所有区域的路径
a_list_hrb = div_hrb.find_all("a")
#定义一个用来装 区域集合的字典
area_dic = {}

# for a  in   a_list_hrb:
#     #  a.get('href').split("/") = ['', 'ershoufang', 'pingfang', '']
#     #  获取哈尔滨市各个区域的名称，是列表的倒数第二个
#     areaUrl = a.get('href').split("/")[-2]
#     #print(areaUrl)
#     area_dic[a.text] = areaUrl
#
# print(area_dic)

#遍历字典，单独访问每一个行政区域
try:
    #遍历字典
    for   key_,value_ in area_dic.items():
        # 获取每个行政区域的房源访问地址
        start_url = "https://hrb.lianjia.com/ershoufang/%s"%(value_)
        #输出每隔区域的房源地址
        #print(start_url)
        # 重新发送请求，访问每隔区域的每一页
        respChild = requests.get(start_url,headers=headers)
        #进一步解析，每个行政区域的网页源码
        bsChild = BeautifulSoup(respChild.content,"html5lib")
        #获取房源总条数
        house_num = bsChild.find("h2",attrs={"class":"total fl"}).find("span").text
        #输出房源数
        print("%s:共找到房源%d套"%(key_,int(house_num)))
        time.sleep(1)
        #页面限制，每个行政区域，100页共计3000条房源信息
        #算出每一个行政区域，可以爬取的页数
        total_page = int(math.ceil(min(3000,int(house_num))/30.0))
        if(total_page!=0):
            #爬取各个区域
            #https://hrb.lianjia.com/ershoufang/%s/pd%d"
            #tqdm(range(total_page) 进度条比例信息
            for i in tqdm(range(total_page),desc=key_):
               #输出每一页开始的url
               region_url = 'https://hrb.lianjia.com/ershoufang/%s/pd%d'%(value_,i+1)
               print('https://hrb.lianjia.com/ershoufang/%s/pd%d'%(value_,i+1))
               #发起每一个行政区域，每一页的请求
               respSun = requests.get( region_url,headers=headers)
               bsSun = BeautifulSoup(respSun.content,"html5lib")
               # 解析每一个行政区域，每一页的网页源码的内容
               #找到存放每个房源信息的div
               info_list = bsSun.find_all("div",attrs={"class":"info clear"})
               #输出房源信息列表
               #print(info_list)
               #开始遍历房源列表找到各个区域
               for  info in info_list:
                   infor_dic = {}
                   infor_dic['area'] = key_
                   infor_dic['title'] = info.find("div",attrs={"class":"title"}).find("a").text
                   #print(infor_dic['title'])
                   #获取小区名
                   infor_dic['community'] = info.find("div",attrs={"class":"positionInfo"}).find_all("a")[0].text
                   #print(infor_dic['community'])
                   #位置信息
                   infor_dic['address'] = info.find("div",attrs={"class":"positionInfo"}).find_all("a")[1].text
                   #房源的总价信息
                   infor_dic['total_price'] = info.find("div",attrs={"class":"totalPrice"}).find("span").text
                   #房源单价信息
                   infor_dic['unite_price'] = info.find("div",attrs={"class":"unitPrice"}).find("span").text.replace("单价","").replace("元/平米","")
                   print("单价信息",infor_dic['unite_price'] )



except:
 pass