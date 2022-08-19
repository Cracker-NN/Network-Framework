import sys
import requests
from tools.mail.websites.social_media.twitter import *
from tools.mail.websites.social_media.instagram import *
from tools.mail.websites.music.spotify import *
from tools.mail.websites.social_media.patreon import *
from tools.mail.websites.social_media.pinterest import *
from tools.mail.websites.cms.wordpress import *
from tools.mail.websites.jobs.freelancer import *
from tools.mail.websites.learning.quora import *
from tools.mail.websites.mails.google import *
from tools.mail.websites.mails.yahoo import *
from tools.mail.websites.medias.flickr import *
from tools.mail.websites.software.docker import *
from tools.mail.websites.products.nike import *
from tools.mail.websites.products.samsung import *
from tools.mail.websites.shopping.amazon import *
from tools.mail.websites.porn.pornhub import *
import httpx
import trio
import re

class Email():
    def __init__(self, mail):
        self.mail = mail
        self.symbols = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        self.lists = []
        
    def console(self, text):
        sys.stdout.write(text + "\n")
    def verify(self):
        self.console(f"\033[1;31m[+]\033[0;37mEmail \033[0;37m=> \033[0;37m{self.mail}")

        if re.search(self.symbols, self.mail):
            self.console("\033[1;31m[+]\033[0;37mEmail Verification \033[0;37m=> \033[0;37mValid Email")
        else:
            self.console("\033[1;31m[+]\033[0;37mEmail Verification \033[0;37m=> \033[0;37mInvalid Email")
        
        print("\033[1;31m[+]\033[0;37mEmail Domain => {}".format(str(str(self.mail).split("@")[1])))
            
    def breaching(self):
        HEADERS = {'user-agent': 'pypi.org/project/haveibeenpwnd/ v0.1', 'api-version': 2}
        email_url = 'https://haveibeenpwned.com/api/v2/breachedaccount/{}'
        error_messages = {
    400: "Bad request — the account does not comply with an acceptable format "
            "(i.e. it's an empty string)",
    403: "Forbidden — no user agent has been specified in the request",
    429: "Too many requests — the rate limit has been exceeded",
    526: "Cloudflare SSL Error - please try again later"
    }
        response = requests.get(email_url.format(self.mail), HEADERS)
        http_status = response.status_code
        if http_status == 200:
            return {
            'breaches': response.json()
            }
        elif http_status == 404:
            return {'breaches': []}
        else:
            message = error_messages.get(http_status, "Unknown error: {}".format(http_status))
            return {
            'error': message,
            'breaches': ''
            }
    
    def breached(self):
        safe = {'error': 'Unknown error: 401', 'breaches': ''}
        if self.breaching() == safe:
            self.console("\033[1;31m[+]\033[0;37mEmail Breach Check\033[0;37m => Not Breached")
        else:
            self.console("\033[1;31m[+]\033[0;37mEmail Breach Check\033[0;37m => Breached")
            
    async def freelancer(self):
        out = []
        client = httpx.AsyncClient()
        await freelancer( self.mail, client, out )
        self.lists.append( out )
        await client.aclose()
    async def flickr(self):
        out = []
        client = httpx.AsyncClient()
        await flickr( self.mail, client, out )
        self.lists.append( out )
        await client.aclose()
    async def docker(self):
        out = []
        client = httpx.AsyncClient()
        await docker( self.mail, client, out )
        self.lists.append( out )
        await client.aclose()
    async def amazon(self):
        out = []
        client = httpx.AsyncClient()
        await amazon( self.mail, client, out )
        self.lists.append( out )
        await client.aclose()
    async def nike(self):
        out = []
        client = httpx.AsyncClient()
        await nike( self.mail, client, out )
        self.lists.append( out )
        await client.aclose()

    async def google(self):
        out = []
        client = httpx.AsyncClient()
        await google( self.mail, client, out )
        self.lists.append( out )
        await client.aclose()
    async def yahoo(self):
        out = []
        client = httpx.AsyncClient()
        await yahoo( self.mail, client, out )
        self.lists.append( out )
        await client.aclose()
    async def quora(self):
        out = []
        client = httpx.AsyncClient()
        await quora( self.mail, client, out )
        self.lists.append( out )
        await client.aclose()

    async def github(self):
        out = []
        r = requests.get( "https://api.twitter.com/i/users/email_available.json",
                        params={
                            "email": self.mail} )
        if r.json()['valid'] == True:
            print("", end="")
        else:
            self.console( "\t[+] Github".upper() )
        self.lists.append(out)
    async def wordpress(self):
        out = []
        client = httpx.AsyncClient()
        await wordpress( self.mail, client, out )
        self.lists.append( out )
        await client.aclose()
    async def pin(self):
        out = []
        client = httpx.AsyncClient()
        await pinterest( self.mail, client, out )
        self.lists.append( out )
        await client.aclose()
    async def samsung(self):
        out = []
        client = httpx.AsyncClient()
        await samsung( self.mail, client, out )
        self.lists.append( out )
        await client.aclose()
    async def xvide(self):
        out = []
        client = httpx.AsyncClient()
        await pornhub( self.mail, client, out )
        self.lists.append( out )
        await client.aclose()

    async def petro(self):
        out = []
        client = httpx.AsyncClient()
        await patreon( self.mail, client, out )
        self.lists.append( out )
        await client.aclose()

    async def twitters(self):
        out = []
        client = httpx.AsyncClient()
        await twitter( self.mail, client, out )
        self.lists.append( out )
        await client.aclose()

    async def instagrams(self):
        out = []
        client = httpx.AsyncClient()
        await instagram( self.mail, client, out )
        self.lists.append( out )
        await client.aclose()

    async def spot(self):
        out = []
        client = httpx.AsyncClient()
        await spotify( self.mail, client, out )
        self.lists.append( out )
        await client.aclose()
    
    def mail_check_on_website(self):
        self.console( "\033[1;31m[+]\033[0;37mSocial Media Website Found =>" )
        print("\033[1;32m")
        trio.run(self.twitters)
        trio.run(self.instagrams)
        trio.run(self.spot)
        trio.run(self.github)
        trio.run(self.petro)
        trio.run(self.pin)
        trio.run(self.wordpress)
        trio.run(self.freelancer)
        trio.run(self.quora)
        trio.run(self.google)
        trio.run(self.yahoo)
        trio.run(self.flickr)
        trio.run(self.docker)
        trio.run(self.amazon)
        trio.run(self.nike)
        trio.run(self.samsung)
        trio.run(self.xvide)
        ac = []
        for i in self.lists:
            try:
                if i[0]['exists'] == True:
                    ac.append( i[0]['name'] )
            except:
                pass

        a = ac
        fo = str( a ).replace( '[', '' ).replace( ']', '' ).replace( "'", "" ).replace( ', ', '\n\t\033[1;32m[+] ' ).upper()
        self.console( "\033[1;32m\t[+] " + fo )
        print("\033[0;30m")

    def run(self):
        self.verify()
        self.breached()
        self.mail_check_on_website()
