import requests
from bs4 import BeautifulSoup
import csv
import time
def getCommentByPage(url):

    header={
        "User-Agent":'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
        "Cookie":'Cookie: bid=O_tHjF5w4d4; douban-fav-remind=1; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1617693754%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dk96Yvd6OYlxizLsZbGIIqk_9LrY0O_neUL3gV1egQ_LwZ3qGiN_M24U3dDeEqMxp%26wd%3D%26eqid%3De6e004a00010bff100000006606c0c34%22%5D; _pk_id.100001.8cb4=9c75cff5230ff6a1.1609596906.2.1617693834.1609596906.; __gads=ID=c64439ffddf82994-223280796fc500c0:T=1609596907:RT=1609596907:S=ALNI_MYrtI0FCEc1BNkkU7dInch6UzIT_w; __utma=30149280.1766607315.1609596909.1609596909.1617693756.2; __utmz=30149280.1617693756.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ll="118281"; _pk_ses.100001.8cb4=*; __utmb=30149280.3.10.1617693756; __utmc=30149280; __utmt=1; dbcl2="235772634:xvG8CAfORGw"; ck=WO0Y; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __yadk_uid=lXkl2lIsl94RFO58uHVKiq3SGOsERdui; __utmv=30149280.23577'','
    }
    response =requests.get(url,headers=header)
    if response.status_code==200:
        bs=BeautifulSoup(response.content,'html5lib')
        commentItemList=bs.find_all('li',attrs={'class':'comment-item'})
        for commentItem in commentItemList:
            commentInfo=commentItem.find('span',attrs={'class':'comment-info'})
            author=commentInfo.find('a').text
            rating = commentInfo.find('span', attrs={"class": "user-stars allstar50 rating"})
            if (rating != None):
                #print(author)
                star = rating.get('title')
                #print(star)
                commentText = commentItem.find("span", attrs={"class": "short"}).text
                #print(commentText)
                commentList.append([author,star,commentText])

def writeComment():
    with open('pinglun.csv','w',newline='',encoding='utf-8') as file:
        csvWriter=csv.writer(file)
        csvWriter.writerows(commentList)


#print(response.content.decode('utf-8'))


if __name__ == '__main__':
    commentList=[]
    for i in range (10):
        getCommentByPage("https://book.douban.com/subject/26674263/comments/?start={}&limit=20&status=P&sort=new_score".format(i*20))
    writeComment()
    time.sleep(2)