# Albert ROS 2 Packages
The `albert_ros2_package` incorporates the basic Albert functionality, which
can then be supplemented with additional packages to extend Albert's feature
set. 


## Core functionality
The basic functions consist of the following packages:

[`albert_bringup`](bringup.md): Launches all the other core packages.

[`albert_control`](control.md): Used for the controls and operation of the
robot. This package specifies which gripper is used, its dynamics, state, how
it is controlled, and the goal it must reach.

[`albert_description`](description.md): Provides the definition of the robot
model, houses meshes of parts of the robot that altogether form the robot
assembly and consequently define the physical (collision) constraints.

[`albert_gazebo`](gazebo.md): Used to spawn `albert_description` into a gazebo
simulation. In essence this package provides the info needed for gazebo to
simulate and show it in a simulation environment.

??? note "Gazebo Ignition"
    Gazebo Classic will reach its end of life in January 2025, making it
    essential to transition to Gazebo Ignition. Gazebo Ignition is suitable for
    ROS 2 Humble :material-turtle:{ .humble-color } and is also compatible with
    ROS Noetic :material-turtle:{ .noetic-color }, making it a versatile choice
    for new developments. The decision to use Gazebo Ignition ensures long-term
    support and access to the latest features and improvements in the
    simulation environment.

    Gazebo Ignition offers improved modularity, a better plugin system, and
    enhanced performance over Gazebo Classic. In Gazebo Ignition, nodes are
    defined and called differently compared to Gazebo Classic. The primary
    differences lie in the naming conventions and the introduction of new
    features such as the [ROS 2 bridge](https://github.com/gazebosim/ros_gz)
    (not to be confused with the `ros1_bridge` used to communicate between ROS
    1 and ROS 2) which ensures that messages are properly
    translated between ROS 2 and Gazebo Ignition.

[`albert_moveit_config`](moveit_config.md): Houses all the information about
sensors, manipulators, controllers and maps (environments) to be used in the
simulation. Additionally this package also houses all the libraries in the form
of launch files to initiate the sensors, controllers and the robot itself.

[`albert_navigation`](navigation.md): Houses the planner for the robot that is
supposed to determine the current best route and update it according to the
current environmental situation.

[`boxer`](boxer.md): This comprehensive package includes several sub-packages
such as `boxer_control`, `boxer_description`, `boxer_gazebo`, `boxer_gazebo_plugins`,
and `boxer_msgs`. Each sub-package has its own set of files and directories,
covering control, description, simulation, plugins, and message definitions for
the Boxer robot.

!!! info "Usage"
    The ROS 2 implementations of this package are used for 
    [simulating Albert in ROS 2](../usage/simulation-ros2.md) but will not be
    deployed on the robot or in the simulation with the `ros1_bridge`.

[`franka_ros2`](franka_ros2.md): This package provides support for the Franka
Emika Panda robot. It includes launch files, configuration files, and URDF
files specific to the Franka robot.

### Dependency diagram
- Blue: Robot package complete
- Green: albert package
- Orange: dependency package
- Red: library

![Dependency diagram](/assets/images/dependency-diagram_light.png#only-light)
![Dependency diagram](/assets/images/dependency-diagram_dark.png#only-dark)


## Additional components 
The following components may not be updated to ROS 2 but are currently used in
various Albert projects. See the individual component repositories for updates.

### Albert skills
The `albert_skills` package houses many functions that makes the albert robot more suited automized order picking
in a store or warehouse environment. Since it has this many functions we will only go over the required libraries it
uses for these functions.

1. **ROS (Robot Operating System)**: The core framework for robot software
   development, facilitating com- munication between robot components.
1. **Gazebo**: A simulation platform integrated with ROS for simulating robots
   in complex environments.
1. **`actionlib`**: A ROS library for handling long-running goals (actions)
   with feedback and preemptive capabilities.
1. **AMCL (Adaptive Monte Carlo Localization)**: A probabilistic localization
   system for a robot moving in 2D, implemented in ROS.
1. **`mock_vacuum_server.py`**: A custom script for simulating a vacuum
   system's functionality in a robotic application.
1. **`fabrics_processing` and `fabrics_bridge`**: Custom ROS packages designed for
   processing and interacting with fabric materials, suggesting use of image
   processing and manipulation tools.
1. **`apriltag_ros`**: A ROS wrapper for the AprilTag library, used for object
   identification and pose estimation through visual markers.

### Albert decision making
The `albert_decision_making` package produces algorithms for the robot to find
the most efficient plan or action for the robot to carry out, this is based on
the robots' status (battery life, state etc...) and based on the desired goal
state.

### Order picker
The `order_picker` package is designed for accepting picking-orders and picking
them up accordingly. For this is requires all the sensors and actuators to be
active in order for it to work. Supposedly this package would be used by the
decision making package to determine the what order to pick up first.

### Base MPC
At the moment this is not relevant.

### Albert vacuum gripper
The `albert_vacuum_gripper` allows for control of the custom grippers that we
use for the airlab project. The control is done by use of action services in
combination with the controllino mini module which accepts conventional ros
commands.

### Airlab gazebo assets
This package houses all the assets required for albert and the environment to
be properly displayed in the gazebo simulation. This package does not require
conversion to ROS 2 since it does not have a `cmakelist`, `package.xml` and
isn't written for ROS in either python or C++.

