from gpiozero import MotionSensor
import time
from picamera import PiCamera
from datetime import datetime 


pir = MotionSensor(4)
i = 0
name = "/home/pi/ISU/Photos/"

while True:
    i+=1
    if i>10:
            i=1
    pir.wait_for_motion()
    print("Motion detected!")
    camera = PiCamera()
    camera.capture("Photos/" + str(i) + ".png")
    camera.close()
    time.sleep(3)

