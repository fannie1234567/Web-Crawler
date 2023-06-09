# -*- coding: utf-8 -*-
"""圖片多頁下載

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Lp3BX4RnpAH8nYygAxyzjcKCgopRdyD
"""

import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from urllib.parse import urljoin

# 設定 ChromeDriver 路徑
service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)

# 爬取10頁
for page in range(1, 6):
    # 前往網頁
    url = f'https://www.shein.tw/style/Shirt-Dresses-sc-00101007.html?ici=tw_tab01navbar05menu04dir11&src_module=topcat&src_tab_page_id=page_select_class1680812971196&src_identifier=fc%3DWomen%60sc%3D%E6%B4%8B%E8%A3%9D%60tc%3D%E6%8C%89%E8%B6%A8%E5%8B%A2%E9%81%B8%E8%B3%BC%60oc%3D%E8%A5%AF%E8%A1%AB%E8%A3%99%60ps%3Dtab01navbar05menu04dir11%60jc%3DitemPicking_00101007&srctype=category&userpath=category-'
    driver.get(url)
    driver.implicitly_wait(10)

    # 取得網頁原始碼
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 找到所有圖片的 URL
    img_urls = []
    for img in soup.find_all('img'):
        if 'data-src' in img.attrs:
            img_url = urljoin(url, img['data-src'].split('@')[0])
            img_urls.append(img_url)

    # 下載圖片
    for i, img_url in enumerate(img_urls):
        # 建立儲存圖片的路徑及檔名
        filename = f"page{page}_image_{i}.jpg"
        filepath = os.path.join("女士短襯衫裙圖檔", filename)

        # 如果目標路徑不存在就建立
        if not os.path.exists("女士短襯衫裙圖檔"):
            os.makedirs("女士短襯衫裙圖檔")

        # 下載圖片
        response = requests.get(img_url)
        with open(filepath, 'wb') as f:
            f.write(response.content)

driver.quit()
print("下載完成！")