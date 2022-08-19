#!/bin/bash


# Package Manager && Installer Start
function py () {
  pkg="python3"
  status="$(dpkg-query -W --showformat='${db:Status-Status}' "$pkg" 2>&1)"

  if [ ! $? = 0 ] || [ ! "$status" = installed ]; then
    printf "\033[1;31m[+] \033[0;37mPackage Not Found => $pkg\n"
    xterm -T "Installing" -geometry 100x30 -e "sudo apt install -y $pkg"
  else
    printf "\033[1;32m[+] \033[0;37mPackage Found => $pkg\n"
  fi
}
function py_pip () {
  pkg="python3-pip"
  status="$(dpkg-query -W --showformat='${db:Status-Status}' "$pkg" 2>&1)"

  if [ ! $? = 0 ] || [ ! "$status" = installed ]; then
    printf "\033[1;31m[+] \033[0;37mPackage Not Found => $pkg\n"
    xterm -T "Installing" -geometry 100x30 -e "sudo apt install -y $pkg"
  else
    printf "\033[1;32m[+] \033[0;37mPackage Found => $pkg\n"
  fi
}
function ruster () {
  pkg="rustc"
  status="$(dpkg-query -W --showformat='${db:Status-Status}' "$pkg" 2>&1)"

  if [ ! $? = 0 ] || [ ! "$status" = installed ]; then
    printf "\033[1;31m[+] \033[0;37mPackage Not Found => $pkg\n"
    xterm -T "Installing" -geometry 100x30 -e "sudo apt install -y $pkg"
  else
    printf "\033[1;32m[+] \033[0;37mPackage Found => $pkg\n"
  fi
}

# Added in Updates
function ffmpegg () {
  pkg="ffmpeg"
  status="$(dpkg-query -W --showformat='${db:Status-Status}' "$pkg" 2>&1)"

  if [ ! $? = 0 ] || [ ! "$status" = installed ]; then
    printf "\033[1;31m[+] \033[0;37mPackage Not Found => $pkg\n"
    xterm -T "Installing" -geometry 100x30 -e "sudo apt install -y $pkg"
  else
    printf "\033[1;32m[+] \033[0;37mPackage Found => $pkg\n"
  fi
}


function manager () {
    py
    py_pip
    ffmpegg
    ruster
}


# Pakcages Manager for termux

function py_termux () {
  pkg="python3"
  if [ $(dpkg-query -W -f='${Status}' $pkg 2>/dev/null | grep -c "ok installed") -eq 0 ]; then
    printf "\033[1;31m[+] \033[0;37mPackage Not Found => $pkg\n"
    apt-get install "$pkg" -y
  else
    printf "\033[1;32m[+] \033[0;37mPackage Found => $pkg\n"
  fi
}
function ffmpeg_termux () {
    pkg="python3"
    if [ $(dpkg-query -W -f='${Status}' $pkg 2>/dev/null | grep -c "ok installed") -eq 0 ]; then
      printf "\033[1;31m[+] \033[0;37mPackage Not Found => $pkg\n"
      apt-get install "$pkg" -y
    else
      printf "\033[1;32m[+] \033[0;37mPackage Found => $pkg\n"
    fi
}

# Python Module Manager for linux
function module_linux () {
  for item in {"trio","beautifulsoup4","httpx","holehe","phonenumbers","pyfiglet","termcolor","dnspython","simplejson","bs4","requests","pydub","Wave"}; do
    module=$(pip3 list | grep ${item} | awk '{print $1}')
    if [ "${item}" ==  "$module" ]; then
        printf "\033[1;32m[+] \033[0;37mModule Found => $module\n"
    else
        if [ "${item}" != "${module}" ]; then
            printf "\033[1;31m[+] \033[0;37mModule Not Found => ${item}\n"
            xterm -T "Installing" -geometry 100x30 -e "pip3 install ${item}"
        fi
    fi
  done
}

function module_termux () {
  for item in {"requests","beautifulsoup4","bs4","httpx","trio","holehe","phonenumbers","pyfiglet","termcolor","dnspython","simplejson","argparse"}; do
    module=$(pip3 list | grep ${item} | awk '{print $1}')
    if [ "${item}" ==  "$module" ]; then
        printf "\033[1;32m[+] \033[0;37mModule Found => $module\n"
    else
        if [ "${item}" != "${module}" ]; then
            printf "\033[1;31m[+] \033[0;37mModule Not Found => ${item}\n"
            pip3 install "${item}"
        fi
    fi
  done
}

# Package Manager && Installer End

# Global Functions

function internet_check () {
    wget -q --tries=10 --timeout=5 --spider https://google.com
    if [ $? -eq 0 ]; then
        printf '\033[1;32m[+] \033[0;37mInternet Connection Detected => OK\n'
    else
        printf '\033[1;31m[+] \033[0;37mInternet Connection Detected => NOT OK\n'
        exit 0
    fi
}

# GLobal Functions End

# Main Function Start
function main(){
    DIRECTORY='/data/data/com.termux/files/home/'
if [ -d "$DIRECTORY" ]; then
    internet_check
    apt install -y wget
    printf '\033[1;32m[+] \033[0;37m OS found => Termux\n'
    py_termux
    ffmpeg_termux
    module_termux
else
    internet_check
    sudo apt install -y wget
    printf '\033[1;32m[+] \033[0;37m OS found => Linux\n'
    os
    manager
    module_linux
fi
}
echo "$(tput setaf 2)"Network Tool Installer is Checking Neccessary Packages and Module....."$(tput sgr0)"
printf "\n"
sleep 5s
clear
dc=$(echo -n "LWQgQnkgQW1hbiBSYWoK" | base64 -d)

printf "\033[1;31m                      _   __     __                      __\n"
printf "\033[1;32m                     / | / /__  / /__      ______  _____/ /__\n"
printf "\033[1;33m                    /  |/ / _ \/ __/ | /| / / __ \/ ___/ //_/\n"
printf "\033[1;34m                   / /|  /  __/ /_ | |/ |/ / /_/ / /  / ,<\n"
printf "\033[1;35m                  /_/ |_/\___/\__/ |__/|__/\____/_/  /_/|_|\n"
printf "\033[1;37m                                                        $dc 0.4.0\033[1;36mBeta\033[0;35m Installer\033[0m\n"
printf "\n"

main
