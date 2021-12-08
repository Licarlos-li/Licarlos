from tqdm import  tqdm  #进度条库
import  math
import time
import requests
from bs4   import  BeautifulSoup


headers = {
    "host":'www.bilibili.com',
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    "Cookie": "fingerprint=e0b8eb6d2737f58f0c10ec9f0a183e0c; buvid_fp=DFDA90FD-6202-4181-B68A-58CF7C6F148C58502infoc; buvid_fp_plain=DFDA90FD-6202-4181-B68A-58CF7C6F148C58502infoc; _uuid=A0F5004D-1C81-3C39-E3A3-F27DF597112695269infoc; buvid3=DFDA90FD-6202-4181-B68A-58CF7C6F148C58502infoc; sid=jxm50bhe; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(JY))~~mYRJ0J'uY|YR)mllu; PVID=1; CURRENT_QUALITY=64; LIVE_BUVID=AUTO3916109643369775; bp_video_offset_299236881=513016444603450615; fingerprint=e0b8eb6d2737f58f0c10ec9f0a183e0c; buvid_fp=DFDA90FD-6202-4181-B68A-58CF7C6F148C58502infoc; buvid_fp_plain=DFDA90FD-6202-4181-B68A-58CF7C6F148C58502infoc; SESSDATA=2796be0c%2C1634048165%2Ce1993%2A41; bili_jct=623eb86176d7ba2fb2ee3c523320cebb; DedeUserID=299236881; DedeUserID__ckMd5=d140a75a40e56b0d"
}

baseUrl = "https://www.bilibili.com/v/popular/rank/all"


resp=requests.get(baseUrl,headers=headers)
print(resp.status_code)
# print(resp.content.decode("utf-8"))
bs = BeautifulSoup(resp.content,"lxml")


commentItemList= bs.find_all('a', attrs={'class': 'title'})
b_icon = bs.find_all('span', attrs={'class': 'data-box'})
area_dic = {}
area_dic1 = {}
for a  in   commentItemList:
    areaUrl = a.get('target').strip('"_blank"')
    area_dic[a.text] = areaUrl

for b  in   b_icon:
    areaUrl1 = b.get('text')
    area_dic1[b.text] = areaUrl1

print(area_dic)
area_dic2='\n'.join(area_dic1).split()
print(area_dic)
print(area_dic2)
print(type(area_dic))
print(type(area_dic2))





