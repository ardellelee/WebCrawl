# to scrap on http://www.tripadvisor.com.sg/members/xxxxx

#coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import json


def scrap_member_info(url):
    root_url = 'http://www.tripadvisor.com.sg'

    html = requests.get(url)
    overlay = BeautifulSoup(html.content, 'html.parser')
    mem_url = overlay.find('a')['href']
    profile_url = root_url + mem_url
    profile = BeautifulSoup(requests.get(profile_url).content, 'html.parser')


    ## profile info
    username = profile.find('div', {'class':'name'}).text

    try:
        ageSince = profile.find('div',{'class':'ageSince'}).text
        since = profile.find('p', {'class': 'since'}).text
        age = ageSince.replace(since, '').strip()
        since = since.replace('Since', '1')
    except:
        age = ''
        since = ''

    try:
        hometown = profile.find('div',{'class':'hometown'}).text
    except:
        hometown = ''

    try:
        desc = profile.find('div', {'class':'aboutMeDesc padded'}).text
    except:
        desc = ''

    print 'username=', username
    print 'age=',age
    print 'since=',since
    print 'hometown=',hometown
    print 'desc=', desc


    ## contribution info
    try:
        reviews = re.sub('\D', '', profile.find('a', {'name': 'reviews'}).text)
    except:
        reviews = ''

    try:
        ratings = re.sub('\D', '', profile.find('a',{'name':'ratings'}).text)
    except:
        ratings = ''

    try:
        photos = re.sub('\D', '', profile.find('a',{'name':'photos'}).text)
    except:
        photos = ''

    try:
        votes = re.sub('\D','', profile.find('a', {'name': 'lists'}).text)
    except:
        votes = ''

    try:
        points = re.sub('\D','', profile.find('div',{'class':'points'}).text)
    except:
        points = ''

    try:
        level = re.sub(r'\D','',profile.find('div', {'class':'level tripcollectiveinfo'}).text)
    except:
        level = ''

    print 'reviews=', reviews
    print 'ratings=', ratings
    print 'photos=', photos
    print 'votes=', votes
    print 'points=', points
    print 'level=', level


    ## travelstyle
    travelStyle = []
    try:
        tags = profile.findAll('div', {'class':'tagBubble unclickable'})
        for tag in tags:
            travelStyle.append(tag.text)
    except:
        print 'No tags on travel style!\n'

    print 'travelStyle=', travelStyle


    ## badge collection info
    badgeList = []
    #totalBadges = profile.find('a', {'class':'totalBadges'}).text
    totalBadges = re.sub(r'\D', '',profile.find('a', {'class':'totalBadges'}).text)
    badge_url = root_url + profile.find('a', {'class':'totalBadges'})['href']
    badgeSoup = BeautifulSoup(requests.get(badge_url).content, 'html.parser')
    badgeInfos = badgeSoup.findAll('li', {'class':'memberBadges'})

    for li in badgeInfos:
        badge = li.find('div', {'class':'badgeText'}).text
        #print badge
        badgeList.append(badge)

    print 'totalBadges=', totalBadges
    print 'badgeList=', badgeList


    # todo: 1）去掉第一个元素all；2）其余元素拆成键值对，用字典存储
    # todo：在test.py里调通函数，更新此处的实现方式
    ## contributions details
    reviews_url = profile.find('li', {'data-filter':'REVIEWS_ALL'}).find('a')['href']
    reviews_soup = BeautifulSoup(requests.get(root_url+reviews_url).content, 'html.parser')
    reviewInfos = reviews_soup.find('div', {'class':'cs-filter-bar'}).findAll('li')
    reviewList = []
    for info in reviewInfos:
        reviewList.append(info.text)
    print 'reviewList=',reviewList


    ratings_url = profile.find('li', {'data-filter': 'RATINGS_ALL'}).find('a')['href']
    ratings_soup = BeautifulSoup(requests.get(root_url + ratings_url).content, 'html.parser')
    ratingInfos = ratings_soup.find('div', {'class': 'cs-filter-bar'}).findAll('li')
    ratingList = []
    for info in ratingInfos:
        ratingList.append(info.text)
    print 'ratingList=', ratingList


    photos_url = profile.find('li', {'data-filter': 'PHOTOS_ALL'}).find('a')['href']
    photos_soup = BeautifulSoup(requests.get(root_url + photos_url).content, 'html.parser')
    photoInfos = photos_soup.find('div', {'class': 'cs-filter-bar'}).findAll('li')
    photoList = []
    for info in photoInfos:
        photoList.append(info.text)
    print 'photoList=', photoList


def main():
    scrap_member_info('http://www.tripadvisor.com.sg/memberOverlay?uid=6B3B28FB8E38427AC0D68838379FA9F4')
    #scrap_member_info('http://www.tripadvisor.com.sg/memberOverlay?uid=5509C134228FA6803AE7CCBBD50FF211')


if __name__ == '__main__':
    main()