# lcd display program

Programs to display some data on an LCD display connected to a Raspberry Pi at bootup and
during operation.  Of interest are the date/time and the IP address.  The
hostname is also displayed.  I use 3 character hostnames for the two RPi comp0uters with an LCD display.

## showIP.py:

The main program

## getIP:

Program to read ifconfig and retrieve the IP address for the interface in
use.  You must edit the 4th and 8th fields to reflect either eth0 or wlan0.

## I2C_LCD_DRIVER.py

The driver file.  Look inside here to see how to install smbus and also how
to scan I2C buss looking for the LCD address.

## Install

Install smbus

Copy these files to a folder named lcd in pi's home folder.

To make this program start automatically, add this line:

/home/pi/lcd/showIP.py &

to /etc/rc.local just before the exit 0 command.
