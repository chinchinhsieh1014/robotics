#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from ar_week10_test.msg import size_param
import sys
import copy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

def callback(data):
    sleep_time = (data.s*(5/0.2))+1
    print("Move Panda – Received square size, s=%f"%data.s)
    print("------------------------------------------------------------")
    print("Move Panda – Going to start configuration")
    print("------------------------------------------------------------")
    joint_goal = move_group.get_current_joint_values()
    joint_goal[0] = 0
    joint_goal[1] = -pi/4
    joint_goal[2] = 0
    joint_goal[3] = -pi/2
    joint_goal[4] = 0
    joint_goal[5] = pi/3
    joint_goal[6] = 0
    # move the panda robot to the starting configuration
    move_group.go(joint_goal, wait=True)
    #ensures that there is no residual movement
    move_group.stop()
    print("------------------------------------------------------------")
    print("Move Panda – planning motion trajectory ")
    print("------------------------------------------------------------")
    #plan a Cartesian path with received msg
    points = []
    wpose = move_group.get_current_pose().pose
    wpose.position.y += data.s
    points.append(copy.deepcopy(wpose))
    wpose.position.x += data.s
    points.append(copy.deepcopy(wpose))
    wpose.position.y -= data.s
    points.append(copy.deepcopy(wpose))
    wpose.position.x -= data.s 
    points.append(copy.deepcopy(wpose))
    (plan, fraction) = move_group.compute_cartesian_path(
                                   points,   # waypoints to follow
                                   0.01,     # eef_step
                                   0.0)      # jump_threshold
    rospy.sleep(sleep_time)
    print("------------------------------------------------------------")
    print("Move Panda – Showing planned trajectory ")
    print("------------------------------------------------------------")
    #ask RViz to visualize a plan
    display_trajectory = moveit_msgs.msg.DisplayTrajectory()
    #start with the current state
    display_trajectory.trajectory_start = robot.get_current_state()
    #add the plan to the trajectory
    display_trajectory.trajectory.append(plan)
    #publish the topic
    display_trajectory_pub.publish(display_trajectory)
    rospy.sleep(sleep_time)
    print("------------------------------------------------------------")
    print("Move Panda – Executing planned trajectory ")
    print("------------------------------------------------------------")
    move_group.execute(plan)
    #wait until the message is available
    print("------------------------------------------------------------")       
    print("Move Panda – Waiting for desired size of square trajectory")
    print("------------------------------------------------------------")

def shutdown():
    rospy.loginfo("Stopping the robot...")
    rospy.sleep(1)   

def move():
    print("------------------------------------------------------------")
    print("Move Panda - Initializing")
    print("------------------------------------------------------------")
    #initialize moveit_commander
    moveit_commander.roscpp_initialize(sys.argv)
    #define the node
    rospy.init_node('move', anonymous=True)
    #set the shutdown function
    rospy.on_shutdown(shutdown)
    rospy.loginfo("Loading robot model 'panda' ...")
    rospy.loginfo("Ready to take commands for planning group panda_arm")
    #wait until the message is available 
    print("------------------------------------------------------------")       
    print("Move Panda – Waiting for desired size of square trajectory")
    print("------------------------------------------------------------")
    #subscribe the topic
    rospy.Subscriber('size', size_param, callback)
    #keep the node existing
    rospy.spin()

if __name__ == '__main__':
    #initialise robot commander
    robot = moveit_commander.RobotCommander()
    #initialise scene planning interface
    scene = moveit_commander.PlanningSceneInterface()
    #initialise move group commander
    move_group = moveit_commander.MoveGroupCommander('panda_arm')
    #create a DisplayTrajectory ROS publisher
    #display trajectories in Rviz
    display_trajectory_pub = rospy.Publisher('/move_group/display_planned_path',
                                     moveit_msgs.msg.DisplayTrajectory,
                                     queue_size=20)
    move()

