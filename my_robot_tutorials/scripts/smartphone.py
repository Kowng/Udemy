#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback__recieve_radio_data(msg):
    rospy.loginfo("Message recieved: ")
    rospy.loginfo(msg)

if __name__ == '__main__':

    rospy.init_node('smartphone', anonymous=True)
    
    sub = rospy.Subscriber("/robot_news_radio_py", String, callback__recieve_radio_data)
    
    rospy.spin()
    