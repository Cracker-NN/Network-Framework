import phonenumbers
from phonenumbers import geocoder, timezone, carrier
import sys
import requests



class location():
    def extract(self, number, api):
            numbers = str(number)
            req = requests.get("http://apilayer.net/api/validate?access_key=" + str(api) + "&number=" + numbers)
            results = req.json()
            ph = phonenumbers.parse(numbers)
            timezones = timezone.time_zones_for_number(ph)
            loc = geocoder.description_for_number(ph, 'en')
            ISP = carrier.name_for_number(ph, 'en')
            print("\033[1;31m[+]\033[0;37mVictim Number Number Found => {}".format(numbers))
            print("\033[1;31m[+]\033[0;37mVictim Number TimeZone Found => {}".format(timezones))
            print("\033[1;31m[+]\033[0;37mVictim Number Country Found => {}".format(loc))
            print("\033[1;31m[+]\033[0;37mVictim Number Internet Service Provider Found => {}".format(ISP))
            try:
                print("\033[1;31m[+]\033[0;37mVictim Country Name => {}".format(results['country_name']))
            except KeyError:
                print("\033[1;31m[+]\033[0;37mVictim Country Name => ")
            try:
                print("\033[1;31m[+]\033[0;37mVictim Location => {}".format(results['location']))
            except KeyError:
                print("\033[1;31m[+]\033[0;37mVictim Location => ")
            try:
                print("\033[1;31m[+]\033[0;37mVictim Line Type => {}".format(results['line_type']))
            except KeyError:
                print("\033[1;31m[+]\033[0;37mVictim Line Type => ")
    def termux(self, number, api):
            numbers = str(number)
            req = requests.get("http://apilayer.net/api/validate?access_key=" + str(api) + "&number=" + numbers)
            results = req.json()
            ph = phonenumbers.parse(numbers)
            timezones = timezone.time_zones_for_number(ph)
            loc = geocoder.description_for_number(ph, 'en')
            ISP = carrier.name_for_number(ph, 'en')
            print("\033[1;31m[+]\033[0;37mVictim Number Number Found => {}".format(numbers))
            print("\033[1;31m[+]\033[0;37mVictim Number TimeZone Found => {}".format(timezones))
            print("\033[1;31m[+]\033[0;37mVictim Number Country Found => {}".format(loc))
            print("\033[1;31m[+]\033[0;37mVictim Number Internet Service Provider Found => {}".format(ISP))
            try:
                print("\033[1;31m[+]\033[0;37mVictim Country Name => {}".format(results['country_name']))
            except KeyError:
                print("\033[1;31m[+]\033[0;37mVictim Country Name => ")
            try:
                print("\033[1;31m[+]\033[0;37mVictim Location => {}".format(results['location']))
            except KeyError:
                print("\033[1;31m[+]\033[0;37mVictim Location => ")
            try:
                print("\033[1;31m[+]\033[0;37mVictim Line Type => {}".format(results['line_type']))
            except KeyError:
                print("\033[1;31m[+]\033[0;37mVictim Line Type => ")

    def console(self, text:str):
        sys.stdout.write(text + "\n")



