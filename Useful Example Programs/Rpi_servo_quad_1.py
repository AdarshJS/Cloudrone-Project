#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from Adafruit_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x40)

def callback(data):
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

def listener():

    rospy.init_node('Quad_listener', anonymous=True)

    pwm.setPWMFreq(50)
    
    rospy.Subscriber("/Quad_vel_manual_1", Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
