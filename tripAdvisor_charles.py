## based on demo code given by Charles on class. Slight modification on regex and print format.

import re
#import urllib2
import requests
from bs4 import BeautifulSoup

url = 'https://www.tripadvisor.com.sg/Hotel_Review-g311415-d887085-Reviews-Four_Seasons_Resort_Bora_Bora-Bora_Bora_Society_Islands.html'
#html = urllib2.urlopen(url).read()
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')

members = soup.findAll('div', {'class':'memberOverlayLink'})
members = members[::2]


for member in members:
    #print member['id']
    empty, uid, src = re.split('UID_|-SRC_', member['id'])
    username = member.find('div', class_='username').text.strip()
    print '\n***************', username, '=', uid
    # https://www.tripadvisor.com.sg/MemberOverlay?uid=9897162894717580C814E8180214A3E4
    html = requests.get('http://www.tripadvisor.com.sg/memberOverlay', params={'uid':uid})
    overlay = BeautifulSoup(html.content, 'html.parser')

    mem_url = overlay.find('a')['href']
    username = overlay.find('h3').text

    if overlay.find('div', {'class': 'badgeinfo'}):
        print overlay.find('div', {'class': 'badgeinfo'}).text

    Travelstyle = []

    for info in overlay.findAll('li'):
        #print info
        if 'member since' in info.text:
            print info.text.strip('\n')
        elif ('from' in info.text) or ('From' in info.text):
            print info.text.strip('\n')
        elif 'Contributions' in info.text:
            print info.text.strip('\n')
        elif 'Cities' in info.text:
            print info.text.strip('\n')
        elif 'Helpful' in info.text:
            print info.text.strip('\n')
        elif 'Photos' in info.text:
            print info.text.strip('\n')
        else:
            Travelstyle.append(info.text)