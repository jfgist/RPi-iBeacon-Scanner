RPi-iBeacon-Scanner
===================

The goal is to create a setup that will scan for iBeacons with a Raspberry Pi.  
This will probably use ibeacon_scan developed by Radius Networks and then piped into another script that 
will do something with the information.  That something is undefined right now. 

Requires 
* bc  (sudo apt-get bc)
* tweepy (sudo apt-get tweepy)
* 

The iBeacon that I am trying to detect is F9:8E:7F:50:CD:68

I don't need the range and stuff, just if it is in range so I may keep it simple and just look for the mac address.  
