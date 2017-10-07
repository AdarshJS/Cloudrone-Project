#!/usr/bin/env python

import roslib
import rospy

import sys
import time
import cv2
import numpy as np

import pygame

from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Twist

from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *

from cloudrone_template_final import Ui_Form

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Form()
ui.setupUi(window)

pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()

joystick_1 = pygame.joystick.Joystick(0)
joystick_1.init()

joystick_2 = pygame.joystick.Joystick(1)
joystick_2.init()

joystick_3 = pygame.joystick.Joystick(2)
joystick_3.init()

Attitude_bg_1 = cv2.imread("/home/aj/catkin_ws/src/beginner_tutorials/scripts/cloudrone/Horizon_Background.png",-1)
Attitude_bg_1 = cv2.cvtColor(Attitude_bg_1, cv2.COLOR_BGRA2RGBA)
Attitude_bg_2 = Attitude_bg_1.copy()
Attitude_bg_3 = Attitude_bg_1.copy()

Grnd_sky_1 = cv2.imread("/home/aj/catkin_ws/src/beginner_tutorials/scripts/cloudrone/Horizon_GroundSky.png",-1)
Grnd_sky_1 = cv2.cvtColor(Grnd_sky_1, cv2.COLOR_BGR2RGB)
Grnd_sky_2 = Grnd_sky_1.copy()
Grnd_sky_3 = Grnd_sky_1.copy()

Needle_1 = cv2.imread("/home/aj/catkin_ws/src/beginner_tutorials/scripts/cloudrone/Maquette_Avion.png", -1)
Needle_1 = cv2.cvtColor(Needle_1, cv2.COLOR_BGRA2RGBA)
Needle_2 = Needle_1.copy()
Needle_3 = Needle_1.copy()

Turn_bg_1 = cv2.imread("/home/aj/catkin_ws/src/beginner_tutorials/scripts/cloudrone/Turn_Background.png")
Turn_bg_1 = cv2.cvtColor(Turn_bg_1, cv2.COLOR_BGR2RGB)
Turn_bg_2 = Turn_bg_1.copy()
Turn_bg_3 = Turn_bg_1.copy()

Turn_bg_copy_1 = Turn_bg_1.copy()
Turn_bg_copy_2 = Turn_bg_1.copy()
Turn_bg_copy_3 = Turn_bg_1.copy()

Ball_1 = cv2.imread("/home/aj/catkin_ws/src/beginner_tutorials/scripts/cloudrone/TurnCoordinatorBall.png", -1)
Ball_2 = Ball_1.copy()
Ball_3 = Ball_1.copy()
               
Pitch_value_1 = Roll_value_1 = Yaw_value_1 = Throttle_value_1 = 0
Pitch_value_2 = Roll_value_2 = Yaw_value_2 = Throttle_value_2 = 0
Pitch_value_3 = Roll_value_3 = Yaw_value_3 = Throttle_value_3 = 0

Altitude_1 = Temperature_1 = Pressure_1 = Voltage_1 = 4.56
Altitude_2 = Temperature_2 = Pressure_2 = Voltage_2 = 4.56
Altitude_3 = Temperature_3 = Pressure_3 = Voltage_3 = 4.56

flag = 0

class Ros_Controller:
    def __init__(self):
        self.sub_sensor_1 = rospy.Subscriber("/cloudrone_sensor_1",Twist, self.callback_sensor_1, queue_size = 1)
        self.pub_speed_1 = rospy.Publisher('/Quad_vel_manual_1', Twist, queue_size=1)

        self.sub_sensor_2 = rospy.Subscriber("/cloudrone_sensor_2",Twist, self.callback_sensor_2, queue_size = 1)
        self.pub_speed_2 = rospy.Publisher('/Quad_vel_manual_2', Twist, queue_size=1)

        self.sub_sensor_3 = rospy.Subscriber("/cloudrone_sensor_3",Twist, self.callback_sensor_3, queue_size = 1)
        self.pub_speed_3 = rospy.Publisher('/Quad_vel_manual_3', Twist, queue_size=1)
    
    def callback_sensor_1(self,ros_data):
        global Altitude_1, Temperature_1, Pressure_1, Voltage_1
        Altitude_1 = ros_data.linear.x
        Temperature_1 = ros_data.linear.y
        Pressure_1 = ros_data.linear.z
        Voltage_1 = ros_data.angular.x

    def callback_sensor_2(self,ros_data):
        global Altitude_2, Temperature_2, Pressure_2, Voltage_2
        Altitude_2 = ros_data.linear.x
        Temperature_2 = ros_data.linear.y
        Pressure_2 = ros_data.linear.z
        Voltage_2 = ros_data.angular.x

    def callback_sensor_3(self,ros_data):
        global Altitude_3, Temperature_3, Pressure_3, Voltage_3
        Altitude_3 = ros_data.linear.x
        Temperature_3 = ros_data.linear.y
        Pressure_3 = ros_data.linear.z
        Voltage_3 = ros_data.angular.x
                     
