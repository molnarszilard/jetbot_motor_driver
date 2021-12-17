import time
import traitlets
from traitlets.config.configurable import SingletonConfigurable
import qwiic_scmd

class Robot2(SingletonConfigurable):

    def __init__(self, *args, **kwargs):
        self.R_MTR = 0
        self.L_MTR = 1
        self.FWD = 0
        self.BWD = 1
        self.myMotor = qwiic_scmd.QwiicScmd()
        if self.myMotor.connected == False:
            print("Motor Driver not connected. Check connections.", \
                file=sys.stderr)
            return
        self.myMotor.begin()
        print("Motor initialized.")
        time.sleep(.250)
        # Zero Motor Speeds
        self.myMotor.set_drive(0,0,0)
        self.myMotor.set_drive(1,0,0)

        self.myMotor.enable()
        print("Motor enabled")
        time.sleep(.250)
        
    def set_motors(self, left_speed, right_speed):
        if left_speed<2.1:
            left_speed*=125
        if left_speed>255:
            left_speed=255
        if right_speed<2.1:
            right_speed*=125
        if right_speed>255:
            right_speed=255
        self.myMotor.set_drive(self.R_MTR,self.FWD,right_speed)
        self.myMotor.set_drive(self.R_MTR,self.FWD,left_speed)
        time.sleep(.1)
        
    def forward(self, speed=1.0, duration=None):
        if speed<2.1:
            speed*=125
        if speed>255:
            speed=255
        self.myMotor.set_drive(self.R_MTR,self.FWD,speed)
        self.myMotor.set_drive(self.L_MTR,self.FWD,speed)

    def backward(self, speed=1.0):
        if speed<2.1:
            speed*=125
        if speed>255:
            speed=255
        self.myMotor.set_drive(self.R_MTR,self.BWD,speed)
        self.myMotor.set_drive(self.L_MTR,self.BWD,speed)

    def left(self, speed=1.0):
        if speed<2.1:
            speed*=125
        if speed>255:
            speed=255
        self.myMotor.set_drive(self.R_MTR,self.FWD,speed)
        self.myMotor.set_drive(self.L_MTR,self.BWD,speed)

    def right(self, speed=1.0):
        if speed<2.1:
            speed*=125
        if speed>255:
            speed=255
        self.myMotor.set_drive(self.R_MTR,self.BWD,speed)
        self.myMotor.set_drive(self.L_MTR,self.FWD,speed)

    def stop(self):
        speed=0
        self.myMotor.set_drive(self.R_MTR,self.BWD,speed)
        self.myMotor.set_drive(self.L_MTR,self.FWD,speed)
        
    def test(self):
#         while True:
        speed = 20
        for speed in range(20,255):
            print(speed)
            self.myMotor.set_drive(self.R_MTR,self.FWD,speed)
            self.myMotor.set_drive(self.L_MTR,self.FWD,speed)
            time.sleep(.05)
        for speed in range(254,20, -1):
            print(speed)
            self.myMotor.set_drive(self.R_MTR,self.FWD,speed)
            self.myMotor.set_drive(self.L_MTR,self.FWD,speed)
            time.sleep(.05)
            
    def disable(self):
        self.stop()
        print("Ending example.")
        self.myMotor.disable()