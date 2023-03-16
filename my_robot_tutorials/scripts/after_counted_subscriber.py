#!/usr/bin/env python3

import rospy
import time
from std_msgs.msg import Int64

def callback(msg):
    rospy.loginfo("Received message: %d", msg.data)
    rate = rospy.Rate(0.00001)


if __name__ == '__main__':
    rospy.init_node('my_subscriber')
    sub = rospy.Subscriber("/after_counted_topic", Int64, callback)
    rospy.spin()
