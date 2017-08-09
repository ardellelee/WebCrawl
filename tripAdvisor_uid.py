# to scrap on http://www.tripadvisor.com.sg/memberOverlay?uid=xxxxxx

import requests
from bs4 import BeautifulSoup
import json


Travelstyle = []
MemberProfile = []


def scrap_member_info(uid):
    url = 'http://www.tripadvisor.com.sg/memberOverlay'
    html = requests.get(url, params={'uid': uid})
    overlay = BeautifulSoup(html.content, 'html.parser')

    ## scraping information
    #mem_url = overlay.find('a')['href']
    username = overlay.find('h3').text
    badge = overlay.find('div', {'class': 'badgeinfo'}).text.strip()
    infoLis = overlay.findAll('li')

    duration = ' '
    location = ' '
    contributions = ' '
    cities = ' '
    helpful = ' '
    photos = ' '

    for info in infoLis:
        if 'member since' in info.text:
            duration = info.text.strip('\n')
            print duration

        elif ('from' in info.text) or ('From' in info.text):
            location = info.text.strip('\n')
            print location

        elif 'Contributions' in info.text:
            contributions = info.text.strip('\n')
            print contributions

        elif 'Cities' in info.text:
            cities = info.text.strip('\n')
            print cities

        elif 'Helpful' in info.text:
            helpful = info.text.strip('\n')
            print helpful

        elif 'Photos' in info.text:
            photos = info.text.strip('\n')
            print photos
        else:
            Travelstyle.append(info.text)

    MemberDic = {'uid':uid, 'duration': duration, 'location': location, 'contributions': contributions, 'cities':cities, 'helpful':helpful, 'photos':photos}
    MemberProfile.append(MemberDic)
    print 'uid=', uid
    print MemberProfile



def main():
    scrap_member_info('6B3B28FB8E38427AC0D68838379FA9F4')



if __name__ == '__main__':
    main()