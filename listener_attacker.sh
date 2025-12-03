#!/bin/bash
echo "This program will start a listener for a reverse ssh..."

echo "Put in password for sudo"
read sudo


sudo pacman -S sshd
sudo systemctl enable sshd
sudo systemctl enable sshd
sudo systemctl start sshd

sudo ufw disable

while true; do
  echo "Input target username: "
  read targetusername
  echo "Input target IP (without port): "
  read targetIP
  clear
  echo "You inputed" $targetusername "as target username and " $targetIP "as target IP, correct? y/n :"
  read correction
  if [ $correction = "y" ]; then
    ssh -p 9000 "$targetusername@$targetIP"
    break
  elif [ $correction = "n" ]; then
    echo " "
  else
    echo "Invalid input..."
  fi
done
