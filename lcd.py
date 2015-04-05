#!/usr/bin/python  
  
import RPi.GPIO as GPIO  
import os, time, signal, sys
from time import localtime, strftime, sleep
from datetime import datetime, timedelta

class HD44780:  
  
    def __init__(self, pin_rs=4, pin_e=15, pins_db=[9, 11, 7, 8]):  
  
        self.pin_rs=pin_rs  
        self.pin_e=pin_e  
        self.pins_db=pins_db  
  
        GPIO.setmode(GPIO.BCM)  
        GPIO.setup(self.pin_e, GPIO.OUT)  
        GPIO.setup(self.pin_rs, GPIO.OUT)  
        for pin in self.pins_db:  
            GPIO.setup(pin, GPIO.OUT)  
  
        self.clear()  
  
    def clear(self):  
        """ Blank / Reset LCD """  
  
        self.cmd(0x33) # $33 8-bit mode  
        self.cmd(0x32) # $32 8-bit mode  
        self.cmd(0x28) # $28 8-bit mode  
        self.cmd(0x0C) # $0C 8-bit mode  
        self.cmd(0x06) # $06 8-bit mode  
        self.cmd(0x01) # $01 8-bit mode  
  
    def cmd(self, bits, char_mode=False):  
        """ Send command to LCD """  
  
        sleep(0.001)  
        bits=bin(bits)[2:].zfill(8)  
  
        GPIO.output(self.pin_rs, char_mode)  
  
        for pin in self.pins_db:  
            GPIO.output(pin, False)  
  
        for i in range(4):  
            if bits[i] == "1":  
                GPIO.output(self.pins_db[::-1][i], True)  
  
        GPIO.output(self.pin_e, True)  
        GPIO.output(self.pin_e, False)  
  
        for pin in self.pins_db:  
            GPIO.output(pin, False)  
  
        for i in range(4,8):  
            if bits[i] == "1":  
                GPIO.output(self.pins_db[::-1][i-4], True)  
  
  
        GPIO.output(self.pin_e, True)  
        GPIO.output(self.pin_e, False)  
  
    def message(self, text, line):  

	if line == 1:
		self.cmd(0x80)
	elif line == 2:
		self.cmd(0xC0)
	elif line == 3:
		self.cmd(0x90)
	elif line == 4:
		self.cmd(0xD0)

        for char in text:
            	self.cmd(ord(char),True)  
  
if __name__ == '__main__':  

    def signal_handler(signal, frame):
        GPIO.cleanup()
        sys.exit(0)

    lcd = HD44780()  
    signal.signal(signal.SIGINT, signal_handler)
    while True:

	# Print date on first line
    	lcd.message(strftime("%a, %d %b %Y", time.localtime()), 1)

    	# Print time on second line
	lcd.message(strftime("Time: %H:%M:%S", time.localtime()), 2)
 
	# Print load average on third line
	loadavg = os.getloadavg()
	strload = ' '.join( ('%.2f' % e) for e in loadavg)
	lcd.message("Load: " + strload, 3)

	# Print uptime on 4th line
	with open('/proc/uptime', 'r') as f:
		uptime_seconds = float(f.readline().split()[0])
		uptime = timedelta(seconds = uptime_seconds)
		d = datetime(1,1,1) + uptime
		uptime_string = "%dd%dh%dm%ds" % (d.day-1, d.hour, d.minute, d.second)
		lcd.message("Up: " + uptime_string, 4)

        sleep(1)

