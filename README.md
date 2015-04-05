Demo Python script for Powertip PC1604A (16x4) character display

Completely based on http://www.rpiblog.com/2012/11/interfacing-16x2-lcd-with-raspberry-pi.html but fixed for 4 lines and GPIO cleanup

Don't forget to set your GPIO pins in "def __init__".

Pinout + 5k pot

PC1604				|  RPi
----------------------------------------------------------
pin 1 (GND)			-> GND 
pin 2 (VCC)			-> Potentiometer pin 3
pin 3 (Contrast Vo) 		-> Potentiometer pin 2
pin 4 (Register Select RS) 	-> GPIO 4 
pin 5 (R/W)			-> GND
pin 6 (Enable E)		-> GPIO 15

pin 7,8,9,10 not connected

pin 11 (IO 4)			-> GPIO 9
pin 12 (IO 5)			-> GPIO 11
pin 13 (IO 6)			-> GPIO 7
pin 14 (IO 7)			-> GPIO 8
pin 15 (VCC backlight)		-> Potentiometer pin 3
pin 16 (GND backlight)		-> GND


- Potentiometer pin 1 		-> GND
- Potentiometer pin 3 		-> 5V

![Powertip PC1604A](https://raw.githubusercontent.com/glorang/Powertip-PC1604A/master/Powertip-PC1604A.jpg)
