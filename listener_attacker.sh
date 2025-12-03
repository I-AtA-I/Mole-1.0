#!/bin/bash
echo "This program will start a listener for a reverse ssh..."

while true; do
  echo "Input target username: "
  read targetusername
  echo "Input target IP (without port): "
  read targetIP
  clear
  echo "You inputed" $targetusername "as target username and " $targetIP "as target IP, correct? y/n :"
  read correction
  if [ $correction = "y" ]; then
    "ssh -p 9000" $targetusername"@"$targetIP
    break
  elif [ $correction = "n" ]; then
    echo " "
  else
    echo "Invalid input..."
  fi
done
