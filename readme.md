<p align="center">
    <img width="400" height="200" src="https://user-images.githubusercontent.com/88227750/177171076-02009005-0048-4b08-b755-4cdf60d57b55.png">
</p>
<p align="center">
    <a href="https://twitter.com/amanraj_Phunish">
    <img alt="Twitter URL" src="https://img.shields.io/twitter/url?label=Twitter&style=social&url=https%3A%2F%2Ftwitter.com%2Famanraj_Phunish"></a>
    <img src="https://img.shields.io/badge/Version-0.1-blue">
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green"></a>
    <br>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8-blue"></a>
    <a href="https://en.wikipedia.org/wiki/Linux"><img src="https://img.shields.io/badge/Platform-Linux%20Based-yellow"></a>
    <a href="https://youtube.com/"><img src="https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=youtube&logoColor=white" alt="Youtube Badge"/></a>
 </p>

# Network-Framework

**_THIS TOOL USING FOR GATHERING INFORMATION FROM ANY WEBSITES, Email Address, and Phone Number._**

## Platform Support & Tested
- Linux
    - Kali Linux
    - Ubuntu Linux
    - Debian Linux
    - Parrot Linux
- Android
    - Termux
## Fetching Tool From github

              sudo apt install git or apt install git
#             
              git clone https://github.com/amanraj-bose/Network-Framework.git
#
              cd Network-Framework

## Installation
- <mark>**Linux**</mark>
    - Automatic Installation
        - Sign Up For API Key ` https://ipinfo.io/ ` and ` https://opencagedata.com/users/sign_in#geocoding `
        - Paste on ` config/config.json `
            - ```
                {
                "key": {
                    "ipinfo": "<API KEY>",
                    "opengrab": "<API KEY>"
                    },
                "Profile":{
                    "name": "",
                    "Install-Date": ""
                    },
                "links":{
                    "ip-Info": "https://ipinfo.io/",
                    "opencage": "https://opencagedata.com/"
                    },
                "termux-url": {
                "hacker-target": "http://api.hackertarget.com/",
                "ip-Info": "https://ipinfo.io/"
                    },
                }
                ```
        - Script Permission ` chmod u+x install.sh ` or ` chmod +x install.sh `

        - Run ` sh install.sh ` if any error occurs ` ./install.sh `
            
    - Manual Installation
        - Sign Up For API Key ` https://ipinfo.io/ ` and ` https://opencagedata.com/users/sign_in#geocoding `
        - Paste on ` config/config.json `
            - ```
                {
                "key": {
                    "ipinfo": "<API KEY>",
                    "opengrab": "<API KEY>"
                    },
                "Profile":{
                    "name": "",
                    "Install-Date": ""
                    },
                "links":{
                    "ip-Info": "https://ipinfo.io/",
                    "opencage": "https://opencagedata.com/"
                    },
                "termux-url": {
                "hacker-target": "http://api.hackertarget.com/",
                "ip-Info": "https://ipinfo.io/"
                    },
                }
                ```
        - Package Installation
            - ` sudo apt install python3 -y `
            - ` sudo apt install python3-pip -y `
            - ` sudo apt install php -y `
            - ` sudo apt install rustc -y `
            - ` sudo apt install cargo -y `
            - ` sudo apt install sox -y `
        
        - Module Installation
            ` sudo pip3 install -r requirements.txt `

