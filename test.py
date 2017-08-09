# to scrap on http://www.tripadvisor.com.sg/members/xxxxx

#coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import json


root_url = 'http://www.tripadvisor.com.sg'

# todo: to find out why this function doesn't work for photos
def scrap_contributes(url):
    soup = BeautifulSoup(requests.get(root_url+url).content, 'html.parser')
    Infos = soup.find('div', {'class': 'cs-filter-bar'}).findAll('li')
    list = []
    dict = []
    for info in Infos:
        list.append(info.text)
    for i in range(1,len(list)):
        key = re.sub(r'[^A-Za-z]','', list[i])
        value = re.sub(r'\D','',list[i])
        dict.append({key:value})
    print dict


def scrap_member_info(url):
    overlay = BeautifulSoup(requests.get(url).content, 'html.parser')
    profile_url = root_url + overlay.find('a')['href']
    profile = BeautifulSoup(requests.get(profile_url).content, 'html.parser')

    ## scrap contributions info
    reviews_url = profile.find('li', {'data-filter':'REVIEWS_ALL'}).find('a')['href']
    ratings_url = profile.find('li', {'data-filter': 'RATINGS_ALL'}).find('a')['href']
    photos_url = profile.find('li', {'data-filter': 'PHOTOS_ALL'}).find('a')['href']

    print reviews_url
    print ratings_url
    print photos_url
    #print root_url+photos_url


    scrap_contributes(reviews_url)
    scrap_contributes(ratings_url)
    #scrap_member_info(photos_url)



def main():
    scrap_member_info('http://www.tripadvisor.com.sg/memberOverlay?uid=6B3B28FB8E38427AC0D68838379FA9F4')
    #scrap_member_info('http://www.tripadvisor.com.sg/memberOverlay?uid=5509C134228FA6803AE7CCBBD50FF211')


if __name__ == '__main__':
    main()