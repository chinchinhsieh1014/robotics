#!/usr/bin/env python
import rospy
from cr_week8_test.msg import perceived_info, robot_info
from cr_week8_test.srv import predict_robot_expression, predict_robot_expressionResponse

def perceive(data):
    #data.id
    #data.object_size
    #data.human_action 
    #data.human_expression
    #create the hadle for calling the service
    likelihood = rospy.ServiceProxy('ep_service',predict_robot_expression)
    resp = likelihood(data.id,data.object_size,data.human_action,data.human_expression)
    #publish the topic
    robot_pub = rospy.Publisher('robot',robot_info,queue_size=10)
    r = robot_info()
    r.id = resp.id
    r.p_happy = resp.p_happy
    r.p_sad = resp.p_sad
    r.p_neutral = resp.p_neutral
    robot_pub.publish(r)

def control():
    #define the node
    rospy.init_node('robot_controller', anonymous=True)
    #subscribe the topic
    rospy.Subscriber('perception', perceived_info, perceive)
    #keep nodes from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    control()
