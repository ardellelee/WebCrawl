############################################
# ISS Staff Info Crawler
# Workshop of Module KE5106, Lecture6
# Author: Li Yue
# Matric No.: A0163373E
############################################
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib2 import urlopen
#import re


def scraping(url, result):
    html = urlopen(url)
    soup = BeautifulSoup(html,'html.parser')
    infoDivs = soup.findAll('div',{'class':'col-sm-7'})

    f = open(result, 'a')
    for infoDiv in infoDivs:
        try:
            name = infoDiv.find('h2').text.strip()
            title = infoDiv.find('h3').text.replace(',', ' OF')
            email = infoDiv.find('my-email')['data-user']+'@'+ infoDiv.find('my-email')['data-domain']
            ## debug info
            print 'Name:', name
            print 'Title:', title
            print 'Email:', email, '\n'
            ## write to csv
            f.write(name + ',' + title + ',' + email + '\n')
        except:
            print 'Failed to write!'
    f.close()


def main():
    ## webpage index
    index = ['https://www.iss.nus.edu.sg/about-us/iss-team/management']
    index.append('https://www.iss.nus.edu.sg/about-us/iss-team/centres-of-excellence')
    index.append('https://www.iss.nus.edu.sg/about-us/iss-team/practice-chiefs')
    index.append('https://www.iss.nus.edu.sg/about-us/iss-team/graduate-programme-chiefs')
    index.append('https://www.iss.nus.edu.sg/about-us/iss-team/teaching-staff')
    index.append('https://www.iss.nus.edu.sg/about-us/iss-team/teaching-staff/2')
    index.append('https://www.iss.nus.edu.sg/about-us/iss-team/teaching-staff/3')
    index.append('https://www.iss.nus.edu.sg/about-us/iss-team/administration-staff')
    index.append('https://www.iss.nus.edu.sg/about-us/iss-team/administration-staff/2')
    index.append('https://www.iss.nus.edu.sg/about-us/iss-team/administration-staff/3')
    index.append('https://www.iss.nus.edu.sg/about-us/iss-team/adjunct-staff')
    index.append('https://www.iss.nus.edu.sg/about-us/iss-team/adjunct-staff/2')

    ## result file
    result = 'ISS_Staff_Info.csv'
    f = open(result, 'w')
    header = 'Name,Title,E-mail\n'
    f.write(header)
    f.close()

    ## scrapping
    for i in range(len(index)):
        print '\n@@@@@@@@@@@@@@@@@@@@@@@@@ Loop:', i, '@@@@@@@@@@@@@@@@@@@@@@@@@@'
        scraping(index[i], result)


if __name__ == '__main__':
    main()