def Throttle_1():
    global Throttle_value_1
    pygame.event.get()
    Throttle_value_1 = Throttle_value_1 + 1*(joystick_1.get_button( 3 ))
    Throttle_value_1 = Throttle_value_1 - 1*(joystick_1.get_button( 0 ))
    if Throttle_value_1 > 85:  Throttle_value_1 = 85
    if Throttle_value_1 < 0:   Throttle_value_1 = 0
    ui.Throttle_bar_1.setValue(Throttle_value_1)

def Throttle_2():
    global Throttle_value_2
    pygame.event.get()
    Throttle_value_2 = Throttle_value_2 + 1*(joystick_2.get_button( 3 ))
    Throttle_value_2 = Throttle_value_2 - 1*(joystick_2.get_button( 0 ))
    if Throttle_value_2 > 85:  Throttle_value_2 = 85
    if Throttle_value_2 < 0:   Throttle_value_2 = 0
    ui.Throttle_bar_2.setValue(Throttle_value_2)

def Throttle_3():
    global Throttle_value_3
    pygame.event.get()
    Throttle_value_3 = Throttle_value_3 + 1*(joystick_3.get_button( 3 ))
    Throttle_value_3 = Throttle_value_3 - 1*(joystick_3.get_button( 0 ))
    if Throttle_value_3 > 85:  Throttle_value_3 = 85
    if Throttle_value_3 < 0:   Throttle_value_3 = 0
    ui.Throttle_bar_3.setValue(Throttle_value_3)

def Attitude_display_1():
    pygame.event.get()
    global Needle_1,Attitude_bg_1,Grnd_sky_1,Pitch_value_1,Roll_value_1
    Pitch_value_1 = float("{:>6.3f}".format(joystick_1.get_axis( 1 )))
    Pitch_value_1 = Pitch_value_1 * (-40)
    Roll_value_1 = float("{:>6.3f}".format(joystick_1.get_axis( 0 )))
    Roll_value_1 = Roll_value_1 * (-20)
    
    Sky = Grnd_sky_1[Pitch_value_1+197:Pitch_value_1+197+210,0:210].copy()
    for c in range(0,3):
        Sky[0:210,0:210, c] = Attitude_bg_1[:,:,c] * (Attitude_bg_1[:,:,3]/255.0) +  Sky[0:0+210, 0:210, c] * (1.0 - Attitude_bg_1[:,:,3]/255.0)
    
    M = cv2.getRotationMatrix2D((210/2,210/2),Roll_value_1,1)
    Mark = cv2.warpAffine(Needle_1,M,(210,210))
    for c in range(0,3):
        Sky[0:210,0:210, c] = Mark[:,:,c] * (Mark[:,:,3]/255.0) +  Sky[0:210, 0:210, c] * (1.0 - Mark[:,:,3]/255.0)
    ui.Attitude_image_1.setPixmap(QPixmap(QtGui.QImage(Sky,Sky.shape[1],Sky.shape[0],Sky.strides[0],QtGui.QImage.Format_RGB888)))
    window.show()
    cv2.waitKey(1)

