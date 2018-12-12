#!/usr/bin/env python
# coding: utf-8

# In[8]:


import RPi.GPIO as GPIO

import time
import os

GPIO.setmode(GPIO.BCM) 

#set the mode of GPIO pin to BCM
TRIG = 23

ECHO = 24

print ("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT) 

#set trigger pin as output

GPIO.setup(ECHO,GPIO.IN)

#set echo pin as input pin

GPIO.output(TRIG, True)

 #Trigger pin is set High, and give the sensor a second to settle.

print ("Waiting For Sensor To Settle")
time.sleep(2)
while True:
	#to create trigger pulse, we set out trigger low for 10uS then set it high again.

	GPIO.output(TRIG, False) 
	time.sleep(0.00001)

	GPIO.output(TRIG, True)
	while GPIO.input(ECHO)==0:
        pulse_start = time.time()
        
        #The time.time() function will record the latest timestamp

	while GPIO.input(ECHO)==1:
        pulse_end = time.time() 
	   
    #Once a signal is received, the value changes 
	#from low (0) to high (1)	, 
	#and the signal will remain high
 	#for the duration of the echo pulse     
        pulse_duration = pulse_end - pulse_start

# calculating the difference between the two recorded timestamps
        distance = pulse_duration x 17150
        distance = round(distance, 2)

#rounding the distance to 2 decimal places
        print ("Distance:",distance,"cm")

#print the distance of the object from the sensor

if distance <= 20:
	print("object detected")
	os.system('fswebcam /home/pi/Pictures/%H%M%S.jpg')
    
    #capturing the image when the distance is <20cm
	print("image captured")
else:
	print("object  not detected")




# In[ ]:




