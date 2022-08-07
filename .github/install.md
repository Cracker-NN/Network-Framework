# Installation

- <mark>**Linux**</mark>
    - Automatic Installation
        - Sign Up For API Key ` https://ipinfo.io/ `
        - Paste on ` config/config.json `
            - ```
                {
                    "key": {
                        "ipinfo": "API KEY"
                    },
                    "Profile":{
                        "name": "",
                        "Install-Date": ""
                     },
                    "links":{
                        "ip-Info": "https://ipinfo.io/",
                        "NumVerify": "https://numverify.com/"
                     },
                    "termux-url": {
                        "NumVerify": "https://numverify.com/",
                        "hacker-target": "http://api.hackertarget.com/",
                        "ip-Info": "https://ipinfo.io/"
                    }
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
                        "ipinfo": "API KEY"
                    },
                    "Profile":{
                        "name": "",
                        "Install-Date": ""
                     },
                    "links":{
                        "ip-Info": "https://ipinfo.io/",
                        "NumVerify": "https://numverify.com/"
                     },
                    "termux-url": {
                        "NumVerify": "https://numverify.com/",
                        "hacker-target": "http://api.hackertarget.com/",
                        "ip-Info": "https://ipinfo.io/"
                    }
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
                        "ipinfo": "API KEY"
                    },
                    "Profile":{
                        "name": "",
                        "Install-Date": ""
                     },
                    "links":{
                        "ip-Info": "https://ipinfo.io/",
                        "NumVerify": "https://numverify.com/"
                     },
                    "termux-url": {
                        "NumVerify": "https://numverify.com/",
                        "hacker-target": "http://api.hackertarget.com/",
                        "ip-Info": "https://ipinfo.io/"
                    }
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
                        "ipinfo": "API KEY"
                    },
                    "Profile":{
                        "name": "",
                        "Install-Date": ""
                     },
                    "links":{
                        "ip-Info": "https://ipinfo.io/",
                        "NumVerify": "https://numverify.com/"
                     },
                    "termux-url": {
                        "NumVerify": "https://numverify.com/",
                        "hacker-target": "http://api.hackertarget.com/",
                        "ip-Info": "https://ipinfo.io/"
                    }
                  }
                ```
        - Package Installation
            - ` pkg install python3 -y `
            - ` pkg install php -y `
        
        - Module Installation
            ` pip3 install -r requirements.txt `
