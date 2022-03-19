#!/usr/bin/env python
import rospy
import numpy as np
import math
from ar_week5_test.srv import compute_cubic_traj, compute_cubic_trajResponse

def compute_coeffs(req):
    #calculate a0-a3 by solving A*a=B
    #p0 = a0 + a1*t0 + a2*t0^2 + a3*t0^3
    #v0 =      a1    + 2*a2*t0 + a3*t0^2
    #pf = a0 + a1*tf + a2*tf^2 + a3*tf^3
    #vf =      a1    + 2*a2*tf + 3*a3*tf^2
    A = np.array([[1.0,req.t0,req.t0**2,req.t0**3],
                  [0.0,1.0,2*req.t0,3*(req.t0**2)],
                  [1.0,req.tf,req.tf**2,req.tf**3],
                  [0.0,1.0,2*req.tf,3*(req.tf**2)]])
    B = np.array([req.p0,req.v0,req.pf,req.vf]).reshape(4,1)
    A_inv = np.linalg.inv(A)
    a = A_inv.dot(B)
    a = a.reshape(-1)
    #return the response (a0, a1, a2, a3)
    return compute_cubic_trajResponse(a[0],a[1],a[2],a[3])


def computer_cubic_coeffs():
    #Define the node
    rospy.init_node('compute_cubic_coeffs', anonymous=True)
    #Define the service
    s = rospy.Service('compute_coeffs', compute_cubic_traj, compute_coeffs)
    #keeps node from exiting until this node is stopped
    rospy.spin()

if __name__ == "__main__":
    computer_cubic_coeffs()
