#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

text = rospy.get_param("/Talker/text")

if __name__ == "__main__":
    pub = rospy.Publisher("chatter",String,queue_size=10)
    rospy.init_node("Talker")
    rate = rospy.Rate(0.5)	
    
    while(not rospy.is_shutdown()):
#        pub.publish("Hello")
        pub.publish(text)
        rospy.loginfo("Node1: "+ str(text))
        rate.sleep()
