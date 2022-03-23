#!/usr/bin/env python
import rospy
import random
from cr_week8_test.msg import object_info,human_info

def generator():
    id = 0
    #define the node
    rospy.init_node('interaction_generator', anonymous=True)

    #publish the topic
    object_pub = rospy.Publisher('object', object_info, queue_size=10)
    human_pub = rospy.Publisher('human', human_info, queue_size=10)

    #set the rate
    rate = rospy.Rate(0.1) #10sec
    while not rospy.is_shutdown():
        object_value = object_info()
        human_value = human_info()

        #id
        id = id+1
        object_value.id = id
        human_value.id = id

        #object_size
        # 1:small
        # 2:big
        object_value.object_size = random.randint(1,2)

        #human_expression
        # 1:happy
        # 2:sad
        # 3:neutral
        human_value.human_expression = random.randint(1,3)

        #human_action
        # 1: looking at the robot face
        # 2: looking at the colored toy
        # 3: looking away
        human_value.human_action = random.randint(1,3)

        #publish
        # topic: object
        # msg: object_info
        # id, object_size
        #rospy.loginfo(object_value)  
        object_pub.publish(object_value) 
        # topic: human
        # msg: human_info
        # id, human_expression, human_action     
        #rospy.loginfo(human_value)
        human_pub.publish(human_value)
        rate.sleep()
if __name__ == '__main__':
    try:
        generator()
    except rospy.ROSInterruptException:
        pass
