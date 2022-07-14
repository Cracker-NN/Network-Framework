from urllib.request import urlopen
from urllib.error import URLError
import sys


def internet():
        try:
            urlopen("https://google.com", timeout=5)
            print("")
        except URLError:
            print("\033[1;31m[+] \033[0;37mInternet Connection Not Found")
            sys.exit(0)