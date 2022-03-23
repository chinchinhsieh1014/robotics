# ROS note
- a framework for writing robot software.
🔗 Gate: https://rgate.eecs.qmul.ac.uk 
🔗 Tutorial: http://wiki.ros.org/ROS/Tutorials#Beginner_Level

- Plumbing
    - process management
    - inter-process communication
    - device drivers
- Tools
    - simulation
    - visualization
    - GUI
    - date logging
- Capabilities
    - control
    - planning
    - perception
    - mapping
    - manipulation
- Ecosystem
    - package organization
    - software distribution
    - documentation
    - tutorials
---


### Prerequisites
```
sudo apt-get install ros-melodic-ros-tutorials
```
```
# Check workspace
echo $ROS_PACKAGE_PATH
```
[Filesystem](http://wiki.ros.org/ROS/Tutorials/NavigatingTheFilesystem)
[Graph](http://wiki.ros.org/rqt_graph)
```
sudo apt-get install ros-melodic-rqt
sudo apt-get install ros-melodic-rqt-common-plugins
rosrun rqt_graph rqt_graph
```
[Record](http://wiki.ros.org/ROS/Tutorials/Recording%20and%20playing%20back%20data)

[actionlib](http://wiki.ros.org/actionlib)

---

### Workspace
- src
    - CmakeLists.txt
    - [Package]
- build
- devel
- install
```
mkdir -p ~/[workspace_name]/src
cd ~/[workspace_name]/
catkin_make
source devel/setup.bash
```

### Package
- Each package can contain libraries, executables, scripts, or other artifacts.
- package.xml
    - provides meta information about the package.
- CMakeLists.txt

#### create a catkin package
```
cd ~/[workspace_name]/src
catkin_create_pkg [package_name] [depend1] [depend2] [depend3]
# catkin_create_pkg package1 std_msgs rospy roscpp
```
#### build a catkin workspace and source the setup file
```
cd ~/[workspace_name]
catkin_make
. ~/[workspace_name]/devel/setup.bash
```

---

### Node
- an independent program running in a ROS architecture.

#### roscore
-  a service that provides connection information to nodes so that they can transmit messages to one another.
-  manages the communication between nodes.
- master
- rosout(stdout/stderr)
- parameter server
```
roscore
```
#### rosnode
```
#show active nodes
rosnode list

#return information about a specific node
rosnode info /[node_name]

#run a node within a package
rosrun [package_name] [node_name]

```

### Topic
- a label for a specific information shared by ROS nodes.
- Nodes communicate over topics
- Nodes can **publish** or **subscribe** to a topic
```
#show the available sub-commands
rostopic -h

#show the data published on a topic
#and it also subscribe the topic
rostopic echo [topic_name]

#show the available sub-commands about listing information
rostopic list -h

#return the message type of any topic being published
rostopic type [topic_name]
#show the detail of the message
rosmsg show [msg_type]
```
#### rostopic pub node
```
#publish data on to a topic currently advertised
rostopic pub [topic_name] [msg_type] [agrs]
#EX: rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'
# -1: only publish one message then exit
```
#### rostopic hz node
```
#reports the rate at which data is published
rostopic hz [topic_name]
```
### Message
- a container of information shared by ROS nodes.
- data structure defining the type of a topic

#### [msg](http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv)
- simple text files that describe the fields of a ROS message.
- They are used to generate source code for messages in different languages.
- msg files are stored in the msg directory of a package.
- simple text files with a field type and field name per line.
- Header
- field types
    - int8, int16, int32, int64 (plus uint*)
    - float32, float64
    - string
    - time, duration
    - other msg files
    - variable-length array[] and fixed-length array[C]
```
#create a msg
roscd [package_name]
mkdir [msg_file]
echo "[field type] [field name]" > [msg_file]/[msg_name]

### setup

#show msg
rosmsg show [package_name]/[msg_name]
rosmsg show [msg_name]
```

### Services
- another way that nodes can communicate with each other.
- allow nodes to send a request and recvive a response.
- synchronous remote procedure calls
- Service calls are well suited to things that you only need to do occasionally and that take a bounded amount of time to complete.
- allow one node to call a function that executes in another node
- The server (which provides the service) specifies a callback to deal with the service request, and advertises the service. 
- The client (which calls the service) then accesses this service through a local proxy.
```
#print information about active services
rosservice list

#call the service with the provided args
rosservice call [service_name] [args]

#print service type
rosservice type [service_name]

#find services by service type
rosservice find

#print service ROSRPC uri
rosservice uri
```

#### [srv](http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv)
- a file describes a service.
- It is composed of two parts: a request and a response.
- separated by a '---' line.
- srv files are stored in the srv directory.
```
#create a srv
roscd [package_name]
mkdir [srv_file]

#copy an existing one from another package
roscp [package_name] [file_to_copy_path] [copy_path]
#roscp rospy_tutorials AddTwoInts.srv srv/AddTwoInts.srv

#show ser
rossrv show [package_name]/[srv_name]
rossrv show [srv_name]
```


### rosparam
- allow you to store and manipulate data on the ROS Parameter Server
- The parameter server can store
    - integres
    - floats
    - booleans
    - dictionaries
    - lists
```
#set parameter
rosparam set [param_name] [value]

#return the value of the parameter
rosparam get [param_name]
#show the contents of the entire Parameter Server
rosparam get /

#load parameters from file
rosparam load [file_name] [namespace]

#dump parameters to file
rosparam dump [file_name] [namespace]

#delete parameter
rosparam delete

#list parameter names
rosparam list
```
---
### Publisher, Subscriber
```
roscd [package_name]
mkdir [python_folder]
cd [python_folder]
###add python files
```
```
#make the node executable
chmod +x [python file]
# CMakeLists.txt
catkin_install_python(PROGRAMS [file_name]/[python file]
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```
```
#Build the node
cd ~/[workspace_name]
catkin_make
```
```
#run
cd ~/[workspace_name]
source ./devel/setup.bash
rosrun [package_name] [python_file]  
```
---
### Service, Client
```
### Add service and client python files

#make the node executable
chmod +x [python file]

# In CMakeLists.txt
catkin_install_python(PROGRAMS [file_name]/[python file]
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```
```
#Build the node
cd ~/[workspace_name]
catkin_make
```
```
#run the service
rosrun [package_name] [service.py]

#run the client
rosrun [package_name] [client.py] [vars]
```

---

### Launch
- a tool for easily launching multiple ROS nodes locally and remotelly via SSH as well as setting parameters on the Parameter Server.
- it closes all of its nodes when Ctrl-C is pressed in the console containing roslaunch.
```
#launches multiple ROS nodes
roslaunch [package_name] [launch_files]
```
- launch files
    - XML files
    - describe a collection of nodes along with their topic remappings and parameters.
```xml
<launch>
  <node name="node" pkg="package"
        type="python file" output="screen" />
</launch>
```
```
cd launch
sudo chmod +x [launch_file]
```

---

### [Moveit](http://docs.ros.org/en/melodic/api/moveit_tutorials/html/doc/getting_started/getting_started.html)

---

### [Bayesian Networks](http://wiki.ros.org/bayesian_belief_networks)
- [example code-Kapper](https://gist.github.com/Kappers/c2f30c0948c7a4a86147c698221cb4f7)
- [example code-eBay](https://github.com/eBay/bayesian-belief-networks/blob/master/bayesian/examples/bbns/cancer.py)
- [The Monty Hall Problem](https://brilliant.org/wiki/monty-hall-problem/)










---
- [Bayesian Networks](https://github.com/eBay/bayesian-belief-networks/blob/master/bayesian/examples/bbns/cancer.py)
- [Locally Weighted Projected Regression](https://web.inf.ed.ac.uk/slmc)
    - [python example](http://www.rueckstiess.net/research/snippets/show/9bd4b418)
- [Incremental Linear Regrassion](https://stackoverflow.com/questions/52070293/efficient-online-linear-regression-algorithm-in-python/)
- Two different Reinforcement Learning packages for ROS
    - http://wiki.ros.org/reinforcement_learning/Tutorials/Reinforcement%20Learning%20Tutorial
    - http://wiki.ros.org/openai_ros