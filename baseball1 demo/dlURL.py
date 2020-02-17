#############################################|############################################
#                                                                                        #
#                                   Download URL Quickly                                 #
#                                                                                        #
#############################################|############################################





#   This defines a function that downloads the html for a given URL with the standard set   
#   of options for parsing. This function returns the parsed text.
#





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
