import requests

def MacAddress(mac:str):
    r = requests.get("https://macvendors.co/api/" + str(mac))
    result = r.json()
    if result['result']:
        data = result['result']
        print("\033[1;31m[+]\033[0;37m MAC Company Name => " + data['company'])
        print("\033[1;31m[+]\033[0;37m MAC Address => " + data['address'])
        print("\033[1;31m[+]\033[0;37m Country Name => " + data['country'])
        print("\033[1;31m[+]\033[0;37m MAC Type => " + data['type'])
        print("")
    else:
        print("\033[1;31m[+]\033[0;37m NO Data Found")