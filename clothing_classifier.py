# -*- coding: utf-8 -*-
"""clothing_classifier

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Lp3BX4RnpAH8nYygAxyzjcKCgopRdyD
"""

# 前往網頁
url = 'https://www.shein.tw/Women-Sweatshirts-c-1773.html?ici=tw_tab01navbar04menu09&src_module=topcat&src_tab_page_id=page_real_class1681039386882&src_identifier=fc%3DWomen%60sc%3D%E8%A1%A3%E6%96%99%E9%A4%A8%60tc%3D%E9%81%8B%E5%8B%95%E8%A1%AB%60oc%3D0%60ps%3Dtab01navbar04menu09%60jc%3Dreal_1773&srctype=category&userpath=category-'
driver.get(url)
driver.implicitly_wait(10)

# 取得網頁原始碼
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 提取所有的商品連結
product_links = []
for div in soup.find_all('div', {'class':'S-product-item__wrapper'}):
    link = div.find('a', {'href': True})
    if link is not None:
        href = link.get('href')
        product_links.append(href)

# 進入每個商品頁面，提取商品名稱、屬性和圖片網址
for link in product_links:
    # 進入商品頁面
    full_url = urljoin(url, link)
    driver.get(full_url)
    driver.implicitly_wait(10)

    # 取得商品頁面原始碼
    html = driver.page_source
    product_soup = BeautifulSoup(html, 'html.parser')

    # 提取商品名稱
    product_name_elem = product_soup.find('h1', {'class':'product-intro__head-name'})
    if product_name_elem is not None:
        product_name = product_name_elem.text.strip()
    else:
        product_name = ''

    # 提取商品屬性
    attributes = []
    div_elements = product_soup.find_all('div', {'class': 'product-intro__attr-wrap'})
    for div in div_elements:
        text = div.text
        attributes.append(text)

    # 提取商品圖片網址
    product_pic_elem = product_soup.find('img', {'class': 'j-verlok-lazy'})
    if product_pic_elem is not None:
        product_pic = product_pic_elem.get('src')
        if product_pic:
            product_pic = 'https:' + product_pic
    else:
        product_pic = ''

    # 輸出商品資訊
    print('Product name:', product_name)
    print('Attributes:', attributes)
    print('Image URL:', product_pic)
    print('------------------------')

    # 將商品名稱和屬性合併為描述
    describe = product_name + ' ' + ' '.join(attributes)

    # 將描述和圖片連結分類並存檔
    classifier = clothing_classifier.Determine
    classifier(describe, product_pic).top()

# 關閉瀏覽器
driver.quit()