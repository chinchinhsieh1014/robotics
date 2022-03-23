#!/usr/bin/env python
import rospy
from cr_week8_test.msg import object_info, human_info, perceived_info
import random

class Filter(object):
    def __init__(self):
        self.O = 0
        self.HA = 0
        self.HE = 0
        rospy.Subscriber('object',object_info,self.callback1)
        rospy.Subscriber('human',human_info,self.callback2)

    def callback1(self, msg):
        self.O = msg.object_size
        
    def callback2(self, msg):
        i = random.randint(1,8)
        if i == 1:
            self.O = 0
            self.HA = msg.human_action
            self.HE = msg.human_expression
        elif i == 2:
            self.O = self.O
            self.HA = 0
            self.HE = msg.human_expression
        elif i == 3:
            self.O = self.O
            self.HA = msg.human_action
            self.HE = 0
        elif i == 4:
            self.O = 0
            self.HA = 0
            self.HE = msg.human_expression
        elif i == 5:   
            self.O = 0 
            self.HA = msg.human_action
            self.HE = 0 
        elif i == 6:
            self.O = self.O
            self.HA = 0
            self.HE = 0
        elif i == 7:
            self.O = 0
            self.HA = 0
            self.HE = 0
        else:
            self.O = self.O
            self.HA = msg.human_action
            self.HE = msg.human_expression
        perception_pub = rospy.Publisher('perception', perceived_info, queue_size=10)
        p = perceived_info()
        p.id = msg.id
        p.object_size = self.O
        p.human_action = self.HA
        p.human_expression = self.HE
        perception_pub.publish(p)
if __name__ == '__main__':
    rospy.init_node('perception_filter', anonymous=True)
    f = Filter()
    rospy.spin()
    
