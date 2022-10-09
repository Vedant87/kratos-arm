#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Joy

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

    elif data.axes[1] >= 0.8 :
      self.y = self.y-1


    elif data.axes[0] < 0 :
      self.x = self.x +1  

    elif data.axes[1] < 0 :
      self.y = self.y +1  
    
  def main(self):
    self.sub=rospy.Subscriber('joy',Joy,self.Joyst)
    rospy.spin()


if __name__ == '__main__' :
  Joystick().main()



