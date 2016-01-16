#!/usr/bin/env python
import printer, random, textwrap, string, os, time
import RPi.GPIO as GPIO

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

def doPrinting():
    p=printer.ThermalPrinter(serialport="/dev/ttyAMA0")
    p.print_text("\nUsername: ")
    username = id_generator()
    p.print_text(username)
    p.print_text("\npassword: ")
    password = id_generator()
    p.print_text(password)
    os.system('/home/pi/hotspot-account-manager/bin/createUser.php '+format(username)+' '+format(password))

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
		time.sleep(1)
	time.sleep(0.000002)
print ("end box execution2")
GPIO.cleanup()
