#!/usr/bin/env python
import rospy
from ar_week5_test.msg import cubic_traj_params, cubic_traj_coeffs
from ar_week5_test.srv import compute_cubic_traj, compute_cubic_trajResponse

def calculate(data):
    #data.p0,data.pf,data.v0,data.vf,data.t0,data.tf
    #create the handle for calling the service
    compute = rospy.ServiceProxy('compute_coeffs', compute_cubic_traj)
    resp = compute(data.p0,data.pf,data.v0,data.vf,data.t0,data.tf)
    print(resp)
    #publish the topic
    pub = rospy.Publisher('trajectories', cubic_traj_coeffs, queue_size=10)
    calculation = cubic_traj_coeffs()
    calculation.a0 = resp.a0
    calculation.a1 = resp.a1
    calculation.a2 = resp.a2
    calculation.a3 = resp.a3
    calculation.t0 = data.t0
    calculation.tf = data.tf
    #publish the message to the topic
    pub.publish(calculation)

def cubic_traj_planner():
    #define the node
    rospy.init_node('cubic_traj_planner', anonymous=True)
    #subscribe the topic
    rospy.Subscriber('point_value', cubic_traj_params, calculate)
    #keeps node from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    cubic_traj_planner()
