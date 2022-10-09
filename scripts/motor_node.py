#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Int8

class Motor():

    def __init__(self):
        rospy.init_node('motor',anonymous= True)
        self.master = 0
        self.pub = rospy.Publisher('chatter',Int8,queue_size=10)
        
    def valueassign(self,data):
        if data.axes[0] >= 0.8 :
            self.master = 1

        elif data.axes[0] < -0.8 :
            self.master =  -1      

        elif data.axes[1] >= 0.8 :
            self.master = 2

        elif data.axes[1] < -0.8:
            self.master = -2

        elif data.axes[3] >= 0.8 :
            self.master = 3

        elif data.axes[3] < -0.8:
            self.master = -3 
       
        elif data.axes[6] ==1:
            self.master = 6

        elif data.axes[6]==-1 :
            self.master = -6

        elif data.axes[7] ==1:
            self.master = 7

        elif data.axes[7]==-1 :
            self.master = -7 
        else:
            self.master = 0
        rospy.loginfo(self.master)
        self.pub.publish(self.master)
            
    def listener(self):
        self.sub=rospy.Subscriber('joy',Joy,self.valueassign)
        

    def motorpub(self):
        ##self.pub = rospy.Publisher('chatter',Int8,queue_size=10)
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            rospy.loginfo(self.master)
            self.pub.publish(self.master)
                

    def main(self):
        self.listener()
        rospy.spin()
        ##while not rospy.is_shutdown():
            #self.motorpub()
    
if __name__ == '__main__' :
    Motor().main()       



