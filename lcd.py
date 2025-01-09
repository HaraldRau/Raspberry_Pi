#!/usr/bin/env python

import smbus
from time import sleep, strftime
from datetime import datetime
from RPLCD.i2c import CharLCD # sudo pip install RPLCD
lcd1602 = CharLCD('PCF8574',0x27)

def get_cpu_temp():
	# CPU Temperatur aus Datei lesen "/sys/class/thermal/thermal_zone0/temp"
	tmp = open('/sys/class/thermal/thermal_zone0/temp')
	cpu = tmp.read()
	tmp.close()
	return 'CPU: ' + '{:.2f}'.format( float(cpu)/1000 ) + ' C '

def get_time_now():
	# get system time
	return datetime.now().strftime('%H:%M')

def destroy():
	lcd1602.clear()

try:
	while(True):
		lcd1602.clear()
		lcd1602.cursor_pos = (0,0)
		lcd1602.write_string(get_cpu_temp() )
		lcd1602.cursor_pos = (1,0)
		lcd1602.write_string(get_time_now() )
		sleep(10)
except KeyboardInterrupt:
	destroy()
