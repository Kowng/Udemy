#!/usr/bin/env python3

import rospy
import time
from std_msgs.msg import Int64

if __name__ == '__main__':
    rospy.init_node('the_number_node_publisher', anonymous=True)
    
    pub = rospy.Publisher("/the_number_topic", Int64, queue_size=10)
    
    publish_frequency = rospy.get_param("/number_publish_frequency")
    number = rospy.get_param("/number_to_publish")
    # rospy.set_param("/another_param", "Hello")
    
    rate = rospy.Rate(publish_frequency)
    
    while not rospy.is_shutdown():
        msg = Int64()
        msg.data = number
        pub.publish(msg)
        rate.sleep
       
        
        
    
        