def Attitude_display_2():
    pygame.event.get()
    global Needle_2,Attitude_bg_2,Grnd_sky_2,Pitch_value_2,Roll_value_2
    Pitch_value_2 = float("{:>6.3f}".format(joystick_2.get_axis( 1 )))
    Pitch_value_2 = Pitch_value_2 * (-40)
    Roll_value_2 = float("{:>6.3f}".format(joystick_2.get_axis( 0 )))
    Roll_value_2 = Roll_value_2 * (-20)
    
    Sky = Grnd_sky_2[Pitch_value_2+197:Pitch_value_2+197+210,0:210].copy()
    for c in range(0,3):
        Sky[0:210,0:210, c] = Attitude_bg_2[:,:,c] * (Attitude_bg_2[:,:,3]/255.0) +  Sky[0:0+210, 0:210, c] * (1.0 - Attitude_bg_2[:,:,3]/255.0)
    
    M = cv2.getRotationMatrix2D((210/2,210/2),Roll_value_2,1)
    Mark = cv2.warpAffine(Needle_2,M,(210,210))
    for c in range(0,3):
        Sky[0:210,0:210, c] = Mark[:,:,c] * (Mark[:,:,3]/255.0) +  Sky[0:210, 0:210, c] * (1.0 - Mark[:,:,3]/255.0)
    ui.Attitude_image_2.setPixmap(QPixmap(QtGui.QImage(Sky,Sky.shape[1],Sky.shape[0],Sky.strides[0],QtGui.QImage.Format_RGB888)))
    window.show()
    cv2.waitKey(1)

def Attitude_display_3():
    pygame.event.get()
    global Needle_3,Attitude_bg_3,Grnd_sky_3,Pitch_value_3,Roll_value_3
    Pitch_value_3 = float("{:>6.3f}".format(joystick_3.get_axis( 1 )))
    Pitch_value_3 = Pitch_value_3 * (-40)
    Roll_value_3 = float("{:>6.3f}".format(joystick_3.get_axis( 0 )))
    Roll_value_3 = Roll_value_3 * (-20)
    
    Sky = Grnd_sky_3[Pitch_value_3+197:Pitch_value_3+197+210,0:210].copy()
    for c in range(0,3):
        Sky[0:210,0:210, c] = Attitude_bg_3[:,:,c] * (Attitude_bg_3[:,:,3]/255.0) +  Sky[0:0+210, 0:210, c] * (1.0 - Attitude_bg_3[:,:,3]/255.0)
    
    M = cv2.getRotationMatrix2D((210/2,210/2),Roll_value_3,1)
    Mark = cv2.warpAffine(Needle_3,M,(210,210))
    for c in range(0,3):
        Sky[0:210,0:210, c] = Mark[:,:,c] * (Mark[:,:,3]/255.0) +  Sky[0:210, 0:210, c] * (1.0 - Mark[:,:,3]/255.0)
    ui.Attitude_image_3.setPixmap(QPixmap(QtGui.QImage(Sky,Sky.shape[1],Sky.shape[0],Sky.strides[0],QtGui.QImage.Format_RGB888)))
    window.show()
    cv2.waitKey(1)

def Turn_display_1():
    pygame.event.get()
    global Turn_bg_1,Ball_1, Yaw_value_1                    
    Yaw_value_1 = float("{:>6.3f}".format(joystick_1.get_axis( 2 ))) - float("{:>6.3f}".format(joystick_1.get_axis( 5 )))
    Yaw_value_1 = Yaw_value_1*(-25)
    for c in range(0,3):
        Turn_bg_1[19:19+14, 98+Yaw_value_1:98+Yaw_value_1+14, c] =  Ball_1[:,:,c] * (Ball_1[:,:,3]/255.0) +  Turn_bg_1[19:19+14, 98+Yaw_value_1:98+Yaw_value_1+14, c] * (1.0 - Ball_1[:,:,3]/255.0)
    ui.Turn_image_1.setPixmap(QPixmap(QtGui.QImage(Turn_bg_1,Turn_bg_1.shape[1],Turn_bg_1.shape[0],Turn_bg_1.strides[0],QtGui.QImage.Format_RGB888)))
    window.show()
    cv2.waitKey(1)
    Turn_bg_1 = Turn_bg_copy_1.copy()

