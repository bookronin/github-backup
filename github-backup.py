#!/usr/bin/python
from BeautifulSoup import BeautifulSoup
import datetime
import re
import urllib2
import sys

def main():
    username = sys.argv[1]

    if username == None or username == '':
        return

    addr = 'https://github.com/' + username + '?tab=repositories'
    
    pageContent = getWebPageContent(addr)
    
    soup = BeautifulSoup(''.join(pageContent))
     
    mainDiv = soup.find("div", {"class": "repo-tab"})
    
    nextPages = mainDiv.findAll('h3', {'class' : 'repolist-name'})
    
    for page in nextPages:
        href_search = re.search(r'href="([^"]+)"', str(page))
        nm = href_search.group(1)
        
        pg = 'https://github.com' + nm + '/archive/master.zip'
        
        cnt = getWebPageContent(pg)
        
        print pg
        
        filenm = nm.replace(username, '')
        filenm = filenm.replace('/', '')
        
        f = open(filenm + '.zip', 'w')
        f.write(cnt)
        f.flush()
        f.close()
        
def getWebPageContent(pageName):
    f = urllib2.urlopen(pageName)
    s = f.read()
    f.close()
    return s
    
if __name__ == '__main__': main()
    
