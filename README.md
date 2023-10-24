# Table of content
- [Resources](https://github.com/iamrajee/drone_swarm/tree/main#resources)
- https://github.com/AlexJinlei/Autonomous_UAVs_Swarm_Mission
- https://github.com/lauratasso/Implementation-Of-Visual-Communication-Protocol-For-Drone-Swarm-Members
   - [Experiments with various Repositories](https://github.com/iamrajee/drone_swarm/tree/main#experiments-with-various-repositories)
   - [Relavent Papers](https://github.com/iamrajee/drone_swarm/tree/main#relavent-papers)
   - [Videos](https://github.com/iamrajee/drone_swarm/tree/main#videos)
   - [Discussion](https://github.com/iamrajee/drone_swarm/tree/main#discussion)
 
- [miscellaneous.md](https://github.com/iamrajee/drone_swarm/blob/main/miscellaneous.md) ([Docs version](https://docs.google.com/document/d/1-t3jcnEsvo-fB-qy1Mbw-cfyZk_PeQISZ7StKZA2MRg/edit?usp=sharing))
- [Code](https://github.com/iamrajee/drone_swarm/tree/main/code)
<!---
- [Installation](https://github.com/iamrajee/slam_rosmelodic_ws#installation)
- [Package description](https://github.com/iamrajee/slam_rosmelodic_ws#package-description)
- [Helper scripts](https://github.com/iamrajee/slam_rosmelodic_ws#helper-scripts)
- [Team](https://github.com/iamrajee/slam_rosmelodic_ws#team)
- [Contributing](https://github.com/iamrajee/slam_rosmelodic_ws#contributing)
- [FAQ](https://github.com/iamrajee/slam_rosmelodic_ws#faq)
- [Support](https://github.com/iamrajee/slam_rosmelodic_ws#support)
- [License](https://github.com/iamrajee/slam_rosmelodic_ws#license)
- [Acknowledgments](https://github.com/iamrajee/slam_rosmelodic_ws#acknowledgments)
-->
# Resources

## Experiments with various Repositories
1. ego-planner & ego-planner-swarm: code, [Video 1](https://youtu.be/3Qbo0vZSxag), [2](https://youtu.be/HOO_PjKB0Ws), [Herd](https://youtu.be/HOO_PjKB0Ws), [V2](https://youtu.be/bdVy5nFA1N8)
![image](https://github.com/iamrajee/drone_swarm/assets/25712145/73973c82-e78e-4a1b-aa63-03cb844e9dfe)
![image](https://github.com/iamrajee/drone_swarm/assets/25712145/1bd0567a-bab7-47a4-b4a4-c44d384b88db)

2. Multi UAV Simulator | Malintha [video 1](https://youtu.be/jvOl3TvK7yU?si=6cizDqbl5FvE6Hlb) [Video 2](https://youtu.be/HqIlaxgbwcA)

3. **flock2**: https://github.com/clydemcqueen/flock2
   
4.  **ros2swarm**:
5.  **micros_swarm_framework**: http://wiki.ros.org/micros_swarm_framework
6.  Extended Ego planner: https://gitee.com/tiemuhua/ego_refactored
7.   swarm_ros_bridge
8.   slim_bridge ![image](https://github.com/iamrajee/drone_swarm/assets/25712145/79e3127f-f76b-465e-b79a-82c15352a0e2)


## Relavent Papers
1. [Paper](https://github.com/iamrajee/drone_swarm/blob/main/resources/paper/Asian%20Journal%20of%20Control%20-%202022%20-%20Ouyang%20-%20Formation%20control%20of%20unmanned%20aerial%20vehicle%20swarms%20%20A%20comprehensive%20review.pdf): **Asian Journal of Control - 2022 - Ouyang - Formation control of unmanned aerial vehicle swarms A comprehensive review**  
The unmanned aerial vehicle formation plays a crucial role in numerous
applications, such as reconnaissance, agricultural plant protection, and electric
power inspection. This paper provides a comprehensive review and analysis of
the unmanned aerial vehicle swarm communication networks and formation
control strategies. First, the most commonly used unmanned aerial vehicles are
introduced and compared. Next, the entire process of the formation task, from
the formation assignment to the formation transformation, is detailed described.
At last, the widely adopted communication networks are analyzed, and the
existing formation control strategies of the UAV swarm are compared, which
shows that the distributed formation control is superior to the centralized
method and is the future development trend.


2. [Paper](https://github.com/iamrajee/drone_swarm/blob/main/resources/paper/Multi-Platform_Hardware_In_The_Loop_HIL_Simulation_for_Decentralized_Swarm_Communication_Using_ROS_and_GAZEBO.pdf) **MultiPlatform_Hardware_In_The_Loop_HIL_Simulation_for_Decentralized_Swarm_Communication_Using_ROS_and_GAZEBO**    
Swarm of robots is a group of multiple autonomous agents, collaborating with each other to achieve collective missions such as surveillance and tracking. In Unmanned Aerial Vehicles (UAVs) swarms, robust and 
 ecentralized communication between the agents is required. To this end, Software-In-The-Loop (SIL) is performed before the actual ﬂight to avoid the risk of failure. However, single-platform-based simulations can 
 either fully encounter nor resolve the communication challenges. In this work, we target to incorporate the real-time communication challenges such as network failure, faced by multi-agent systems via Hardware-In-The-Loop (HIL) simulation using Robot-Operating-System (ROS), Gazebo and off the shelf communication modems. A Ground-Control-Station (GCS) is developed to monitor and supervise autonomous UAVs missions. The multiplatform HIL completely emulates the multi-agent system and the communication between the agents, thereby reducing the risk of swarm failure.

3. [Paper](https://github.com/iamrajee/drone_swarm/blob/main/resources/paper/MQLINK_A_Scalable_and_Robust_Communication_Network_for_Autonomous_Drone_Swarms.pdf) 
[Video](https://www.youtube.com/watch?v=uB29Q0hU6Z8) : **Robust Communication for Autonomous Drone Swarms / MQLINK_A_Scalable_and_Robust_Communication_Network_for_Autonomous_Drone_Swarms**  
This research task presents a novel drone network architecture, named MQLINK, for autonomous drone swarms which simultaneously addresses the issues of communication, coordination, and scalability. The proposed system utilizes a lightweight, efficient MQTT protocol and incorporates a self developed UAVLINK module to ensure robust communication in various scenarios such as emergencies and infrastructure failures. The effectiveness of MQLINK in leader-follower formation and proximity detection is demonstrated through real-world experiments for the prototypes. This work advances drone swarm technology, offering a practical solution for enhancing mission efficiency, completion rate and group complementarity. The wide spread applications include drone display, surveillance, logistics, construction site inspection, disaster relief and more.

4. **EGO-Swarm_A_Fully_Autonomous_and_Decentralized_Quadrotor_Swarm_System_in_Cluttered_Environments** [Paper](https://ieeexplore.ieee.org/abstract/document/9561902)
![image](https://github.com/iamrajee/drone_swarm/assets/25712145/d4bcbed4-3b27-4dff-b20a-02e0c8c078a8)
The communication framework discussed by author of paper consists of two networks: a broadcast network and a chain network.  

4.1. Broadcast Network: It facilitates communication among agents by sharing collision-free trajectories.
Trajectories are immediately broadcast to all agents, who then store them for generating safe trajectories when needed.
Two methods are proposed to reduce the possibility of collisions:
Trajectories are broadcast at a given frequency to avoid computational burden.
Agents check for potential collisions upon receiving trajectories and generate new collision-free trajectories if necessary.
The computational complexity is managed by comparing an agent's position with trajectories received from surrounding agents within the planning range.  
  
4.2. Chain Network:  This network is used for timestamp synchronization and system startup management.
Agents generate trajectories in a predefined order during system startup.
Each agent generates its initial trajectory after receiving trajectories from agents with higher priority through the chain network, preventing chaos during startup.
In summary, the communication framework employs a broadcast network for immediate trajectory sharing and collision avoidance and a chain network for orderly trajectory generation during system startup.

5. ROS2SWARM - A ROS 2 Package for Swarm Robot Behaviors: http://heikohamann.de/pub/kaiserICRA2022.pdf  
   — Developing reusable software for mobile robots
is still challenging. Even more so for swarm robots, despite
the desired simplicity of the robot controllers. Prototyping and
experimenting are difficult due to the multi-robot setting and
often require robot-robot communication. Also, the diversity
of swarm robot hardware platforms increases the need for
hardware-independent software concepts. The main advantages
of the commonly used robot software architecture ROS 2 are
modularity and platform independence. We propose a new
ROS 2 package, ROS2SWARM, for applications of swarm
robotics that provides a library of ready-to-use swarm behavioral primitives. We show the successful application of our
approach on three different platforms, the TurtleBot3 Burger,
the TurtleBot3 Waffle Pi, and the Jackal UGV, and with a set of
different behavioral primitives, such as aggregation, dispersion,
and collective decision-making. The proposed approach is easy
to maintain, extendable, and has good potential for simplifying
swarm robotics experiments in future applications.  

6. Minimum Snap Trajectory Generation and Control for Quadrotors [Paper](https://ieeexplore.ieee.org/document/5980409)
7. Robust and Efficient Trajectory Planning for Formation Flight in Dense Environments: https://arxiv.org/pdf/2210.04048.pdf
8. Geometrically Constrained Trajectory Optimization for Multicopters: https://arxiv.org/pdf/2103.00190.pdf
9. https://www.researchgate.net/profile/David-St-Onge/publication/322368758_SWARMING_IN_ROS_FROM_DESIGN_TO_DEPLOYMENT/links/5a564bd10f7e9bf2a536c0cf/SWARMING-IN-ROS-FROM-DESIGN-TO-DEPLOYMENT.pdf
10. 


## Videos
1. Drone Swarm Simulation in ROS, Gazebo, Ardupilot & QGroundControl: https://youtu.be/8DAmQF_gQn4?si=MaCl836536xQ-AuK
2. Multi Videos: https://www.youtube.com/@ctu-mrs/videos
3. 

## Discussion
1. Latency and communication proble with ego planner? Works fine for ~10 drones in real-life testing.  
https://github.com/ZJU-FAST-Lab/ego-planner-swarm/issues/30

## Architecture Diagram
![image](https://github.com/iamrajee/drone_swarm/assets/25712145/a768ce70-7a92-4b5e-bfdb-cb3c31c12cc8)
![image](https://github.com/iamrajee/drone_swarm/assets/25712145/9ad054ea-2853-43b3-a593-71ffee434501)
![image](https://github.com/iamrajee/drone_swarm/assets/25712145/414177fb-c935-4345-a4f8-bdae3e8b0657)
![image](https://github.com/iamrajee/drone_swarm/assets/25712145/90530ee1-3b5c-4a8c-9973-77b642719661)
![image](https://github.com/iamrajee/drone_swarm/assets/25712145/be336ffa-32ce-43ad-b41c-03683a71a5d3)


