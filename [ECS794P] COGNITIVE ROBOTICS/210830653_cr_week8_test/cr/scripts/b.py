#!/usr/bin/env python
import rospy
from cr.msg import info
from cr.srv import p, pResponse
from bayesian.bbn import *

def p_eye(eye, noise):
    if noise==0:
	return 1.0/2.0
    else:
        return 1.0/6.0

def p_n(noise):
    return 1.0/2.0

def p_head(head):
    return 1.0/3.0

def p_RE(eye,noise,head,RE):
    if RE == 1:
        table = dict()
        table['001'] = 0.66
    	table['002'] = 0.33
    	table['003'] = 0.0
    	table['111'] = 0.66
    	table['112'] = 0.33
    	table['113'] = 0.0
    	table['121'] = 0.66
    	table['122'] = 0.33
    	table['123'] = 0.0
    	table['131'] = 0.66
    	table['132'] = 0.33
    	table['133'] = 0.0
    	key = ''
    	if noise == 1:
            key = key+'00'
    	else: #2
            key = key+'1'
	    if eye == 2:
	        key = key+'1'
	    elif eye == 3:
		key = key+'2'
	    else: #4
		key = key+'3'
        if head == 1:
            key = key+'1'
        elif head ==2:
            key = key+'2'
        else:
            key = key+'3'
        return table[key]

    if RE == 2:
        table = dict()
        table['001'] = 0.33
    	table['002'] = 0.33
    	table['003'] = 0.33
    	table['111'] = 0.33
    	table['112'] = 0.33
    	table['113'] = 0.33
    	table['121'] = 0.33
    	table['122'] = 0.33
    	table['123'] = 0.33
    	table['131'] = 0.33
    	table['132'] = 0.33
    	table['133'] = 0.33
    	key = ''
    	if noise == 1:
            key = key+'00'
    	else: #2
            key = key+'1'
	    if eye == 2:
	        key = key+'1'
	    elif eye == 3:
		key = key+'2'
	    else: #4
		key = key+'3'
        if head == 1:
            key = key+'1'
        elif head ==2:
            key = key+'2'
        else:
            key = key+'3'
        return table[key]

    if RE == 3:
        table = dict()
        table['001'] = 0.0
    	table['002'] = 0.33
    	table['003'] = 0.66
    	table['111'] = 0.0
    	table['112'] = 0.33
    	table['113'] = 0.66
    	table['121'] = 0.0
    	table['122'] = 0.33
    	table['123'] = 0.66
    	table['131'] = 0.0
    	table['132'] = 0.33
    	table['133'] = 0.66
    	key = ''
    	if noise == 1:
            key = key+'00'
    	else: #2
            key = key+'1'
	    if eye == 2:
	        key = key+'1'
	    elif eye == 3:
		key = key+'2'
	    else: #4
		key = key+'3'
        if head == 1:
            key = key+'1'
        elif head ==2:
            key = key+'2'
        else:
            key = key+'3'
        return table[key]

def ep(req):
    eye = req.eye_direction
    noise = req.noise
    head = req.head_direction
    bnn = build_bbn(p_eye,p_n,p_head,p_RE,
                    domains=dict(
                    noise = [1,2],
                    eye = [1,2,3,4],
                    head = [1,2,3],
                    RE = [1,2,3]))

    r = bnn.query(noise=noise,eye=eye,head=head)    
    p = {n[1]:v for n,v in r.items() if n[0]=='RE'}
    print(p)
    return pResponse(p[1],p[2],p[3])
    
def prediction():
    #define the node
    rospy.init_node('bayesian', anonymous=True)
    #define the service
    s = rospy.Service('bayesian_service',p,ep)
    #keeps nodes from exiting until this node is stopped
    rospy.spin()

if __name__ == "__main__":
    prediction()
