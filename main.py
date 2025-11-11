#this file is for starting the program
import os
def cls():
    os.system("cls")

from colorama import init, Fore, Back, Style
init(autoreset=True)

import socket
import sys
from time import sleep
import platform


#ask for password to start the program else exit
password="krtek"
askforpassword = input(Fore.YELLOW + "Enter password to start the program: ")
sleep(0.1)
if askforpassword != password:
    print(Fore.RED + "Incorrect password, exiting...")
    sleep(0.5)
    exit()
else:
    print(Fore.GREEN + "Password correct, starting program...")
    sleep(0.5)

#ask to scan the machine whilst if "y" then gather system information else if "n" ask to continue else exit
asktoscan = input("Welcome, scan this machine? y/n: ")
sleep(0.1)

if asktoscan == "y":
    cls()
    print("Gathering system information...")
    sleep(1)
    #gather system information using platform module
    print("System Information:")
    sleep(0.1)
    system=platform.system()
    print(Fore.RED + platform.system())
    sleep(0.1)
    node=platform.node()
    print(platform.node())
    sleep(0.1)
    machine=platform.machine()
    print(platform.machine())
    sleep(0.1)
    platform_info=platform.platform()
    print(Fore.RED + platform.platform())
    sleep(0.1)
    ip=socket.gethostbyname(socket.gethostname())
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(Fore.RED + s.getsockname()[0])
    s.close()
    print("System information gathered.")
    sleep(1)
    input("Press Enter to continue...")
    
    info=system + "\n" + node + "\n" + machine + "\n" + platform_info + "\n" + ip

#if user inputs "n" ask to continue else exit 
elif asktoscan == "n":
    asktocontinue = input("Continue with the program? y/n: ")
    sleep(0.1)

#if user inputs "y" wait for program else exit
    if asktocontinue == "y":
        print("Waiting for program...")
        sleep(0.1)
    elif asktocontinue == "n":
        exit()
    else:
        exit()

else:
    exit()

cls()
