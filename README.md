# PiStaticIP
Python script that sets a static/reserved IP for Raspberry Pi

### To install:
`wget -qO- https://raw.githubusercontent.com/slashtechno/PiStaticIP/main/install | bash`

### To run
`staticIP`

### To Update (I recommend doing this frequently)
`https://raw.githubusercontent.com/slashtechno/PiStaticIP/main/update | bash` 

### To Uninstall  
`https://raw.githubusercontent.com/slashtechno/PiStaticIP/main/uninstall | bash` 


### How this works

1. Asks user if they are using WiFi or Ethernet  

2. Executes a command that shows current IP info. 

3. Asks user for what the command output was 

4. Adds static IP info to `/etc/dhcpcd.conf` 
