#!/bin/bash

while true; do
  echo "Input target username: "
  read targetusername
  echo "Input target IP (without port): "
  read targetIP
  echo "You inputed" $targetusername "as target username and " $targetIP "as target IP, correct? y/n :"
  read correction
  if [ correction = "y" ]; then
    "ssh -p 9000" $targetusername"@"$targetIP
    break
  elif [ correctionIP = "n" ]; then
    echo " "
  else
    echo "Invalid input..."
  fi
done
