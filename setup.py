import os
import time
import requests



black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

logo=f"""
{red}▒█░░▒█ █▀▀ █▀▀▄ ░░ ▒█░▒█ █▀▀█ █▀▀█ █░█ █▀▀ █▀▀█ 
{purple}▒█▒█▒█ █▀▀ █▀▀▄ ▀▀ ▒█▀▀█ █░░█ █░░█ █▀▄ █▀▀ █▄▄▀ 
{cyan}▒█▄▀▄█ ▀▀▀ ▀▀▀░ ░░ ▒█░▒█ ▀▀▀▀ ▀▀▀▀ ▀░▀ ▀▀▀ ▀░▀▀
                                         {red}[{blue}V{green}1.0{red}]

"""


if __name__=="__main__":   
        os.system("mkdir Hooked_site")
        os.system("clear")
        print(logo)
        os.system("pkg install wget && pip install requests && rm -rf setup.py && python3 WebHooker.py")

