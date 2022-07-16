import json
import requests
from bs4 import BeautifulSoup
import socket
import re
import geopy
import os


class Scan():
    def __init__(self, url:str, api:any) -> str:
        self.url = str(url)
        self.api = str(api)
    def dns_for_termux(self, url):
        r = requests.get("http://api.hackertarget.com/dnslookup/?q={}".format(str(url)))
        results = {}
        with open("tools/web/temp_web.txt", "w") as file:
            file.write(r.text)
        with open("tools/web/temp_web.txt", "r") as f_read:
            for l in f_read.readlines():
                term, description = l.strip().split(None, 1)
                results[term] = description.strip()
        with open("tools/web/temp_capture.json", "w") as jsonc:
            json.dump(results, jsonc, indent=4, sort_keys=False)
        with open("tools/web/temp_capture.json", "r") as final:
            data = json.load(final)
        
        AAAA = data['AAAA']
        MX = data['MX']
        NS = data['NS']
        TXT = data['TXT']
        SOA = data['SOA']
        
        print("\033[1;31m[+]\033[0;37mAAAA => {}".format(str(AAAA)))
        print("\033[1;31m[+]\033[0;37mMX => {}".format(str(MX)))
        print("\033[1;31m[+]\033[0;37mNS => {}".format(str(NS)))
        print("\033[1;31m[+]\033[0;37mTXT => {}".format(str(TXT)))
        print("\033[1;31m[+]\033[0;37mSOA => {}".format(str(SOA)))
    
    def domain_scanner(self, domain_name,sub_domnames):
        for subdomain in sub_domnames:
            url = f"https://{subdomain}.{domain_name}"
            try:
                requests.get(url)
                print('\t\033[1;37m|--------> \033[1;32m{}\033[0m'.format(url))
            except requests.ConnectionError:
                print("", end="")
                
                    
    def track(self, ip:any):
        geography = geopy.Nominatim(user_agent="geoapiExercises")
        r = requests.get(f"https://ipinfo.io/{ip}?token={self.api}")
        data = r.json()
        self.city = data['city']
        self.state = data['region']
        self.locationing = data['loc']
        self.timeZone = data['timezone']
        self.carrier = data['org']
        self.country_code = data['country']
        self.pin_code = data['postal']
        self.location2 = geography.geocode(self.locationing)

    def simplescan(self) -> None:
        # Global
        user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
        }
        r = requests.get(str(self.url))
        soup = BeautifulSoup(r.content, "html.parser")
        header = r.headers
        # http://api.hackertarget.com/dnslookup/?q=
        # Title
        title = soup.title.string
        print("\033[1;31m[+]\033[0;37mTitle Found => {}".format(title))
        # Server
        server = r.headers['Server']
        print("\033[1;31m[+]\033[0;37mSever Found => {}".format(server))
        # IP
        s = socket.gethostbyname(str(self.url).split("/")[2])
        print("\033[1;31m[+]\033[0;37mIP Found => {}\033[0m".format(s))
        # Checking Online or Offline
        
        if r.status_code == 200:
            print("\033[1;31m[+]\033[0;37mStatus => \033[1;32mOnLine\033[0m")
        else:
            print("\033[1;31m[+]\033[0;37mStatus => \033[1;31mOffline\033[0m")
        
        # Checking Encoding
        if "Transfer-Encoding" in header:
            print("\033[1;31m[+]\033[0;37mTransfer-Encoding Found => " ,header["Transfer-Encoding"])
        elif "Encoding" in header:
            print("\033[1;31m[+]\033[0;37mTransfer-Encoding Found => " ,header["Encoding"])
        elif "encoding" in header:
            print("\033[1;31m[+]\033[0;37mTransfer-Encoding Found => " ,header["encoding"])
        else:
            print("\033[1;31m[+]\033[0;37mTransfer-Encoding Not Found => ")
        
        # Connections
        try:
            print("\033[1;31m[+]\033[0;37mConnection Found => ", header["Connection"] )
        except KeyError:
                print("\033[1;31m[+]\033[0;37mConnection Not Found => ")
        # X - Values
        try:
            print("\033[1;31m[+]\033[0;37mX-rq Found => ", header["X-rq"] )
        except KeyError:
            print("\033[1;31m[+]\033[0;37mX-rq Not Found => ")
        
        try:
            print("\033[1;31m[+]\033[0;37mX-Content-Type-Options Found => ", header["X-Content-Type-Options"] )
        except:
            print("\033[1;31m[+]\033[0;37mX-Content-Type-Options Not Found => ")
        try:
            print("\033[1;31m[+]\033[0;37mX-XSS-Protection Found => ", str(header["X-XSS-Protection"]).replace(";", ",") )
        except KeyError:
            print("\033[1;31m[+]\033[0;37mX-XSS-Protection Not Found => ")
        try:
            print("\033[1;31m[+]\033[0;37mX-Frame-Options Found => ", header["X-Frame-Options"] )
        except KeyError:
            print("\033[1;31m[+]\033[0;37mX-Frame-Options Not Found => ")
        try:
            print("\033[1;31m[+]\033[0;37mX-Cache Found => ", header["X-Cache"] )
        except KeyError:
            print("\033[1;31m[+]\033[0;37mX-Cache not Found => ")
        
        # Ranges And Ages
        try:
            print("\033[1;31m[+]\033[0;37mAccept-Ranges Found => ", header["Accept-Ranges"] )
        except KeyError:
            print("\033[1;31m[+]\033[0;37mAccept-Ranges Not Found => ")
        try:
            print("\033[1;31m[+]\033[0;37mVary Found => ", header["Vary"] )
        except KeyError:
            print("\033[1;31m[+]\033[0;37mVary Not Found => ")
        try:
            print("\033[1;31m[+]\033[0;37mAge Found => ", header["Age"] )
        except KeyError:
            print("\033[1;31m[+]\033[0;37mAge Not Found => ")
        try:
            print("\033[1;31m[+]\033[0;37mExpect-CT Found => ", header["Expect-CT"] )
        except KeyError:
            print("\033[1;31m[+]\033[0;37mExcept-CT Not Found => ")
        try:
            print("\033[1;31m[+]\033[0;37mStrict-Transport-Security Found => ", header["Strict-Transport-Security"] )
        except KeyError:
            print("\033[1;31m[+]\033[0;37mStrict-Transport-Security Not Found => ")
        try:
            print("\033[1;31m[+]\033[0;37mContent-Encoding Found => ", header["Content-Encoding"] )
        except KeyError:
            print("\033[1;31m[+]\033[0;37mContent-Encoding Not Found => ")
        try:
            print("\033[1;31m[+]\033[0;37mCache-Control Found => ", header["Cache-Control"] )
        except KeyError:
            print("\033[1;31m[+]\033[0;37mCache-Control Not Found => ")
        try:
            print("\033[1;31m[+]\033[0;37mContent-Type Found => ", header["Content-Type"] )
        except KeyError:
            print("\033[1;31m[+]\033[0;37mContent-Type Not Found => ")
        
        # GeoIp Checking
        self.track(s)
        print("\033[1;31m[+]\033[0;37mWebsite Server City Found => {}\033[0;30m".format(self.city))
        print("\033[1;31m[+]\033[0;37mWebsite Server State Found => {}\033[0;30m".format(self.state))
        print("\033[1;31m[+]\033[0;37mWebsite Server Location in Latitude and Longitude Found => {}\033[0;30m".format(self.locationing))
        print("\033[1;31m[+]\033[0;37mWebsite Server Location Found => {}\033[0m".format(self.location2))
        print("\033[1;31m[+]\033[0;37mWebsite Server Found => {}".format(self.carrier))
        print("\033[1;31m[+]\033[0;37mWebsite Server Time Zone Found => {}".format(self.timeZone))
        self.dns_for_termux(str(self.url).split("/")[2])
        # CMS Checking
        
        # Wordpress url Checking
        # print("\033[1;31m<\033[1;37m---------------\033[1;31m[\033[1;37m CMS Detecting \033[1;31m]\033[1;37m-------------------\033[1;31m>")
        wpLoginCheck = requests.get(
            str(self.url) + '/wp-login.php', headers=user_agent)
        if wpLoginCheck.status_code == 200 and "user_login" in wpLoginCheck.text and "404" not in wpLoginCheck.text:
            print (f"\033[1;31m[+]\033[0;37mWord Press Pages => {self.url}/wp-login.php \033[1;32mDetected\033[0m")
        else:
            print ("\033[1;31m[+]\033[0;37mWord Press Pages NotFound => WP-Login")
            
        wpAdminUpgradeCheck = requests.get(url=str(self.url) + '/wp-admin/upgrade.php')
        if wpAdminUpgradeCheck.status_code == 200 and "404" not in wpAdminUpgradeCheck.text:
            print (f"\033[1;31m[+]\033[0;37mWord Press Pages => {self.url}/wp-admin/upgrade.php \033[1;32mDetected\033[0m")
        else:
            print("\033[1;31m[+]\033[0;37mWord Press Pages NotFound => WP-Admin/upgrade.php")
        
        wordpressAdmin = requests.get(str(self.url) + "/wp-admin",headers=user_agent) 
        if wordpressAdmin.status_code == 200 and "user_login" in wordpressAdmin.text and "404" not in wordpressAdmin.text:
            print(f"""\033[1;31m[+]\033[0;37mWord Press Pages => {self.url}/wp-admin \033[1;32mDetected\033[0m""")
        else:
            print("\033[1;31m[+]\033[0;37mWord Press Pages NotFound => WP-Admin")
        
        wpAdminReadMeCheck = requests.get(str(self.url) + '/readme.html')
        if wpAdminReadMeCheck.status_code == 200 and "404" not in wpAdminReadMeCheck.text:
            print (f"\033[1;31m[+]\033[0;37mWord Press Pages => {self.url}/readme.html \033[1;32mDetected\033[0m")
        else:
            print("\033[1;31m[+]\033[0;37mWord Press Pages NotFound => Readme.html")
        
        # PHP Scans
        php = requests.get(str(self.url))
        if php.status_code == 200 and 'phpmyadmin' in php.text:
            print("\033[1;31m[+]\033[0;37mPHP Admin Found => index page")
        else:
            print("\033[1;31m[+]\033[0;37mPHP Admin Not Found => index page")
        
        phpConfiguration = requests.get(str(self.url) + '/config.inc.php')
        if phpConfiguration.status_code == 200 and '404' not in phpConfiguration.text:
            print ("\033[1;31m[+]\033[0;37mPHP Admin Found => {}/config.inc.php".format(self.url))
        else:
            print ("\033[1;31m[+]\033[0;37mPHP Admin Not Found => config.inc.php")
            
        # Forwarding Urls
        print("\033[1;31m[+]\033[0;37mForwarding Urls")
        
        for urls in soup.find_all("a", attrs={"href": re.compile(r"^https://")}):
            print("\t\033[1;37m|--------> \033[1;32m{}\033[0m".format(urls.get("href")))
        print("\n\033[1;31m[+]\033[0;37mSub-Domain Found")
        # self.domain_scan(str(self.url).split("/")[2])
        with open('tools/web/domain.txt','r') as file:
            filename = file.read()
        sub_dom = filename.splitlines()
        self.domain_scanner(str(self.url).split('/')[2],sub_dom)
