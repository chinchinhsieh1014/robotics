#!/usr/bin/env python
import rospy
from ar_week5_test.msg import cubic_traj_coeffs
import math
from std_msgs.msg import Float32
import random

def traj(data):
    #publish the topic [position trajectory]
    pt = rospy.Publisher('position_trajectory', Float32, queue_size=10)
    #publish the topic [velocity trajectory]
    vt = rospy.Publisher('velocity_trajectory', Float32, queue_size=10)
    #publish the topic [acceleration trajectory]
    at = rospy.Publisher('acceleration_trajectory', Float32, queue_size=10)
    #set the time
    t = rospy.Time.from_sec(data.t0)
    t = t.to_sec()
    end = rospy.Time.from_sec(data.tf)
    end = end.to_sec()
    while t<=end:
	#publish the message to the topic
	    p = data.a0+data.a1*t+data.a2*(t**2)+data.a3*(t**3)
        pt.publish(p)
        #publish the message to the topic
        v = data.a1+2*data.a2*t+3*data.a3*(t**2)
        vt.publish(v)
        #publish the message to the topic
        a = 2*data.a2+6*data.a3*t
        at.publish(a)
        t = t+0.001

def plot_cubic_traj():
    #Define the node
    rospy.init_node('plot_cubic_traj', anonymous=True)
    #subscribe the topic
    rospy.Subscriber('trajectories', cubic_traj_coeffs, traj)
    #keeps node from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        plot_cubic_traj()
    except rospy.ROSInterruptException:
        pass
