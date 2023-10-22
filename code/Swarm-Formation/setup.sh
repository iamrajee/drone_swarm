source /opt/ros/noetic/setup.bash
sudo rosdep init
sudo rosdep install -i --from-path src --rosdistro noetic -y
rosdep update
catkin_make
source devel/setup.sh
