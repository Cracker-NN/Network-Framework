import phonenumbers
from phonenumbers import geocoder, timezone, carrier
from geopy.geocoders import Nominatim
import sys


class location():
    def extract(self, number,api):
                from opencage.geocoder import OpenCageGeocode
                self.no_ = str( number )
                self.phone_number = phonenumbers.parse( self.no_ )
                self.times = timezone.time_zones_for_number( self.phone_number )
                self.location_country = geocoder.description_for_number(self.phone_number, 'en')
                self.carriers = carrier.name_for_number(self.phone_number, 'en')
                self.geography = OpenCageGeocode(api)
                self.responding = self.geography.geocode(str(self.location_country))
                self.latitude = self.responding[0]['geometry']['lat']
                self.longitude = self.responding[0]['geometry']['lng']
                self.geography = Nominatim(user_agent="geoapiExercises")
                self.location = self.geography.geocode(str(self.latitude )+ "," + str(self.longitude))
                self.console("\033[1;31m[+]\033[0;37mVictim Number Number Found => {}".format(self.no_))
                self.console("\033[1;31m[+]\033[0;37mVictim Number TimeZone Found => {}".format(self.times))
                self.console("\033[1;31m[+]\033[0;37mVictim Number Country Found => {}".format(self.location_country))
                self.console("\033[1;31m[+]\033[0;37mVictim Number Internet Service Provider Found => {}".format(self.carriers))
                self.console("\033[1;31m[+]\033[0;37mVictim Number Latitude Found => {}".format(self.latitude))
                self.console("\033[1;31m[+]\033[0;37mVictim Number Longitude Found => {}".format(self.longitude))
                self.console("\033[1;31m[+]\033[0;37mVictim Number Location Found => {}\033[0;30m".format(self.location))
    def termux(self, number):
            numbers = str(number)
            ph = phonenumbers.parse(numbers)
            timezones = timezone.time_zones_for_number(ph)
            loc = geocoder.description_for_number(ph, 'en')
            ISP = carrier.name_for_number(ph, 'en')
            print("\033[1;31m[+]\033[0;37mVictim Number Number Found => {}".format(numbers))
            print("\033[1;31m[+]\033[0;37mVictim Number TimeZone Found => {}".format(timezones))
            print("\033[1;31m[+]\033[0;37mVictim Number Country Found => {}".format(loc))
            print("\033[1;31m[+]\033[0;37mVictim Number Internet Service Provider Found => {}".format(ISP))

    def console(self, text:str):
        sys.stdout.write(text + "\n")


