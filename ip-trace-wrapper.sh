#!/bin/bash

# 🎨 Colors
green='\e[1;32m'
blue='\e[1;34m'
yellow='\e[1;33m'
red='\e[1;31m'
cyan='\e[1;36m'
reset='\e[0m'

# 🎬 ASCII Banner
echo -e "${green}
 _ ____    _
(_)  _ \  | |_ _ __ __ _  ___ ___ _ __
| | |_) | | __| '__/ _\` |/ __/ _ \ '__|
| |  __/  | |_| | | (_| | (_|  __/ |
|_|_|      \__|_|  \__,_|\___\___|_|
${reset}"

echo -e "${yellow}
   }----------------------------------------{
}--------------- IP Information ---------------{
   }----------------------------------------{
${reset}"

# 🎯 Input
read -p "🔍 Target IP डालें: " target_ip

# 🌐 Fetch IP Info
response=$(curl -s "http://ip-api.com/json/$target_ip")

# 🧠 Parse & Display
country=$(echo $response | jq -r '.country')
region=$(echo $response | jq -r '.regionName')
city=$(echo $response | jq -r '.city')
timezone=$(echo $response | jq -r '.timezone')
isp=$(echo $response | jq -r '.isp')
org=$(echo $response | jq -r '.org')
lat=$(echo $response | jq -r '.lat')
lon=$(echo $response | jq -r '.lon')
asn=$(echo $response | jq -r '.as')
datetime=$(date +"%B %d, %Y, %I:%M %p")

# 🗣️ Hindi Narration
echo -e "${cyan}📢 जानकारी प्राप्त की जा रही है...${reset}"
sleep 1
echo -e "${blue}IP Address     >  $target_ip${reset}"
echo -e "${green}Country        >  $country${reset}"
echo -e "${green}Region         >  $region${reset}"
echo -e "${green}City           >  $city${reset}"
echo -e "${green}Time Zone      >  $timezone${reset}"
echo -e "${yellow}ISP            >  $isp${reset}"
echo -e "${yellow}Organization   >  $org${reset}"
echo -e "${red}ASN            >  $asn${reset}"
echo -e "${red}Location       >  $lat,$lon${reset}"
echo -e "${cyan}Date & Time    >  $datetime${reset}"

# 📁 Save to Log
mkdir -p logs
logfile="logs/ip_trace_$(date +%F_%H-%M-%S).txt"
echo "$response" > "$logfile"
echo -e "${blue}📁 Log saved to: $logfile${reset}"
