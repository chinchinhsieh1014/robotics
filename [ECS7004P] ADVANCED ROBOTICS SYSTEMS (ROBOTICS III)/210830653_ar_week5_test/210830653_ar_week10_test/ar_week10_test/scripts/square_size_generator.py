#!/usr/bin/env python
import rospy
import random
from ar_week10_test.msg import size_param

def generator():
    #define the node
    rospy.init_node('square_size_generator', anonymous=True)
    #publish the topic
    pub = rospy.Publisher('size', size_param, queue_size=10)
    #set the rate
    rate = rospy.Rate(0.05) #20sec
    while not rospy.is_shutdown():
        size = size_param()
        size.s = random.uniform(0.05,0.2)
        rospy.loginfo(size)
        #publish the message to the topic
        pub.publish(size)
        rate.sleep()

if __name__ == '__main__':
    try:
        generator()
    except rospy.ROSInterruptException:
        pass
