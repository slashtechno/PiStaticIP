#!/usr/bin/python3
import os
input("If you are running with sudo press control+c\nIf you are running without press enter")
os.system("cd ~")
interface=input("Are you using WiFi(Press 1) or Ethernet (Press 2)")
interface=int(interface)
print("\n\n\n")
if interface==1:
    result=os.system("ip route | grep wlan0")
    interface="wlan0"
if interface==2:
    os.system("ip route | grep eth0")
    interface="eth0"
str(result)
print("\nThe rest of the questions are referring to the two lines above")
via=input("\nIn the top line between \"via\" and \"dev\", what is the IP (number)?\n")
currentIP=input("In the bottom line, between \"src\" and \"metric\" what is theIP (number)?\n")
addition="interface "+interface+"\nstatic ip_address="+currentIP+"/24"+"\nstatic routers="+via
file=open("/etc/dhcpcd.conf", "a")
file.write("\n"+addition)
file.close