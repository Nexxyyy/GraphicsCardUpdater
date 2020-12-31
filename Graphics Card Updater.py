import bs4
import time
import requests
import datetime
from datetime import datetime
import re

# List out amazon URL's and for loop in main code will go though
urls = ['https://www.amazon.com/gp/offer-listing/B08N9VTCWG/ref=dp_olp_unknown_mbc',
        'https://www.amazon.com/gp/offer-listing/B08L8L71SM/ref=dp_olp_unknown_mbc']
def check_price_amazon(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

    def dictionary_pairing(dictionary):
        for keys, values in dictionary.items():
            if 'ASUS' in card_brand:
                print(f'In Stock: Amazon ASUS: {keys}: {values}')
            elif 'MSI' in card_brand:
                print(f'In Stock: Amazon MSI: {keys}: {values}')
            else:
                print(f'In Stock: Amazon EVGA: {keys}: {values}')

    def strip_price_func(price_list):
        stripped_price_list = []
        for price in prices:
            stripped_price = price.getText().strip()
            stripped_price_list.append(stripped_price)
        return stripped_price_list

    def get_sellers_amazon(seller_list):
        stripped_seller_list = []
        for seller in seller_list:
            stripped_seller = seller.getText().strip()
            if stripped_seller !='New':
                stripped_seller_list.append(stripped_seller)
            else:
                pass
        return stripped_seller_list

    result = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(result.text,'html.parser')
    prices = soup.select('.a-size-large.a-color-price.olpOfferPrice.a-text-bold')
    sellers = soup.select('.a-size-medium.a-text-bold')
    card_brand = soup.select('h1')[0].getText()

    stripped_price_list = strip_price_func(prices)
    get_sellers_amazon(sellers)
    result_sellers_amazon = get_sellers_amazon(sellers)
    amazon_dictionary = dict(zip(result_sellers_amazon, stripped_price_list))
    dictionary_pairing(amazon_dictionary)

def check_price_bestbuy_evga():
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    #make the website request
    result = requests.get("https://www.bestbuy.com/site/evga-geforce-rtx-3070-ftw3-ultra-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6439301.p?skuId=6439301",headers=headers)

    #form the html
    soup = bs4.BeautifulSoup(result.text,'html.parser')

    #grab span that contains price from html list
    span_string = str(soup.select('.sr-only')[2])

    price = re.search(r'\d\d\d', span_string).group()

    #grabs list element of Sold Out
    stock= soup.select('button')

    #checks to see if list element contains sold out
    stock_check = "Sold Out" in str(stock)

    #print out price
    #print('Newegg MSI: $' + price)

    #checks if string element is true
    if stock_check == True:
        print('Sold Out: BestBuy EVGA: $' + price)
    else:
        print('In Stock: BestBuy EVGA: $' + price)

def check_price_bestbuy_strix():
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    #make the website request
    result = requests.get("https://www.bestbuy.com/site/asus-rog-strix-rtx3070-8gb-gddr6-pci-express-4-0-graphics-card-black/6439127.p?skuId=6439127",headers=headers)

    #form the html
    soup = bs4.BeautifulSoup(result.text,'html.parser')

    #grab span that contains price from html list
    span_string = str(soup.select('.sr-only')[2])

    price = re.search(r'\d\d\d', span_string).group()

    #grabs list element of Sold Out
    stock= soup.select('button')

    #checks to see if list element contains sold out
    stock_check = "Sold Out" in str(stock)

    #print out price
    #print('Newegg MSI: $' + price)

    #checks if string element is true
    if stock_check == True:
        print('Sold Out: BestBuy Strix: $' + price)
    else:
        print('In Stock: BestBuy Strix: $' + price)


def check_price_newegg_msi():
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    #make the website request
    result = requests.get("https://www.newegg.com/msi-geforce-rtx-3070-rtx-3070-gaming-x-trio/p/N82E16814137603?Description=rtx%203070%20gaming%20trio&cm_re=rtx_3070%20gaming%20trio-_-14-137-603-_-Product",headers=headers)

    #form the html
    soup = bs4.BeautifulSoup(result.text,'html.parser')

    #grab price from html list
    price = soup.select('strong')[1].getText()

    #grabs list element of Sold Out
    stock= soup.select('#ProductBuy')

    #checks to see if list element contains sold out
    stock_check = "Sold Out" in str(stock)

    #print out price
    #print('Newegg MSI: $' + price)

    #checks if string element is true
    if stock_check == True:
        print('Sold Out: Newegg MSI: $' + price)
    else:
        print('In Stock: Newegg MSI: $' + price)

def check_price_newegg_evga():
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    #make the website request
    result = requests.get("https://www.newegg.com/evga-geforce-rtx-3070-08g-p5-3767-kr/p/N82E16814487532?Description=rtx%203070&cm_re=rtx_3070-_-14-487-532-_-Product",headers=headers)

    #form the html
    soup = bs4.BeautifulSoup(result.text,'html.parser')

    #grab price from html list
    price = soup.select('strong')[1].getText()

    #grabs list element of Sold Out
    stock= soup.select('#ProductBuy')

    #checks to see if list element contains sold out
    stock_check = "Sold Out" in str(stock)

    #print out price
    #print('Newegg EVGA: $' + price)

    #checks if string element is true
    if stock_check == True:
        print('Sold Out: Newegg EVGA: $' + price)
    else:
        print('In Stock: Newegg EVGA: $' + price)

def check_price_newegg_strix():
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    #make the website request
    result = requests.get("https://www.newegg.com/asus-geforce-rtx-3070-rog-strix-rtx3070-o8g-gaming/p/N82E16814126458?Description=asus%20rog%20strix%203070&cm_re=asus_rog%20strix%203070-_-14-126-458-_-Product&quicklink=true",headers=headers)

    #form the html
    soup = bs4.BeautifulSoup(result.text,'html.parser')

    #grab price from html list
    price = soup.select('strong')[1].getText()

    #grabs list element of Sold Out
    stock= soup.select('#ProductBuy')

    #checks to see if list element contains sold out
    stock_check = "Sold Out" in str(stock)

    #print out price
    #print('Newegg Strix: $' + price)

    #checks if string element is true
    if stock_check == True:
        print('Sold Out: Newegg Strix: $' + price)
    else:
        print('In Stock: Newegg Strix: $' + price)

while True:
    for link in urls:
        check_price_amazon(link)
    check_price_bestbuy_evga()
    check_price_bestbuy_strix()
    check_price_newegg_strix()
    check_price_newegg_evga()
    check_price_newegg_msi()
    print(datetime.now())
    time.sleep(1)