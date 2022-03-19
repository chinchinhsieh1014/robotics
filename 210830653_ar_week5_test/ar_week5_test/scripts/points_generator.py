#!/usr/bin/env python
import rospy
import random
from ar_week5_test.msg import cubic_traj_params

def points():
    #define the node
    rospy.init_node('point_generator', anonymous=True)
    #publish the topic
    pub = rospy.Publisher('point_value', cubic_traj_params, queue_size=10)
    #set the rate
    rate = rospy.Rate(0.05) #20sec
    while not rospy.is_shutdown():
	point = cubic_traj_params()
	point.p0 = random.uniform(-10,10)
	point.pf = random.uniform(-10,10)
	point.v0 = random.uniform(-10,10)
	point.vf = random.uniform(-10,10)
	point.t0 = 0.0
	point.tf = random.uniform(5,10)
        rospy.loginfo(point)
        #publish the message to the topic
        pub.publish(point)
        rate.sleep()

if __name__ == '__main__':
    try:
        points()
    except rospy.ROSInterruptException:
        pass
