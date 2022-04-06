Yi-Chin, Hsieh 210830653

Environment:
ros1 melodic 
python2

Setup:
1. Unzip "ar_week10_test" in to the workspace
2. Open a terminal
3. Change the path to the workspace
4. Build the workspace
   catkin_make
   source /devel/setup.bash

Install moveit
1. Change the path to workspace/src
2. Input commands in order
git clone -b melodic-devel https://github.com/ros-planning panda_moveit_config.git
rosdep update
rosdep install --from-paths . --ignore-src -r -y 
cd .. 
catkin_make 
source deve/setup.bash

Run:
1. Open 5 terminals
2. Respectively build the workspace
3. Input "roscore" in terminal1 to run the master
4. Input "rosrun ar_week10_test square_size_generator.py" in terminal2 to run node1
5. Show the generated value in terminal2
6. Input "rosrun ar_week10_test move_panda_square.py" in terminal3 to run node2
7. Show the planning process
8. Input "roslaunch panda_moveit_config demo.launch" in terminal4 to launch moveit
9. Display the planned trajectory
10. Input "rosrun rqt_plot rqt_plot" in terminal5
11. Show the plot

