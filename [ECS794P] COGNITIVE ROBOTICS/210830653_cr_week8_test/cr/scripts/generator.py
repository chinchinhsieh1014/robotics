#!/usr/bin/env python
import rospy
import random
from cr.msg import info

def generator():
    #define the node
    rospy.init_node('generator', anonymous=True)
    #publish the topic
    object_pub = rospy.Publisher('info_generated', info, queue_size=10)
    #set the rate
    rate = rospy.Rate(0.1) #10sec
    while not rospy.is_shutdown():
        i = info()
        i.noise = random.randint(0,1)
        if i.noise==0:
            i.eye_direction = 0
        else:
            i.eye_direction = random.randint(1,3)
        i.head_direction = random.randint(1,3)
        #publish the topic 
        rospy.loginfo(i)
        object_pub.publish(i)
        rate.sleep()

if __name__ == '__main__':
    try:
        generator()
    except rospy.ROSInterruptException:
        pass
