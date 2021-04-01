#!/usr/bin/python3

import pathlib

import I2C_LCD_DRIVER
from datetime import datetime
from time import sleep
from subprocess import check_output
from subprocess import check_call

from gpiozero import Button

global host_name

def shutdown():
    print('Shutdown called')
    myLCD.lcd_display_string("System shutdown  ",2,0)
    check_call(['sudo', 'poweroff'])

myLCD = I2C_LCD_DRIVER.lcd()
myLCD.lcd_display_string("RPi starting!",1)

sleep(1)

myLCD.lcd_clear()

host_ip = str(check_output(['/home/pi/lcd/getIP','I']),'utf-8')
host_ip = host_ip.strip()
print(host_ip)

myLCD.lcd_display_string(host_ip,2,0)

shutdown_btn = Button(26, hold_time=5)
shutdown_btn.when_held = shutdown

pp = open('/etc/hostname','r')
host_name = pp.read().strip()
pp.close

print(host_name)
#print (len(host_name))

oldsec = datetime.now().second
oldmin = datetime.now().minute - 1

while(1):
#    global host_name
    while (oldsec == datetime.now().second):
        sleep(0.1)

    if oldmin != datetime.now().minute:

        oldmin = datetime.now().minute
        host_ip = str(check_output(['/home/pi/lcd/getIP','I']),'utf-8')
        host_ip = host_ip.strip()

        #myLCD.lcd_clear()
        myLCD.lcd_display_string("                ",2,0)
        sleep(0.1)
        myLCD.lcd_display_string(host_ip,2,0)
        myLCD.lcd_display_string(host_name,1,13)
   
    oldsec = datetime.now().second

    myDatetime = datetime.now().strftime("%H:%M:%S")
    myLCD.lcd_display_string(myDatetime,1,0)
    while (1):
        file = pathlib.Path("off")
        if file.exists ():
          myLCD.backlight(0)
        else:
          myLCD.backlight(1)


        
        
        