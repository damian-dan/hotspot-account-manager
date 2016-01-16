#!/usr/bin/env python
import printer, random, textwrap, string, os
from time import sleep
import RPi.GPIO as GPIO

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

def doPrinting():
    p=printer.ThermalPrinter(serialport="/dev/ttyAMA0")
    p.print_text("\nUsername: ")
    username = id_generator()
    p.print_text(username)
    p.print_text("\npassword: ")
    p.print_text(id_generator())
    os.system('/home/pi/hotspot-account-manager/bin/createUser.php {0} {1}'.format(username) format(password))

    #wrapped_text = textwrap.fill("Lorem")
    #p.print_text(wrapped_text)
    p.linefeed()

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)

print GPIO.getmode()
print("start box execution")
while True:
	if GPIO.input(27) == False:
		print("Printing")
		doPrinting()
		#os.system("/home/pi/try/py-thermal-printer/run.py")
		sleep(1)
print ("end box execution2")
GPIO.cleanup()
