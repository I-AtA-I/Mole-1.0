

mole is a CLI multi-use .py payload for BadUSB inject...

It is a tunnelmaker like tool that can help you in exploiting a system and retrieving vulnerable information from the target machine.

!!!On attacker site you need to allow "GatewayPorts" (GatewayPorts yes) and "AllowTcpForwarding" (AllowTcpForwarding yes) 
in 
etc/ssh/sshd_config!!!

Steps:

1) Download the files on your attacker computer
2) Put main.py and install_py.bat on a flashdisk you will be using to plug into the target computer
3) plug the flash disk into the target computer
4) run install_py.bat on the target machine installing python onto it (takes a few seconds)
5) open admin powershell and start main.py

