#!/bin/bash
#version 1.0

clear
# Variables
b='\033[1m'
u='\033[4m'
bl='\E[30m'
r='\E[31m'
g='\E[32m'
bu='\E[34m'
m='\E[35m'
c='\E[36m'
w='\E[37m'
endc='\E[0m'
enda='\033[0m'
blue='\e[1;34m'
cyan='\e[1;36m'
red='\e[1;31m'

cowsay -f eyes "zombie" | lolcat
figlet -f slant "zombie" | lolcat
echo "    <=====================[]====================>" | lolcat
echo "    <=====[          Tool by ZomBie         ]=====>" | lolcat
echo  "    <=====[  Concact Me : +6283821185782  ]=====>" | lolcat
echo "    <=====================[]====================>" | lolcat

sleep 1

###################################################
# CTRL + C
###################################################
trap ctrl_c INT
ctrl_c() {
clear
clear
sleep 1
exit
}


lagi=1
while [ $lagi -lt 6 ];
do
echo ""
echo -e $b "1. Password TXT${enda}";
echo -e $b "2. Proxy TXT${enda}";
echo -e $b "3. Langsung Crack${enda}";
echo -e $b "00. Exit${enda}";
read -p "Pilih Nomernya =>" pil;

case $pil in
1) nano password.txt
echo

;;
2) nano abcd.txt
echo

;;
3) python ua.py

;;

00) sh zombie.sh
;;

*) echo "Pilih Sesuai List BangPey87"
esac
done
done
