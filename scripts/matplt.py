#!/usr/bin/env python3



import rospy
from sensor_msgs.msg import Joy
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle



class Joystick():
    def __init__(self):
        rospy.init_node('listener',anonymous= True)
        self.x=0
        self.y=0
        print("Init finished")


    def Joyst(self,data):
        # rospy.loginfo(data.axes[0])
        # rospy.loginfo(data.buttons[0])
        
        
        print(self.x)
        print(self.y)
        if data.axes[0] >= 0.8 :
            self.x=self.x-1

        elif data.axes[0] < -0.8 :
            self.x = self.x +1  

        if data.axes[1] >= 0.8 :
            self.y = self.y-1

        elif data.axes[1] < -0.8 :
            self.y = self.y +1 

    def plotter(self):
        rect1 = Rectangle((self.x,self.y), 1, 1, color='yellow')
        plt.gca().add_patch(rect1)
        plt.plot(self.x,self.y,'o')
        plt.pause(0.01)
        

    ##def updateplt(self):
       ####

        

    def main(self):
        self.sub=rospy.Subscriber('joy',Joy,self.Joyst)
        while not rospy.is_shutdown():
            self.plotter()
    
        

if __name__=="__main__":
    Joystick().main()
    #r = Joystick()
    #r.plotter(r,r.x,r.y)
    
         
    