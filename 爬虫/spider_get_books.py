'''
爬虫，爬取书籍信息 
网站：http://books.toscrape.com/
输出：xlsx文件(包含书籍名称、价格、链接、封面链接)
'''

import requests as rq
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import pandas as pd

# 1.获取网页内容
url = 'http://books.toscrape.com/'
response = rq.get(url)
response.encoding = 'utf-8'
html=response.text

#2.解析网页内容
soup=bs(html,'lxml')

#3.定位到书籍位置
div_books=soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
# print(div_books)
#4.分别获取书籍的信息
books=[]
if div_books:
    for book in div_books:
        #书籍图片
        book_img_url=book.find("img").get("src")
        full_img_url = urljoin(url, book_img_url).replace("../../", "")
        #    print(full_img_url)
        #书籍链接
        book_href=book.find("a").get('href')
        full_url=urljoin(url, book_href)
        #    print(full_url)
        #书籍名称
        book_name=book.find("h3").text.strip()
        #    print(book_name)
            #书籍价格
        book_price=book.find("p", class_="price_color").text
        #    print(book_price)
        #整合书籍数据
        books.append({
            "书籍封面":full_img_url,
            "书籍名称":book_name,
            "书籍链接":full_url,
            "书籍价格":book_price
        })
else:
    print("没有找到书籍")
    
#5.把书籍信息保存到excel文件中
# 转换数据为DataFrame
df = pd.DataFrame(books)[["书籍名称", "书籍价格", "书籍链接", "书籍封面"]]
try:
    # 确保已安装openpyxl: pip install openpyxl
    df.to_excel("书籍列表.xlsx", 
                index=False, 
                engine="openpyxl")  
    
    print(f"成功保存 {len(df)} 条数据到 书籍列表.xlsx")
except Exception as e:
    print(f"Excel保存失败: {str(e)}")
    # 降级保存为CSV（当个保险）
    df.to_csv("书籍列表_备份.csv", 
             index=False, 
             encoding="utf-8-sig")  

