#!/user/bin/python3
# -*-coding:utf-8 -*-

import re

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import imgdl

file_handle = open('1.txt', mode='a', encoding='utf-8')

data = []
titles = []
title = []
driver = webdriver.Chrome(ChromeDriverManager().install())
urllist = [
    "https://www.suruga-ya.jp/search?category=&search_word=%E5%A4%8F%E5%92%B2%E8%A9%A0&searchbox=1&is_marketplace=0",
    "https://www.suruga-ya.jp/search?category=&search_word=%E7%8B%97%E7%A5%9E%E7%85%8C&is_marketplace=0"]
for parenturl in urllist:
    driver.get(parenturl)
    html = driver.page_source
    for m in range(2, 10000):
        html = driver.page_source
        urls = re.findall(re.compile(r'<p class="title"><a href=".*\s*(?=</a></p>)'), html)
        if len(urls) == 0:
            break
        for i in urls:
            print(i)
            imgurl = i.split("\">")[1].split("=\"")[1]
            title = i.split("\">")[2]
            imgdl.getImg(imgurl, title)
        driver.get(parenturl + "&page=" + str(m))

file_handle.close()
