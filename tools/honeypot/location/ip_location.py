from geopy.geocoders import Nominatim
import sys
import requests


class Geo_Loc():

    def grab(self, ip, api):
            self.geography = Nominatim(user_agent="geoapiExercises")
            url = f"https://ipinfo.io/{ip}?token={api}"
            r = requests.get(url)
            json = r.json()
            self.ip = json['ip']
            self.city = json['city']
            self.state = json['region']
            self.locationing = json['loc']
            self.timeZone = json['timezone']
            self.carrier = json['org']
            self.country_code = json['country']
            self.pin_code = json['postal']
            self.location2 = self.geography.geocode(self.locationing)

            self.console("\n\033[1;31m[+]\033[0;37mVictim City Found => {}\033[0;30m".format(self.city))
            self.console("\033[1;31m[+]\033[0;37mVictim State Found => {}\033[0;30m".format(self.state))
            self.console("\033[1;31m[+]\033[0;37mVictim IP Found => {}\033[0;30m".format(self.ip))
            self.console("\033[1;31m[+]\033[0;37mVictim Location in Latitude and Longitude Found => {}\033[0;30m".format(self.locationing))
            self.console("\033[1;31m[+]\033[0;37mVictim Location Found => {}\033[0m".format(self.location2))
            self.console("\033[1;31m[+]\033[0;37mVictim Time Zone Found => {}".format(self.timeZone))
            self.console("\033[1;31m[+]\033[0;37mVictim Carrier Found => {}".format(self.carrier))
            self.console("\033[1;31m[+]\033[0;37mVictim Country Code Found => {}".format(self.country_code))
            self.console("\033[1;31m[+]\033[0;37mVictim Pin Code Found => {}".format(self.pin_code))

    def console(self, text):
        sys.stdout.write(text + "\n")