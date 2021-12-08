
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties





def read_data():
    url = 'http://www.tianqihoubao.com/aqi/guangzhou-202003.html'
    df = pd.read_html(url, encoding='gbk', header=0)[0]
    return df


def get_url(city, year, month):
    """拼接url"""
    base_url = 'http://www.tianqihoubao.com/aqi/{}-{}{}.html'
    url = base_url.format(city, year, month)
    return url


def get_data(url):


    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    # 找到表格整理并读取
    table = soup.find('table')
    df = pd.read_html(table.prettify(), header=0)[0]
    return df


def save_df(dfs, filename):
    """储存csv文件"""
    for df in dfs:
        df.to_csv(filename, mode='a', header=None)


def spider_main():
    """主函数"""
    city = input('你想要查询的城市')
    year = input('你想要查询的年份')

    filename = city + year
    for month in range(1, 13):
        print('正在爬取第%d月的数据...' % month)
        dfs = []
        # 处理月份
        month = str(month)
        if len(month) == 1:
            month = '0' + month
    font = set_font()
    url = get_url(city, year, month)
    df = get_data(url)
    dfs.append(df)
    save_df(dfs, (filename + '.csv'))
    print('爬取完成,保存成功')


def set_font():
    # 设置中文
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 处理负号无法正常显示
    plt.rcParams['axes.unicode_minus'] = False
    # 设置字体
    font = FontProperties(fname=r'C:\Windows\Fonts\STKAITI.TTF', size=20)
    return font


def read_data():
    """pandas直接读取表格 该方法适用于没有反爬"""


    url = 'http://www.tianqihoubao.com/aqi/guangzhou-202003.html'
    df = pd.read_html(url, encoding='gbk', header=0)[0]
    return df


def get_url(city, year, month):
    base_url = 'http://www.tianqihoubao.com/aqi/{}-{}{}.html'
    url = base_url.format(city, year, month)
    return url


def get_data(url):
    """通用爬虫方法"""


    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    # 找到表格整理并读取
    table = soup.find('table')
    df = pd.read_html(table.prettify(), header=0)[0]
    return df


def save_df(dfs, filename):
    """储存csv文件"""


    for df in dfs:
        df.to_csv(filename, mode='a', header=None)


def spider_main():
    """主函数"""


city = input('你想要查询的城市')
year = input('你想要查询的年份')

filename = city + year
for month in range(1, 13):
    print('正在爬取第%d月的数据...' % month)
    dfs = []
    # 处理月份
    month = str(month)
    if len(month) == 1:
        month = '0' + month

    font = set_font()
    url = get_url(city, year, month)
    df = get_data(url)
    dfs.append(df)
    save_df(dfs, (filename + '.csv'))
print('爬取完成,保存成功')
