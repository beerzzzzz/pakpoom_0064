#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist

frame = Tk()
frame.title("REMOTE")
frame.geometry("200x200")

rospy.init_node("GUI_Remote")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)

def fw():
    print("fw")
    cmd = Twist()
    cmd.linear.x = 1.0
    cmd.angular.z=0.0
    pub.publish(cmd)
        
def bw():
    print("bw")
    cmd = Twist()
    cmd.linear.x = -1.0
    cmd.angular.z=0.0
    pub.publish(cmd)
    
def lt():
    print("lt")
    cmd = Twist()
    cmd.linear.x = 1.0
    cmd.angular.z= 1.0
    pub.publish(cmd)

def rt():
    print("rt")
    cmd = Twist()
    cmd.linear.x = 1.0
    cmd.angular.z= -1.0
    pub.publish(cmd)

B1 = Button(text = "FW", command=fw)
B1.place(x=73, y=20)

B2 = Button(text = "BW", command=bw)
B2.place(x=73, y=130)

B3 = Button(text = "LT", command=lt)
B3.place(x=20, y=80)

B4 = Button(text = "RT", command=rt)
B4.place(x=128, y=80)

frame.mainloop()    
    
    
    
