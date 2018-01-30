# Connector_Zeus

# ABOUT
This projects intention is to get information from the AP's with Zeus API on it. for now, we are able to collect data information from the device that are using API v1 and V3 (that is the only API versions that I have found on Intelbras products). 

I would like to mention that the bases of this project was provided from this link: https://medium.com/@sergiomarioq/intelbras-inicia-abertura-das-apis-de-seus-dispositivos-986f0a9a4e76 , and from that, I was able to make this project and help other people whitch whants to collect data from the Intelbras devices.

Just to clarify, this project was crated to work with some Router devices (like AP 310 and 360), and probably, will work with the other devices that uses Zeus API.

To use the Connector_Zeus, is simple, you just need to pass some parameters to fullfill the required arguments. Below, I will show you all informatio that you can collect from the device:

**Get Configured channel:** Connector_Zeus.py -m channel -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS};

**Get Clients connected:**  Connector_Zeus.py -m clients -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS};

**Get Download from ETH0 kbps:** Connector_Zeus.py -m downloadeth0 -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS};

**Get Download from WLAN0 kbps:** Connector_Zeus.py -m downloadwlan0 -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS};

**Get Upload from ETH0 kbps:** Connector_Zeus.py -m uploadeth0 -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS};

**Get Upload from WLAN0 kbps:** Connector_Zeus.py -m uploadwlan0 -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS};

**Get Device identification:** Connector_Zeus.py -m alias -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS};

**Get Operation mode:** Connector_Zeus.py -m opmode -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS};

**Get Device Model:** Connector_Zeus.py -m model -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS};

**Get Firmware Version:** Connector_Zeus.py -m version -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS};

**Get Device Uptim:** Connector_Zeus.py -m uptime -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS};

There is a important information tha you need to understand to be able to use this code on both API's Versions. To be able to use this project with API v3 devices, YOU NEED to pass as argument the version number, and that I will show you later, and other dargument with the interface that you whant to collect, like 5Ghz interface or 2Ghz.

By default, the version argument is already 2Ghz and and API V1.

Examples with Version 3 of API:



**Get Download from ETH0 kbps:** Connector_Zeus.py -m downloadeth0 -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS} -ver v3 -int 2Ghz;

**Get Download from WLAN0 kbps:** Connector_Zeus.py -m downloadwlan0 -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS} -ver v3 -int 2Ghz;;

**Get Upload from ETH0 kbps:** Connector_Zeus.py -m uploadeth0 -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS} -ver v3 -int 2Ghz;;

**Get Upload from WLAN0 kbps:** Connector_Zeus.py -m uploadwlan0 -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS} -ver v3 -int 2Ghz;;

**Get Device identification:** Connector_Zeus.py -m alias -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas  -ver v3 -int 2Ghz;

Obs: If the device has 5ghz interface, change the "-int 2Ghz" to "-int 5Ghz".

There is other get functions that you can use, but be becarefull, if you use, that maybe will disconnect all devices connected to your router device. This functions I only recomend touse if you need to analise your wireless environment.


**Get How much wireless network are in your environment:** Connector_Zeus.py -m surveycount -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS} -ver v3 -int 2Ghz;

**Get noise level from all wireless network in your environment:** Connector_Zeus.py -m noise -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS} -ver v3 -int 2Ghz;;

**Get noise level by channel from all wireless network in your environment:** Connector_Zeus.py -m noise_channel -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS} -ver v3 -int 2Ghz -ch 8;;

**Get noise level on the channel that the device is using:** Connector_Zeus.py -m noise_ownchannel -ip {HOST.CONN} -p {$HTTPS_PORT} -user {$LOGIN_USER} -pas {$LOGIN_PASS} -ver v3 -int 2Ghz;




