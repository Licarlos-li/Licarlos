import csv
#导入词云的包
from wordcloud import  WordCloud
#导入结巴分词
import jieba
#导入图像
from PIL import Image
# numpy数据分析的包，可以进行矩阵运算
import numpy as np

#将评论信息读取出来
def BookCommentRead():
    with open("司藤评论.csv","r",encoding="utf-8") as file:
        #将文件构建读取器
        csvReader = csv.reader(file)
        # 只返回列表中的评论内容
        #如下写法 是列表中的过滤
        return [ item[-1] for  item in csvReader  ]


#生成词云图的方法

def  generateWordCloud():
    listInfo = BookCommentRead()
    # 定义一个字符变量，进行拼接
    finalComments = ""
    #将所有的评论信息拼接一起
    for comment in listInfo:
        finalComments += comment
    #输出切完之后的字符串
    cutComments = " ".join(jieba.cut( finalComments))
    print(cutComments)
    #引入图片
    #Image.open 把图像引入到内存当中
    image  = np.array(Image.open("111.jpg"))
    #print(image)
    #通过词云类，生成词云图片
    wordCloud = WordCloud(
        font_path="STCAIYUN.TTF",#字体图标
        background_color="white",#词云背景
        mask=image #词云生成的图像模板

    ).generate(cutComments)

    wordCloud.to_file("词云4.jpg")






if __name__ == '__main__':

   generateWordCloud()
