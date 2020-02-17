### Download URL Quickly

### Set up necessary package
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
#####

### Define function
def dlURL (url , parser = "html.parser" ) :
    urlClient = uReq(url)
    pageRough = urlClient.read()
    urlClient.close()
    pageSoup = soup(pageRough,parser)

    return pageSoup

#####