def Turn_display_2():
    pygame.event.get()
    global Turn_bg_2,Ball_2, Yaw_value_2                    
    Yaw_value_2 = float("{:>6.3f}".format(joystick_2.get_axis( 2 ))) - float("{:>6.3f}".format(joystick_2.get_axis( 5 )))
    Yaw_value_2 = Yaw_value_2*(-25)
    for c in range(0,3):
        Turn_bg_2[19:19+14, 98+Yaw_value_2:98+Yaw_value_2+14, c] =  Ball_2[:,:,c] * (Ball_2[:,:,3]/255.0) +  Turn_bg_2[19:19+14, 98+Yaw_value_2:98+Yaw_value_2+14, c] * (1.0 - Ball_2[:,:,3]/255.0)
    ui.Turn_image_2.setPixmap(QPixmap(QtGui.QImage(Turn_bg_2,Turn_bg_2.shape[1],Turn_bg_2.shape[0],Turn_bg_2.strides[0],QtGui.QImage.Format_RGB888)))
    window.show()
    cv2.waitKey(1)
    Turn_bg_2 = Turn_bg_copy_2.copy()

def Turn_display_3():
    pygame.event.get()
    global Turn_bg_3,Ball_3, Yaw_value_3                    
    Yaw_value_3 = float("{:>6.3f}".format(joystick_3.get_axis( 2 ))) - float("{:>6.3f}".format(joystick_3.get_axis( 5 )))
    Yaw_value_3 = Yaw_value_3*(-25)
    for c in range(0,3):
        Turn_bg_3[19:19+14, 98+Yaw_value_3:98+Yaw_value_3+14, c] =  Ball_3[:,:,c] * (Ball_3[:,:,3]/255.0) +  Turn_bg_3[19:19+14, 98+Yaw_value_3:98+Yaw_value_3+14, c] * (1.0 - Ball_3[:,:,3]/255.0)
    ui.Turn_image_3.setPixmap(QPixmap(QtGui.QImage(Turn_bg_3,Turn_bg_3.shape[1],Turn_bg_3.shape[0],Turn_bg_3.strides[0],QtGui.QImage.Format_RGB888)))
    window.show()
    cv2.waitKey(1)
    Turn_bg_3 = Turn_bg_copy_3.copy()

def Hover_function_1():
    pygame.event.get()
    global Hover_value_1, Hover_value_2
    Hover_value_1 = joystick.get_button(1)
    Hover_value_2 = joystick.get_button(2)

def Sensor_display_1():
    global Altitude_1, Temperature_1, Pressure_1, Voltage_1
    ui.Altitude_LCD_1.display(Altitude_1)
    ui.Temperature_LCD_1.display(Temperature_1)
    ui.Pressure_LCD_1.display(Pressure_1)
    ui.Voltage_LCD_1.display(Voltage_1)
    Battery_1 = Voltage_1*7.9365
    if Battery_1 > 100:
        Battery_1 = 100
    if Battery_1 < 0:
        Battery_1 = 0
    ui.Battery_bar_1.setValue(Battery_1)

def Sensor_display_2():
    global Altitude_2, Temperature_2, Pressure_2, Voltage_2
    ui.Altitude_LCD_2.display(Altitude_2)
    ui.Temperature_LCD_2.display(Temperature_2)
    ui.Pressure_LCD_2.display(Pressure_2)
    ui.Voltage_LCD_2.display(Voltage_2)
    Battery_2 = Voltage_2*7.9365
    if Battery_2 > 100:
        Battery_2 = 100
    if Battery_2 < 0:
        Battery_2 = 0
    ui.Battery_bar_2.setValue(Battery_2)

def Sensor_display_3():
    global Altitude_3, Temperature_3, Pressure_3, Voltage_3
    ui.Altitude_LCD_3.display(Altitude_3)
    ui.Temperature_LCD_3.display(Temperature_3)
    ui.Pressure_LCD_3.display(Pressure_3)
    ui.Voltage_LCD_3.display(Voltage_3)
    Battery_3 = Voltage_3*7.9365
    if Battery_3 > 100:
        Battery_3 = 100
    if Battery_3 < 0:
        Battery_3 = 0
    ui.Battery_bar_3.setValue(Battery_3)
    
