# lcd display program

Programs to display some data connected to a Raspberry Pi at bootup and
during operation.  Of interest are the date/time and the IP address.  The
hostname is also displayed.

## showIP.py:

The main program

## getIP:

Program to rea ifconfig and retrieve the IP address for the interface in
use.  You must edit the 4th and 8th fields to reflect either eth0 or wlan0.

## I2C_LCD_DRIVER.py

The driver file.  Look inside here to see how to install smbus and also how
to scan I2C buss looking for the LCD address.