- <mark>**Termux ( ANDROID )**</mark>
    - Automatic Installation
        - Sign Up For API Key ` https://ipinfo.io/ `
        - Paste on ` config/config.json `
            - ```
                {
                "key": {
                    "ipinfo": "<API KEY>",
                    "opengrab": ""
                    },
                "Profile":{
                    "name": "",
                    "Install-Date": ""
                    },
                "links":{
                    "ip-Info": "https://ipinfo.io/",
                    "opencage": "https://opencagedata.com/"
                    },
                "termux-url": {
                "hacker-target": "http://api.hackertarget.com/",
                "ip-Info": "https://ipinfo.io/"
                    },
                }
                ```
        - Script Permission ` chmod u+x install.sh ` or ` chmod +x install.sh `
        - Run ` sh install.sh ` if any error occurs ` ./install.sh `
    
    - Manual Installation
        - Sign Up For API Key ` https://ipinfo.io/ `
        - Paste on ` config/config.json `
            - ```
                {
                "key": {
                    "ipinfo": "<API KEY>",
                    "opengrab": ""
                    },
                "Profile":{
                    "name": "",
                    "Install-Date": ""
                    },
                "links":{
                    "ip-Info": "https://ipinfo.io/",
                    "opencage": "https://opencagedata.com/"
                    },
                "termux-url": {
                "hacker-target": "http://api.hackertarget.com/",
                "ip-Info": "https://ipinfo.io/"
                    },
                }
                ```
        - Package Installation
            - ` pkg install python3 -y `
            - ` pkg install php -y `
        
        - Module Installation
            ` pip3 install -r requirements.txt `
#
### Module List
- Python Modules
    - requests
    - beautifulsoup4
    - httpx
    - trio
    - holehe
    - phonenumbers
    - geopy
    - pyfiglet
    - termcolor
    - dnspython
    - simplejson
    - bs4
    - argparse
    - opencage


## Usages
```    
root@Ubuntu $: python3 network.py --help

usage: network.py [-h] [--author AUTHOR] [--version] [--no_banner NO_BANNER]

Copyright (c) 2022 to 2030 and it has created by Aman Raj. Our github account is https://github.com/amanraj-
bose/,every options have to arguments.

optional arguments:
  -h, --help            show this help message and exit
  --author AUTHOR, -a AUTHOR
                        For Seeing Author Name
  --version, -v         show program's version number and exit
  --no_banner NO_BANNER, -q NO_BANNER
                        Starting Network Without Banner using this arguments none. example: python3 network.py -q none

```

## Description

 ```
    -h, --help            show this help message and exit.
    --author, -a AUTHOR   For Seeing Author Name.
    --version, -v         show program's version number and exit.
    --no_banner, -q       For No Banner Starting. 
 ```

 - Keywords

```
    Name                    Description
    ----                    -----------

    None                 using with --no_banner or -q

```

## Examples

```
root@Ubuntu $: python3 network.py -q none 
```

<video src="https://user-images.githubusercontent.com/88227750/178748824-0c2ef687-666c-40d1-a623-19b5232af3bc.mp4" width="800">
</video>


## Features
- Email Verifier Scan
- Email Domain Scan
- Email Social Media Scan
- IP Info Finder
- IP Geolocation Finder
- Website Domain Scan
- Website IP Scan
- Website Geolocation
- Content-type Scan
- Website Header Scan
- Website Link Scan
- Subdomain Scan
- CMS Scan
- Phone Number Scan
- Website Tag Capturing
- Website URL Scraping

<!-- ## Tools List and Features

- HoneyPot
    - HoneyPot is a tool which can extract the information of Attacker.

- Email scanner
    - Email Scanner is a osint tool which can find the email address on Pouplar Social Media Sites.
    - Included Tools
        - Email Verifier
        - Email Domain
        - Email Social Media
        - Site List
            - Instagram
            - Twitter
            - Github
            - Spotify
            - Petrone
            - Pinterest
            - WordPress
            - Quora
            - Google
            - Yahoo
            - Flickr
            - Nike
            - Docker
            - Amazon
            - Samsung
            - PS

- Ip Locate -->

<!-- - ip_locate -->

## Update's

`Patch Update on Beta Version 1 month ago`

## Update-Process

- ****Unistall the network tool****
- **reinstall it**

## author
- [@Aman Raj]((https://github.com/amanraj-bose))

## License
<p align="center">
    <img src=".github/mit.png"></img>

```
MIT License

Copyright (c) 2021 amanraj-bose

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
</p>

## Copyright
<mark>**©️ Copyright 2022 Aman Raj. All rights reserved.**</mark>


<hr>

# Special Thanks to Thumb Group

> **special thanks to Thumb Group for their support**