def Publish_1():
    global Pitch_value_1, Roll_value_1, Throttle_value_1, Yaw_value_1, ic
    Pitch_value_1 = Pitch_value_1*(-0.022162) + 8.251953000  #(8.255411)#Pitch_value_1*(-0.0205) + 7.5
    Roll_value_1 =  Roll_value_1*(-0.022162*2) + 8.251953000 #8.255411#(8.288654-0.022162*1.5) #Roll_value_1*(-0.0410) + 7.5
    Yaw_value_1 = (-Yaw_value_1 + 50)*0.022162*2 + 6.041358  #6.218654
    power_1 = (0.043174*Throttle_value_1)+6.33021            #(Throttle_value_1 * 0.04) + 5.7
    cmd = Twist()
    cmd.linear.x = Pitch_value_1
    cmd.linear.y = Roll_value_1
    cmd.linear.z = power_1
    cmd.angular.z = Yaw_value_1
    ic.pub_speed_1.publish(cmd)

def Publish_2():
    global Pitch_value_2, Roll_value_2, Throttle_value_2, Yaw_value_2, ic
    Pitch_value_2 = Pitch_value_2*(-0.022162) + 8.251953000  #(8.255411)#Pitch_value_1*(-0.0205) + 7.5
    Roll_value_2 =  Roll_value_2*(-0.022162*2) + 8.251953000 #8.255411#(8.288654-0.022162*1.5) #Roll_value_1*(-0.0410) + 7.5
    Yaw_value_2 = (-Yaw_value_2 + 50)*0.022162*2 + 6.041358  #6.218654
    power_2 = (0.043174*Throttle_value_2)+6.33021            #(Throttle_value_1 * 0.04) + 5.7
    cmd = Twist()
    cmd.linear.x = Pitch_value_2
    cmd.linear.y = Roll_value_2
    cmd.linear.z = power_2
    cmd.angular.z = Yaw_value_2
    ic.pub_speed_2.publish(cmd)

def Publish_3():
    global Pitch_value_3, Roll_value_3, Throttle_value_3, Yaw_value_3, ic
    Pitch_value_3 = Pitch_value_3*(-0.022162) + 8.251953000  #(8.255411)#Pitch_value_1*(-0.0205) + 7.5
    Roll_value_3 =  Roll_value_3*(-0.022162*2) + 8.251953000 #8.255411#(8.288654-0.022162*1.5) #Roll_value_1*(-0.0410) + 7.5
    Yaw_value_3 = (-Yaw_value_3 + 50)*0.022162*2 + 6.041358  #6.218654
    power_3 = (0.043174*Throttle_value_3)+6.33021            #(Throttle_value_1 * 0.04) + 5.7
    cmd = Twist()
    cmd.linear.x = Pitch_value_3
    cmd.linear.y = Roll_value_3
    cmd.linear.z = power_3
    cmd.angular.z = Yaw_value_3
    ic.pub_speed_3.publish(cmd)

def exit_prog():
    global flag
    flag ==1
    rospy.signal_shutdown("Exit Pressed")
    cv2.destroyAllWindows()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    ic = Ros_Controller()
    rospy.init_node('QUADCOP', anonymous=True)
    while flag == 0:
        ui.button_1.clicked.connect(exit_prog)
        rate = rospy.Rate(60)

        Attitude_display_1()
        Attitude_display_2()
        Attitude_display_3()
        
        Turn_display_1()
        Turn_display_2()
        Turn_display_3()
        
        Throttle_1()
        Throttle_2()
        Throttle_3()
        
        Sensor_display_1()
        Sensor_display_2()
        Sensor_display_3()
        
        Publish_1()
        Publish_2()
        Publish_3()

        rate.sleep()
  
#Pitch_value_1 =Pitch_value_1*(-0.089255401/2) +7.1604320995
#Roll_value_1 =  Roll_value_1*(-0.089255401) + 7.16043209950 
#Yaw_value_1 = Yaw_value_1*(-0.032175)+7.1687552510000 
#power_1 = (Throttle_value_1 * 0.04) + 5.30        
        

    
