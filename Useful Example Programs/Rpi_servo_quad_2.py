#!/usr/bin/env python

import rospy
import roslib
import sys

from geometry_msgs.msg import Twist

from Adafruit_PWM_Servo_Driver import PWM
import time
from Adafruit_ADS1x15 import ADS1x15
from Adafruit_BMP085 import BMP085

adc = ADS1x15(ic=0x00)
altimeter = BMP085(0x77)
pwm = PWM(0x40)

class Quad_listener:
    
    def __init__(self):

        global pwm
        pwm.setPWMFreq(50)
        
        self.manual_sub = rospy.Subscriber("/Quad_vel_manual", Twist, self.callback)
        self.sensor_pub = rospy.Publisher("/cloudrone_sensor", Twist, queue_size=1)

    def callback(self,data):
        try:
            Pitch = data.linear.x  #receving inputs from joystick
            Roll = data.linear.y
            Throttle = data.linear.z
            Yaw = data.angular.z

            Pitch = int(Pitch*41)
            Roll = int(Roll*41)
            Throttle = int(Throttle*41)
            Yaw = int(Yaw*41)

            pwm.setPWM(0, 0, Roll)     # channel 0 Roll
            pwm.setPWM(1, 0, Pitch)    # channel 1 Pitch
            pwm.setPWM(2, 0, Throttle) # channel 2 Throttle
            pwm.setPWM(3, 0, Yaw)      # channel 3 Yaw
    
            print "P :"+str(Pitch)+" R :"+str(Roll)+" Y :"+str(Yaw)+" T :"+str(Throttle)

            sensor_data = Twist()
            sensor_data.linear.x = adc.readADCSingleEnded(0, 4096, 250) * 0.004308094 
            sensor_data.linear.y = altimeter.readAltitude()
            sensor_data.linear.z = altimeter.readPressure()
            sensor_data.angular.x = altimeter.readTemperature()
            self.sensor_pub.publish(sensor_data)

        except:
            pass
    
if __name__ == '__main__':
    cloudrone = Quad_listener()
    rospy.init_node('Quad_listener',anonymous=True)
    rospy.spin()
