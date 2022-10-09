#!/usr/bin/env python3
import rospy
import math
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32
from geometry_msgs.msg import Point

class Russia():
    def __init__(self) :
        rospy.init_node('cyka',anonymous=True)
        self.x = 80
        self.y = 0
        self.a6 = 35.0 
        self.a4 = 36.5
        self.k6 = 19.50
        self.q6 = 0
        self.k4 = 7.5
        self.h6 = 1.50
        self.h4 =4.0
        self.q4 = 0
        self.l4 = 36.00
        self.l6 = 31.00
        self.f = 38.0
        self.LL6 = self.l6 + self.h6 + self.k4
        self.LL4 = self.l4 + self.h4
        self.t4 = 0
        self.t6 = 0

    def givxy(self,data):
        
        if data.axes[0] > 0.8 :
            self.x += 0.001
            self.y += 0

        elif data.axes[0] < -0.8 :
            self.x -= -0.001  
            self.y += 0

        if data.axes[1] > 0.8 :
            self.y += 0.001
            self.x += 0

        elif data.axes[1] < -0.8 :
            self.y -= -0.001 
            self.x += 0

        else:
            self.x +=0
            self.y +=0
        self.x=62.8
        self.y=7

        self.Stalin()

    def calculateq4(self):
        try :   
            self.q4 = math.acos(((self.x)**2+(self.y)**2 - (self.LL6)**2 - (self.LL4)**2)/(2*(self.LL4)*(self.LL6)))
            return self.q4
        except ZeroDivisionError:
            pass    

    def calculateq6(self):
        try:
            self.q6 = math.atan(self.y/self.x) + math.atan(((self.LL4)*math.sin(self.q4))/(self.LL6 +(self.LL4)*(math.cos(self.q4))))    
            return self.q6
        except ZeroDivisionError:
            pass    


##Stalin is publisher function and famine and cummunism are topics
    def Stalin(self):
        self.pub = rospy.Publisher('a4',Float32,queue_size=10)
        self.pub1 = rospy.Publisher('a6',Float32,queue_size=10)
        self.calculatea4()
        self.pub1.publish(self.a4)
        self.calculatea6()
        self.pub.publish(self.a6)
    
    def calculatet6(self):
        self.calculateq6()
        self.t6 = math.pi-self.q6-math.radians(self.f)

    def calculatet4(self):
        self.calculateq4()
        self.t4  = math.pi - (self.q4)
    
    def calculatea6(self):
        self.calculatet6()
        self.a6 = math.sqrt(((self.k6*self.k6)+(self.l6*self.l6))-(2*math.cos(self.t6)*(self.l6)*(self.k6)))

    def calculatea4(self):
        self.calculatet4()
        self.a4 = math.sqrt(((self.k4*self.k4)+(self.l4*self.l4))-(2*(math.cos(self.t4)*(self.l4)*(self.k4))))

    def main(self):
        self.sub=rospy.Subscriber('joy',Joy,self.givxy)
        rospy.spin()
        

if __name__ == '__main__' :
    obj = Russia()
    obj.main()


