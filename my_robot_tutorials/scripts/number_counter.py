#!/usr/bin/env python3

import rospy
import time
from std_msgs.msg import Int64
from std_srvs.srv import SetBool

counter = 0
pub = None

def callback_the_number_topic(msg):
   global counter
   counter += msg.data
   new_msg = Int64()
   new_msg.data = counter
   pub.publish(new_msg)
   rate = rospy.Rate(0.00001)


def callback_reset_counter(req):
    if req.data:
        global counter
        counter = 0
        return True, "Counter has been successfully reset"
    return False, "Counter has not been successfully reset"


if __name__ == '__main__':

    rospy.init_node('the_number_counter_sub')
    
    sub = rospy.Subscriber("/the_number_topic", Int64, callback_the_number_topic)
    
    
    
    pub = rospy.Publisher("/after_counted_topic", Int64, queue_size=1)
    rate = rospy.Rate(0.00001)  # publish at 1 Hz
    
    reset_service = rospy.Service("/reset_counter",SetBool, callback_reset_counter)
    
    while not rospy.is_shutdown():
        rate.sleep()

    
    rospy.spin()



