while true; do
  echo "Input target username: "
  read targetusername
  echo "You inputed" $targetusername "as target username, correct? y/n :"
  read correctionuser
  if [ correctionuser = "n"]; then
    
  
  if [ correctionuser = "y" ]; then
    while true; do
      echo "Input target IP (without port): "
      read targetIP
      echo "You inputed" $targetIP "as target IP, correct? y/n :"
      read correctionIP
      if [ correctionIP = "y" ]; then
        "ssh -p 9000" $targetusername"@"$targetip
      elif [ correctionIP = "n" ]; then
        echo " "
      else
        echo "Invalid input..."
      fi
  else
