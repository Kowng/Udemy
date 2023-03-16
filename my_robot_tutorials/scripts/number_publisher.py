#!/usr/bin/env python3

import rospy
import time
from std_msgs.msg import Int64

if __name__ == '__main__':
    rospy.init_node('the_number_node_publisher')
    
    pub = rospy.Publisher("/the_number_topic", Int64, queue_size=10)
    
    rate = rospy.Rate(0.00001)
    
    while not rospy.is_shutdown():
        msg = Int64()
        msg.data = 1
        pub.publish(msg)
        rate = rospy.Rate(0.00001)
        rate.sleep
       
        
        
    
        