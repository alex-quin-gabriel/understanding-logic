# albert_control
This package is used for the controls and operation of the
robot. This package specifies which gripper is used, its dynamics, state, how
it is controlled, and the goal it must reach.


## Differences between ROS versions
- **Launch Files**: Converted launch files to Python scripts for enhanced
  flexibility and integration with ROS 2 tools. For example,
  `boxer_control.launch` was converted to `boxer_control_launch.py`.
- **Scripts**: Moved the `gripper_control.py` script to a new `albert_control`
  directory and added an `__init__.py` file to improve modularity and
  maintainability.
    - The `gripper_control.py` script was overhauled to first comply with ROS 2,
      using the necessary dependencies such as the `rclpy` action client and
      `rlcpy` node to configure and setup nodes subscriptions and publications. 
- **New Configuration Files**: Added ROS 2-specific configuration files,
  `setup.cfg` and `setup.py`, to manage dependencies and build the package
  correctly in the ROS 2 environment.
    !!! note
        The `setup.cfg` file can also be used to specify dependencies and other
        configurations such as the `test` configuration.

## Launch files
The `albert_control` package houses all launch files necessary for
initiating the controls of the robot for both the real world and simulation
environments. The following launch files are inside this package:

`boxer_control.launch.py`: In future update this launch file might become obsolete, because the boxer package has already a boxer control launch file called `control_launch.py`, and may be used directly into the `sim_control_launch.py`. 
<!--
This launch file is a crucial component of the Albert
system's control configuration, setting the stage for the Boxer robot's
operation. It defines the default differential drive mode and dynamically loads
control parameters, reflecting the system's adaptability. Conditionally
included extras enhance customization, while the `controller_manager` and
`twist_mux` nodes ensure precise execution of movement commands. This launch
file exemplifies the meticulous organization within the Albert repository's
suite of packages, enabling nuanced control and efficient task performance by
the robot within its environment.
-->

`panda_control.launch.py`: This launch file is currently not used and will be updated in the future.
<!--
The launch file for the panda robotic arm allows for
multiple control modes and configurations to be loaded. It begins with
defining the default control mode and then loads the relevant controller
configurations from specified packages. State information is published using a
state controller, and depending on the chosen control mode, different
controllers are spawned for various functionalities, such as an example
cartesian controller or **MoveIt** control for more complex manipulations. The
launch file also supports compliant velocity and position control, spawning
the corresponding controllers when these modes are selected. This flexible
setup, part of the `albert_control` and `franka_control` packages, exemplifies
the modular nature of the control system, enabling a variety of robotic tasks
to be executed efficiently.
-->
`sim_control.launch.py`: This launch file serves as a configuration hub for setting up various controllers and parameters for robot simulation. It integrates control logic for different robots, focusing on modularity and adaptability. For the Boxer robot, the file includes the `control_launch.py` file from the `boxer_control package`, which manages the primary control systems, including the differential drive controller and robot state broadcasting. This ensures that the Boxer robot's locomotion and control framework are fully operational within the simulation. For the Panda robot, the file is prepared to include the `panda_control_launch.py` file, which will handle specific controllers and configurations for the Panda robotic arm in the future. Currently, a joint_trajectory_controller for the Panda is directly loaded within this file but is planned to be migrated to the `panda_control_launch.py` for better organization.
