source /opt/ros/noetic/setup.bash
sudo rosdep install -i --from-path src --rosdistro $ROS_DISTRO -y
rosdep update
catkin_make
source devel/setup.sh
