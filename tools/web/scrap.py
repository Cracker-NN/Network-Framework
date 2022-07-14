import requests
from bs4 import BeautifulSoup
import re
import simplejson


class Scrap:
    def url(self, urls):
        r = requests.get(str(urls))
        soup = BeautifulSoup(r.text, "html.parser")
        for items in soup.find_all("a", attrs={"href": re.compile(r"^https://")}):
            print("\033[1;31m[+]\033[0;37m Url Found => \033[0;32m{}\033[0m".format(items.get("href")))
    
    def data_scrap(self, urls):
        requestsing = requests.get(str(urls))
        print("\033[1;31mWebsite Url Found --> \033[0m\033[96m", requestsing.url)
        print("\033[1;34mResponse Code --> \033[0m", requestsing.status_code)
        print("\033[1;33mWebsite Encoding Found --> \033[0m",
            requestsing.apparent_encoding)
        try:
            print("\033[1;35mjsons Found ---> \033[0mFound")
        except Exception and simplejson.JSONDecodeError:
            print("\033[1;35mjsons ---> \033[0mNot Found !!")

        print("\033[1;34mCookies Found --> \033[0m", requestsing.cookies)
        print("\033[1;34mWebsite Reason Found --> \033[0m", requestsing.reason)
        if requestsing.links == {}:
            print("\033[1;34mLinks is : \033[0m" + "None")
        else:
            print("\033[1;34mLinks is : \033[0m", requestsing.links)
        if requestsing.is_redirect == False:
            print("\033[1;34mRedirecting : \033[0m" + "False")
        else:
            print("\033[1;34mRedirecting : \033[0m" + "True")
        if requestsing.is_permanent_redirect == False:
            print("\033[1;34mPermanent Redirecting : \033[0m" + "False")
        else:
            print("\033[1;34mPermanent Redirecting : \033[0m" + "True")
        print("\033[1;36mWebsite Header is : \033[0m\033[92m", requestsing.headers)
        print("\033[0m")
        
    def capture_tag(self, urls, tag):
        r = requests.get(str(urls))
        soup = BeautifulSoup(r.text, "html.parser")
        for items in soup.find_all(str(tag)):
            print("\033[1;31m[+] \033[0;37mCapturing Tag => \033[0;32m{}\033[0m".format(items))
