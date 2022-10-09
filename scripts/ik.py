from cmath import pi, sqrt
import math 

class Inverse() :

    def __init__(self):
        self.a1 = 6
        self.a2 = 4
        self.x = 0.4
        self.y = 2
        self.theta1 = 0
        self.theta2 = 0
        self.k = 0.3
        self.a6 = 1
        self.i = 0.3
        self.a4 = 1
        self.h = pi/3
        self.theta6 = 0
        self.theta4 = 0
        self.l4 = 0
        self.l6 = 0
        

    def radianstodegree(self) :
        self.deg = self.radians*(180/pi)

    def calculatetheta2(self):
        self.theta2 = math.acos(((self.x)**2+(self.y)**2 -(self.a1)**2 -(self.a2)**2)/(2*(self.a1)*(self.a2)))
        return self.theta1

    def calculatetheta1(self):
        self.theta1 = math.atan(self.y/self.x) - math.atan(((self.a2)*math.sin(self.theta2))/(self.a1 +(self.a2)*(math.cos(self.theta2))))    
        return self.theta2
    
    
    def calculatet6(self):
        self.theta6 = pi - ((self.theta1)+(self.h))

    def calculatel6(self):
        self.calculatet6()
        self.l6 = sqrt((self.a6)**2+(self.k)**2 -2*(math.cos(self.theta6))*(self.a6)*(self.k))
    
    def calculatet4(self):
        self.theta4 = pi - self.theta2

    def calculatel4(self):
        self.calculatet4()
        self.l4 = sqrt((self.i)**2+(self.a4)**2-2*(math.cos(self.theta4)*(self.a4)*(self.i)))  


    def main(self):
        self.calculatetheta1()
        self.calculatetheta2()
        print(self.theta1)
        print(self.theta2)
        self.calculatel4()
        self.calculatel6()
        print(self.l4)
        print(self.l6)
        

if __name__ == '__main__' :
    Inverse().main()