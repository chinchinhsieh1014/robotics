#!/usr/bin/env python
import rospy
from cr.msg import info,perdict
from cr.srv import p, pResponse

def perceive(data):
    #data.noise
    #data.eye_direction
    #data.head_direction
    #create the hadle for calling the service
    likelihood = rospy.ServiceProxy('bayesian_service',p)
    resp = likelihood(data.noise, data.eye_direction, data.head_direction)
    #publish the topic
    robot_pub = rospy.Publisher('direction', perdict ,queue_size=10)
    r = perdict()
    r.gaze_left = resp.p_left
    r.gaze_right = resp.p_right
    r.gaze_toward = resp.p_toward
    rospy.loginfo(r)
    robot_pub.publish(r)

def control():
    #define the node
    rospy.init_node('observer', anonymous=True)
    #subscribe the topic
    rospy.Subscriber('info_generated', info, perceive)
    #keep nodes from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    control()
