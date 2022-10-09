#!/usr/bin/env python3

import rospy
import math
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32

class Inv():
    def __init__(self):
        rospy.init_node('puthli',anonymous= True)
        self.a1 = 10
        self.a2 = 10
        self.x = 0
        self.y = 2
        self.theta1 = 0
        self.theta2 = 0
        self.k = 0.3
        self.a6 = 1
        self.i = 0.3
        self.a4 = 1
        self.h = math.pi/3
        self.theta6 = 0
        self.theta4 = 0
        self.l4 = 0
        self.l6 = 0
    
    def givexy(self,data):
        print("Callback")
        print(self.x,self.y)
        if data.axes[0] > 0.8 :
            self.x += 0.005

        elif data.axes[0] < -0.8 :
            self.x -= -0.005  

        if data.axes[1] > 0.8 :
            self.y += 0.005

        elif data.axes[1] < -0.8 :
            self.y -= -0.005 

        else:
            self.x +=0
            self.y +=0


    def calculatetheta2(self):
        try:
            self.theta2 = math.acos(((self.x)**2+(self.y)**2 -(self.a1)**2 -(self.a2)**2)/(2*(self.a1)*(self.a2)))
            return self.theta1
        except:
            # print("Domain error")
            pass

    def calculatetheta1(self):
        try :
            self.theta1 = math.atan(self.y/self.x) - math.atan(((self.a2)*math.sin(self.theta2))/(self.a1 +(self.a2)*(math.cos(self.theta2))))    
            return self.theta2
        except ZeroDivisionError:
            # print("Domain error")
            pass
                
    
    def Putin(self):
        self.pub1 = rospy.Publisher('putin',Float32,queue_size=10)
        self.pub = rospy.Publisher('modi',Float32,queue_size=10)
        while not rospy.is_shutdown():
            self.calculatel4()
            # rospy.loginfo(self.l4)
            self.pub1.publish(self.l4)
            self.calculatel6()
            # rospy.loginfo(self.l6)
            self.pub.publish(self.l6)
    
    
    def calculatet6(self):
        self.calculatetheta1()
        self.theta6 = math.pi - ((self.theta1)+(self.h))

    def calculatel6(self):
        self.calculatet6()
        self.l6 = math.sqrt((self.a6)**2+(self.k)**2 -2*(math.cos(self.theta6))*(self.a6)*(self.k))
        # print(self.l6)
    
    def calculatet4(self):
        self.calculatetheta2()
        self.theta4 = math.pi - self.theta2

    def calculatel4(self):
        self.calculatet4()
        self.l4 = math.sqrt((self.i)**2+(self.a4)**2-2*(math.cos(self.theta4)*(self.a4)*(self.i))) 
        # print(self.l4) 


    def main(self):
        self.sub=rospy.Subscriber('joy',Joy,self.givexy)
        while not rospy.is_shutdown():
            self.Putin()

if __name__ == '__main__' :
    Inv().main()