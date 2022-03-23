#!/usr/bin/env python
import rospy
from cr_week8_test.msg import perceived_info, robot_info
from cr_week8_test.srv import predict_robot_expression, predict_robot_expressionResponse
from bayesian.bbn import *
def p_O(O):
    return 1.0/2.0
def p_HA(HA):
    return 1.0/3.0
def p_HE(HE):
    return 1.0/3.0

def p_RE(O,HA,HE,RE):
    if RE == 1:
        table = dict()
        table['HRS'] = 0.8
    	table['HRB'] = 1.0
    	table['HOS'] = 0.8
    	table['HOB'] = 1.0
    	table['HAS'] = 0.6
    	table['HAB'] = 0.8
    	table['SRS'] = 0.0
    	table['SRB'] = 0.0
    	table['SOS'] = 0.0
    	table['SOB'] = 0.1
    	table['SAS'] = 0.0
    	table['SAB'] = 0.2
    	table['NRS'] = 0.7
    	table['NRB'] = 0.8
    	table['NOS'] = 0.8
    	table['NOB'] = 0.9
    	table['NAS'] = 0.6
    	table['NAB'] = 0.7
    	key = ''
    	if HE == 1:
            key = key+'H'
    	elif HE == 2:
       	    key = key+'S'
    	else: #0,3
            key = key+'N'
    	if HA == 1:
            key = key+'R'
    	elif HA == 2:
            key = key+'O'
    	else: #0,3
            key = key+'A'
        if O == 1:
            key = key+'S'
        else: #0,2
            key = key+'B'
        return table[key]

    if RE == 2:
        table = dict()
    	table['HRS'] = 0.2
    	table['HRB'] = 0.0
    	table['HOS'] = 0.2
    	table['HOB'] = 0.0
    	table['HAS'] = 0.2
    	table['HAB'] = 0.2
    	table['SRS'] = 0.0
    	table['SRB'] = 0.0
    	table['SOS'] = 0.1
    	table['SOB'] = 0.1
    	table['SAS'] = 0.2
    	table['SAB'] = 0.2
    	table['NRS'] = 0.3
    	table['NRB'] = 0.2
    	table['NOS'] = 0.2
    	table['NOB'] = 0.1
    	table['NAS'] = 0.2
    	table['NAB'] = 0.2
    	key = ''
    	if HE == 1:
            key = key+'H'
    	elif HE == 2:
            key = key+'S'
        else: #0, 3
            key = key+'N'
        if HA == 1:
            key = key+'R'
        elif HA == 2:
            key = key+'O'
        else: #0, 3
            key = key+'A'
        if O == 1:
            key = key+'S'
        else: #0, 2
            key = key+'B'
        return table[key]

    if RE == 3:
        table = dict()
        table['HRS'] = 0.0
        table['HRB'] = 0.0
        table['HOS'] = 0.0
        table['HOB'] = 0.0
        table['HAS'] = 0.2
        table['HAB'] = 0.0
        table['SRS'] = 1.0
        table['SRB'] = 1.0
        table['SOS'] = 0.9
        table['SOB'] = 0.8
    	table['SAS'] = 0.8
    	table['SAB'] = 0.6
    	table['NRS'] = 0.0
    	table['NRB'] = 0.0
    	table['NOS'] = 0.0
    	table['NOB'] = 0.0
   	table['NAS'] = 0.2
    	table['NAB'] = 0.1
    	key = ''
   	if HE == 1:
            key = key+'H'
        elif HE == 2:
            key = key+'S'
        else: #0,3
            key = key+'N'
        if HA == 1:
            key = key+'R'
        elif HA == 2:
            key = key+'O'
        else: #0, 3
            key = key+'A'
        if O == 1:
            key = key+'S'
        else: #0,2
            key = key+'B'
        return table[key]

def ep(req):
    O = req.object_size
    HE = req.human_expression
    HA = req.human_action
    bnn = build_bbn(p_O,p_HA,p_HE,p_RE,
                    domains=dict(
                    O = [1,2],
                    HE = [1,2,3],
                    HA = [1,2,3],
                    RE = [1,2,3]))

    if O == 0:
        r = bnn.query(HA=HA,HE=HE)      
    elif HE == 0:
        r = bnn.query(O=O,HA=HA)
    elif HA == 0:
        r = bnn.query(O=O,HE=HE)
    elif O == 0 and HE == 0:
        r = bnn.query(HA=HA)
    elif O == 0 and HA == 0:
        r = bnn.query(HE=HE)
    elif HE == 0 and HA == 0:
        r = bnn.query(O=O)
    elif O == 0 and HE == 0 and HA == 0:
        r = bnn.query()
    else:
        r = bnn.query(O=O,HA=HA,HE=HE)    
    p = {n[1]:v for n,v in r.items() if n[0]=='RE'}
    return predict_robot_expressionResponse(req.id,p[1],p[2],p[3])
    
def expression_prediction():
    #define the node
    rospy.init_node('robot_expression_prediction', anonymous=True)
    #define the service
    s = rospy.Service('ep_service',predict_robot_expression,ep)
    #keeps nodes from exiting until this node is stopped
    rospy.spin()

if __name__ == "__main__":
    expression_prediction()
