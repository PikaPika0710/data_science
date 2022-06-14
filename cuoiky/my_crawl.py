from functools import partial
from queue import PriorityQueue
import requests
from bs4 import BeautifulSoup
import numpy as np
from sqlalchemy import null
import pandas as pd
import re

# get links

base_link = 'https://www.zanado.com'
links = ['https://www.zanado.com/ao-khoac-nam-51.html', ## 141 sản phẩm
         'https://www.zanado.com/ao-so-mi-nam-49.html',
         'https://www.zanado.com/ao-thun-nam-50.html', 
         'https://www.zanado.com/quan-tay-nam-39.html',
         'https://www.zanado.com/quan-jean-nam-247.html',
         'https://www.zanado.com/quan-kieu-nam-248.html',
         'https://www.zanado.com/bop-vi-nam-35.html',
         'https://www.zanado.com/tui-xach-tui-deo-nam-164.html',
         'https://www.zanado.com/ba-lo-nam-165.html',
         'https://www.zanado.com/mu-non-nam-42.html',
         'https://www.zanado.com/mat-kinh-nam-43.html',
         'https://www.zanado.com/tat-vo-nam-46.html',
         'https://www.zanado.com/phu-kien-nam-khac-90.html',
        ] 

categories_str = ['Áo khoác', 'Áo sơ mi', 'Áo thun', 'Quần tây',
                  'Quần jean', 'Quần kiểu', 'Bóp ví', 'Túi xách, đeo',
                  'Ba lô', 'Mũ nón', 'Mắt kính', 'Tất vớ', 'Phụ kiện khác'
                 ]

# so luong page trong link can lay
pages = [5, 5, 5, 2, 4, 2, 5, 5, 5, 5, 3, 1, 4]

product_names = []
product_ids = []
sale_offs = []
origin_prices = []
sales_prices = []
list_detail_links = []
purchases = []
ratings = []
num_raters = []
category_ids = []

def handle_duplicated_value(df):
    new_data = dict()
    new_df = df.copy()
    count = 0

    name_products_list = df['product_names']
    for i in range(1, len(name_products_list)):
        if not name_products_list[i] in new_data:
            new_data[name_products_list[i]] = df[i:i + 1]
            new_df[count:count+1] = df[i:i + 1]
            count += 1

    return new_df[1:len(new_data)]


# access to detail link product
def access_detail_link(detail_link):
    draw_r1 = requests.get(detail_link)
    coverpage_drawn = draw_r1.content
    soap_drawn = BeautifulSoup(coverpage_drawn, 'html5lib')
    return soap_drawn

def crawl_data_from_link(link, category_id):
    draw_r1 = requests.get(link)
    coverpage_drawn = draw_r1.content
    soap_drawn = BeautifulSoup(coverpage_drawn, 'html5lib')


    # get name product 
    list_product_names = soap_drawn.find_all('h2', {'class': 'product-name'})
    for name in list_product_names:
        product_name = name.get_text()
        product_names.append(product_name)
        category_ids.append(category_id)

    # get % sales off
    list_sales_off = soap_drawn.find_all('div', {'class': 'discountpercent'})
    for sale in list_sales_off:
        if sale.get_text() == "0%":
            sale_offs.append(None)
        else:
            sale_offs.append(sale.get_text())

    # get orign price and sales price 
    list_prices = soap_drawn.find_all('div', {'class': 'infoprice'})
    for price in list_prices:
        origin_price = price.find('span', {'class': 'priceold'}).get_text()[:-2]
        sales_price = price.find('span', {'class': 'pricespecial'}).get_text()[:-2]
        origin_price = origin_price.replace(".","")
        sales_price = sales_price.replace(".","")
        if origin_price == sales_price:
            sales_prices.append(None)
        else:
            sales_prices.append(sales_price)
        origin_prices.append(origin_price)

    # get detail information: nuber of raters, rating, purchase,
    detail_links = soap_drawn.find_all('a', {'class': 'product-content'}, href=True)
    for link in detail_links:
        detail_link = base_link + link['href']
        list_detail_links.append(detail_link)
        detail_soap_drawn = access_detail_link(detail_link)

        # get number of num_rater
        num_rater = detail_soap_drawn.find('div', {'class': 'count'})
        num_raters.append(num_rater.find('span').get_text())

        # get rating
        rating = detail_soap_drawn.find('div', {'class': 'rating'}, style=True)
        ratings.append(rating['style'][6:-2])
        
        # get purchases
        purchase = detail_soap_drawn.find('div', {'class': 'sprites soluongmua'})
        purchases.append(purchase.find('span').get_text())
    

for i in range(0, len(links)):
    category_id = i
    page_num = pages[i]
    if page_num == 1:
        link = links[i]
        print(link)
        crawl_data_from_link(link, category_id)
    else:
        for j in range(1, pages[i] + 1):
            link = links[i] + '?p=' + str(j)
            print(link)
            crawl_data_from_link(link, category_id)

product_ids = [i for i in range(0, len(product_names))]



arr = []
for i in range(0, len(category_ids)):
    arr.append(categories_str[category_ids[i]])


# add data to csv file
dictionary = {'product_id': product_ids,
              'product_names': product_names, 
              'sale_offs': sale_offs,
              'sales_prices': sales_prices,
              'origin_prices': origin_prices,
              'purchases': purchases,
              'num_raters': num_raters,
              'ratings': ratings,
              'categories_str': arr,
              'category_id': category_ids}


df = pd.DataFrame(dictionary)
# df = handle_duplicated_value(df)
to_csv = df.to_csv('zanado.csv')
