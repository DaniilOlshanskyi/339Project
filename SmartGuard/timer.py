from gpiozero import MotionSensor
import time
from picamera import PiCamera
from datetime import datetime 



pir = MotionSensor(4)
name = "/home/pi/ISU/Photos/"

start_time=time.time()

while True:
    if (time.time()-start_time) > 10:
            start_time=time.time()            
            print("Taken!")
            camera = PiCamera()
            camera.capture("Photos/" + str(0) + ".png")
            camera.close()

