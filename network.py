import os
import socket
from modules.help_tool import iplocate, honeypot, phone_number, mail, web_sc_adv, web_scan, url_scrap, url_capturing, MAC_Locater, Encrypt, Decrypt
import sys
from tools.location.ip_location import Geo_Loc
from modules.color import bright, low
from tools.honeypot.honeypot import HoneyPot
from modules.help import helps
from tools.location.location import location
from tools.mail.verify import Email
from tools.web.scan import Scan
from tools.web.scrap import Scrap
import json
import pyfiglet
from modules.help import tools, tools_temux
import termcolor
import random
import argparse
from modules.internet import internet
from modules.sprint import sprint
from tools.location.maclookup import MacAddress
from tools.audio_cryptor.encrypt import Encrypter
from tools.audio_cryptor.decrypt import Decryptor
from tools.audio_cryptor.converter import converter, converterWav


command = HoneyPot()
enter = b"\n"
color = "green", "red", "blue", "cyan", "yellow"
font = "slant", "shadow"
scrap = Scrap()
null = "\0"

class Network():
    def __init__(self):
        pass
    def encrypter(self):
        msg = str(input(f"\033[1;37mNetwork\033[1;32m:\033[1;37mEncrypter\033[1;32m:\033[1;37mMessage >\033[0m "))
        path = str(input(f"\033[1;37mNetwork\033[1;32m:\033[1;37mEncrypter\033[1;32m:\033[1;37mPath >\033[0m "))
        try:
            if msg == "cls":
                os.system("clear")
            elif msg == "show options":
                print(Encrypt)
                self.encrypter()
            elif msg == "exit":
                sys.exit(0)
            elif msg == "back":
                self.interface()
            else:
                en = Encrypter(str(msg.split('msg')[1]), os.path.join(str(path.split("file")[1].strip(" "))))
                en.encrypt()
                self.encrypter()
        except IndexError:
            self.encrypter()
    def decrypter(self):
        path = str(input(f"\033[1;37mNetwork\033[1;32m:\033[1;37mDecrypter\033[1;32m:\033[1;37mPath >\033[0m "))
        try:
            if path == "cls":
                os.system("clear")
            elif path == "show options":
                print(Decrypt)
                self.decrypter()
            elif path == "exit":
                sys.exit(0)
            elif path == "back":
                self.interface()
            else:
                dn = Decryptor(os.path.join(str(path.split("file")[1].strip(" "))))
                dn.decryptAudio()
                self.decrypter()
        except IndexError:
            self.decrypter()

    def mails(self, mail):
        return Email(mail)

    def Advance_web(self):
        web_adv_scanner = str(input(f"\033[1;37mNetwork\033[1;32m:\033[1;37mWEB Scanner Advance\033[1;32m:\033[1;37mUrl >\033[0m "))
        try:
            if web_adv_scanner == "exit":
                sys.exit(0)
            elif web_adv_scanner == "cls":
                os.system("clear")
                self.Advance_web()
            elif web_adv_scanner == "back":
                self.interface()
            elif web_adv_scanner == "show options":
                print(web_sc_adv)
                self.Advance_web()
            else:
                with open("config/config.json", "r") as f:
                    api = json.load(f)['key']['ipinfo']
                scanner = Scan(web_adv_scanner.split()[2], api)
                scanner.simplescan()
                self.Advance_web()
        except IndexError:
            self.Advance_web()

    def web_scraping(self):
        web_adv_scanner = str(input(f"\033[1;37mNetwork\033[1;32m:\033[1;37mWEB Scanner\033[1;32m:\033[1;37mUrl >\033[0m "))
        try:
            if web_adv_scanner == "exit":
                sys.exit(0)
            elif web_adv_scanner == "cls":
                os.system("clear")
                self.web_scraping()
            elif web_adv_scanner == "back":
                self.interface()
            elif web_adv_scanner == "show options":
                print(web_scan)
                self.web_scraping()
            else:
                scrap.data_scrap(web_adv_scanner.split()[2])
                self.web_scraping()
        except IndexError:
            self.web_scraping()

    def url_scraping(self):
        web_adv_scanner = str(input(f"\033[1;37mNetwork\033[1;32m:\033[1;37mUrl Scraping\033[1;32m:\033[1;37mUrl >\033[0m "))
        try:
            if web_adv_scanner == "exit":
                sys.exit(0)
            elif web_adv_scanner == "cls":
                os.system("clear")
                self.url_scraping()
            elif web_adv_scanner == "back":
                self.interface()
            elif web_adv_scanner == "show options":
                print(url_scrap)
                self.url_scraping()
            else:
                scrap.url(web_adv_scanner.split()[2])
                self.url_scraping()
        except IndexError:
            self.url_scraping()

    def web_caputing_tags(self):
        url = str(input(f"\033[1;37mNetwork\033[1;32m:\033[1;37mWeb Capture Tag\033[1;32m:\033[1;37mUrl >\033[0m "))
        tag = str(input(f"\033[1;37mNetwork\033[1;32m:\033[1;37mWeb Capture Tag\033[1;32m:\033[1;37mTag >\033[0m "))

        try:
            if url == "exit":
                sys.exit(0)
            elif url == "cls":
                os.system("clear")
                self.web_caputing_tags()
            elif url == "back":
                self.interface()
            elif url == "show options":
                print(url_capturing)
                self.web_caputing_tags()
            elif tag == "cls":
                os.system("clear")
                self.web_caputing_tags()
            elif tag == "exit":
                sys.exit(0)
            elif tag == "back":
                self.interface()
            elif tag == "show options":
                print(url_capturing)
                self.web_caputing_tags()
            else:
                scrap.capture_tag(url.split()[2], tag.split()[2])
                self.web_caputing_tags()
        except IndexError:
            self.web_caputing_tags()

    def Email_Scan(self):

        mailer = str(input(f"\033[1;37mNetwork\033[1;32m:\033[1;37mEmail Scanner\033[1;32m:\033[1;37mEmail >\033[0m "))

        try:
            if mailer == "exit":
                sys.exit(0)
            elif mailer == "cls":
                os.system("clear")
                self.Email_Scan()
            elif mailer == "back":
                self.interface()
            elif mailer == "show options":
                print(mail)
                self.Email_Scan()
            else:
                    mails = self.mails(mailer.split()[2])
                    mails.run()
                    self.Email_Scan()
        except IndexError:
            self.Email_Scan()

    def phone_number(self):

        phone_numbers = location()
        self.number = str(input(f"\033[1;37mNetwork\033[1;32m:\033[1;37mPhone Number\033[1;32m:\033[1;37mNumber >\033[0m "))
        try:
            if self.number == "exit":
                sys.exit(0)
            elif self.number == "cls":
                os.system("clear")
                self.phone_number()
            elif self.number == "back":
                self.interface()
            elif self.number == "show options":
                print(phone_number)
                self.phone_number()
            else:
                self._ = self.number.split()[2]
                with open("config/config.json", "r") as fd:
                    api = json.load(fd)['key']['numVerify']

                if os.path.isdir("/data/data/com.termux/files/home") == True:
                    phone_numbers.termux(self._, api)
                    self.phone_number()
                else:
                    phone_numbers.extract(self._, api)
                    self.phone_number()

        except IndexError:
            self.phone_number()

    def IP(self):

        ipaddr = Geo_Loc()
        self.geo = input(f"\033[1;37mNetwork\033[1;32m:\033[1;37mIP_Locate\033[1;32m:\033[1;37mIP >\033[0m ")
        try:
            if self.geo == "exit":
                sys.exit(0)
            elif self.geo == "cls":
                os.system("clear")
                self.IP()
            elif self.geo == "back":
                self.interface()
            elif self.geo == "show options":
                print(iplocate)
                self.IP()
            else:
                self.ip = self.geo.split()[2]
                with open("config/config.json", "r") as f:
                    api = json.load(f)["key"]["ipinfo"]
                ipaddr.grab(self.ip, api)
                self.IP()
        except IndexError:
            self.IP()

    def MAC(self):
        self.mac = input(f"\033[1;37mNetwork\033[1;32m:\033[1;37mMAC_Locater\033[1;32m:\033[1;37mMAC >\033[0m ")
        try:
            if self.mac == "exit":
                sys.exit(0)
            elif self.mac == "cls":
                os.system("clear")
                self.MAC()
            elif self.mac == "back":
                self.interface()
            elif self.mac == "show options":
                print(MAC_Locater)
                self.MAC()
            else:
                self.mac = self.mac.split()[2]
                MacAddress(mac=self.mac)
                self.MAC()
        except IndexError:
            self.MAC()

    def HoneyPot(self):
        command = HoneyPot()

        self.honey = input(f"\033[1;37mNetwork\033[1;32m:\033[1;37mHoneyPot\033[1;32m:\033[1;37mIP >\033[0m ")
        try:
            if self.honey == "exit":
                sys.exit(0)
            elif self.honey == "cls":
                os.system("clear")
                self.HoneyPot()
            elif self.honey == "back":
                self.interface()
            elif self.honey == "show options":
                self.HoneyPot()
            else:
                self.ip = self.honey.split()[2]
        except IndexError:
            self.HoneyPot()

        while True:

            template = input(f"\033[1;37mNetwork\033[1;32m:\033[1;37mHoneyPot\033[1;32m:\033[1;37mTemplate >\033[0m ")
            if template == "set template denied":
                try:
                    print( "HoneyPot Started on http://{}".format( self.ip ) )
                    with open("tools/honeypot/template/denied.html", 'r') as f:
                        data = f.read()
                    command.honeypot(self.ip, data)
                except socket.gaierror and Exception:
                    self.HoneyPot()
                self.HoneyPot()
            elif self.honey == "help honeypot":
                        print(honeypot)
            elif template == "set template 402":
                try:
                    print( "HoneyPot Started on http://{}".format( self.ip ) )
                    with open("tools/honeypot/template/402.html", 'r') as f:
                        data = f.read()
                    command.honeypot(self.ip, data)
                except socket.gaierror and Exception:
                    self.HoneyPot()
                self.HoneyPot()
            elif template == "set template error":
                try:
                    print( "HoneyPot Started on http://{}".format( self.ip ) )
                    with open("tools/honeypot/template/error.html", 'r') as f:
                        data = f.read()
                    command.honeypot(self.ip, data)
                except socket.gaierror and Exception:
                    self.HoneyPot()
                self.HoneyPot()
            elif template == "set template matrix":
                try:
                    print( "HoneyPot Started on http://{}".format( self.ip ) )
                    with open("tools/honeypot/template/matrix.html", 'r') as f:
                        data = f.read()
                    command.honeypot(self.ip, data)
                except socket.gaierror and Exception:
                    self.HoneyPot()
                self.HoneyPot()
            elif template == "set template not_found":
                try:
                    print( "HoneyPot Started on http://{}".format( self.ip ) )
                    with open("tools/honeypot/template/not_found.html", 'r') as f:
                        data = f.read()
                    command.honeypot(self.ip, data)
                except socket.gaierror and Exception:
                    self.HoneyPot()
                self.HoneyPot()
            elif template == "back":
                self.interface()
            elif template == "exit":
                sys.exit(0)
            elif template == "cls":
                os.system("clear")
            else:
                self.HoneyPot()

    def interface(self):
        while True:
            self.user = input(f"\033[1;37mNetwork\033[1;32m:\033[1;37m >\033[0m ")
            # Use Function Define
            """
            >>> import network

            >>> network.interface()

            """
            if self.user == "use honeypot":
                if os.path.isdir("/data/data/com.termux/files/home") == True:
                    print("\033[0;31mAccess Denied\033[0m")
                    self.interface()
                else:
                    print("\033[0;37mType \033[0;31m`set ip < IP >\033[0;37m` for set the System IP For scanning and \033[0;31m`set template < Template >\033[0;37m`")
                    self.HoneyPot()
            elif self.user == "use ip_locate":
                with open("config/config.json", "r") as ip:
                    ips = str(json.load(ip)["key"]["ipinfo"])
                if ips == "" or ips.isspace() == True:
                    print("\033[0;31mAccess Denied\033[0m")
                    self.interface()
                else:
                    print("\033[0;37mType \033[0;31m`set ip < Public IP >\033[0;37m` for set the IP For scanning")
                    self.IP()

            elif self.user == "use phone_no":
                with open("config/config.json", "r") as nv:
                    numVerify = str(json.load(nv)["key"]["numVerify"])
                if numVerify == "" or numVerify.isspace() == True:
                    print("\033[0;31mAccess Denied\033[0m")
                    self.interface()
                else:
                    print("\033[0;37mType \033[0;31m`set no < Phone Number >\033[0;37m` for set the Phone Number For scanning")
                    self.phone_number()
            elif self.user == "use email_sc":
                print("\033[0;37mType \033[0;31m`set mail < Mail >\033[0;37m` for set the Email For scanning")
                self.Email_Scan()
            elif self.user == "use web_sc_adv":
                print("\033[0;37mType \033[0;31m`set url < URL >\033[0;37m` for set the Url For scanning")
                self.Advance_web()
            elif self.user == "use web_sc":
                print("\033[0;37mType \033[0;31m`set url < URL >\033[0;37m` for set the Url For scanning")
                self.web_scraping()
            elif self.user == "use url_cp":
                print("\033[0;37mType \033[0;31m`set url < URL >\033[0;37m` for set the Url and \033[0;31m`set tag < Tag >\033[0;37m` For Capturing Tag")
                self.web_caputing_tags()
            elif self.user == "use url_scr":
                print("\033[0;37mType \033[0;31m`set url < URL >\033[0;37m` for set the Url For Scraping")
                self.url_scraping()
            elif self.user == "use MAC_Locater":
                print("\033[0;37mType \033[0;31m`set mac < MAC >\033[0;37m` for set the MAC Address For Extracting")
                self.MAC()
            elif self.user == "use Encrypter":
                print("\033[0;37mType \033[0;31m`set msg < Message >\033[0;37m` for set the Message and \033[0;31m`set file < Audio File >\033[0;37m` For Scanning and Encrypting the AudioFile")
                self.encrypter()
            elif self.user == "use Decrypter":
                print("\033[0;31m`set file < Audio File >\033[0;37m` For Decrypting the AudioFile")
                self.decrypter()

            # GLobal Functions

            elif self.user == "help" or self.user == "?":
                print( helps )
            elif self.user == "cls":
                os.system( "clear" )
            elif self.user == "exit":
                sys.exit( 0 )
            elif self.user == "use":
                print(helps)
            elif self.user == "cmp":
                cmp = str(input("\033[1;37mPath\033[1;32m:\033[1;37m >\033[0m "))
                converter(r"{}".format(cmp))
            elif self.user == "cwav":
                cwav = str(input("\033[1;37mPath\033[1;32m:\033[1;37m >\033[0m "))
                converterWav(r"{}".format(cwav))
            elif self.user == "ipconfig":
                hostname = socket.gethostname()
                ip_address = socket.gethostbyname(hostname)
                print("\033[1;32m[+] \033[0;37m IP address => {}".format(ip_address))


            # Help Functions

            elif self.user == "help honeypot":
                print(honeypot)
            elif self.user == "help ip_locate":
                print(iplocate)
            elif self.user == "help phone_no":
                print(phone_number)
            elif self.user == "help email_sc":
                print(mail)
            elif self.user == "help web_sc_adv":
                print(web_sc_adv)
            elif self.user == "help web_sc":
                print(web_scan)
            elif self.user == "help url_cp":
                print(url_capturing)
            elif self.user == "help url_scr":
                print(url_scrap)
            elif self.user == "help MAC_Locater":
                print(MAC_Locater)
            elif self.user == "help Encrypter":
                print(Encrypt)
            elif self.user == "help Decrypter":
                print(Decrypt)

            # Non-GLobal Functions
            elif self.user == "banner":
                print( termcolor.colored( pyfiglet.figlet_format( "Network", font=random.choice(font), justify="center" ),
                                          random.choice( color ), attrs=["bold"] ) )
                print( "\t\t\t\t\t\t\033[1;31mBy Aman Raj 0.1 \033[1;36mBeta\033[0m" )
            elif self.user == "tool" or self.user == "tools":
                if os.path.isdir("/data/data/com.termux/files/home") == True:
                    print(tools_temux)
                else:
                    print(tools)

            # Else Statement
            else:
                if self.user.isalpha() == True:
                    print("\033[1;31m[-] \033[0;37mUnknown Command")
                elif self.user.isdigit() == True:
                    print("\033[1;31m[-] \033[0;37mUnknown Command")

                # Newly Added Functions
                elif self.user.isspace() == True:
                    pass
                elif self.user == "":
                    pass
                # Newly Added Functions Ended
                else:
                    print("\033[1;31m[-] \033[0;37mUnknown Command")

    def run(self):
        print( termcolor.colored( pyfiglet.figlet_format( "Network", font=random.choice(font), justify="center" ),
                                  random.choice( color ), attrs=["bold"] ) )
        print( "\t\t\t\t\t\t\033[1;31mBy Aman Raj 0.1 \033[1;36mBeta\033[0m" )
        # print("\t\033[0;37mType \033[0;32m`help`\033[0;37m for check help menu\n")
        keys = "\033[0;37mType \033[0;32m`help`\033[0;37m for check help menu\n", "\033[0;37mType \033[0;32m`exit`\033[0;37m for exit\n", "\033[0;37mType \033[0;32m`use`\033[0;37m for using any tool\n", "\033[0;37mType \033[0;32m`banner`\033[0;37m for Printing Banner\n", "\033[0;37mType \033[0;32m`cls`\033[0;37m for clearing the console\n"
        print(random.choice(keys))
        self.interface()
    def no_banner_run(self):
        self.interface()

    def arguments_start(self):
        parser = argparse.ArgumentParser(description="Copyright (c) 2022 to 2030 and it has created by Aman Raj. Our github account is https://github.com/amanraj-bose/,every options have to arguments.")
        parser.add_argument("--author", "-a", help="For Seeing Author Name")
        parser.add_argument("--version", "-v",
                    version="%(prog)s 0.1", action="version")
        parser.add_argument("--no_banner", "-q", help="Starting Network Without Banner using this arguments none. example: python3 network.py -q none")
        # self.run()
        args = parser.parse_args()
        if args.no_banner == "none":
            internet()
            sprint("Network is Starting.....")
            print("\n")
            self.no_banner_run()
        else:
            internet()
            sprint("Network is Starting.....")
            print("\n")
            self.run()


if __name__ == '__main__':
    network = Network()
    network.arguments_start()

