# boxer
This comprehensive package includes several sub-packages
such as `boxer_control`, `boxer_description`, `boxer_gazebo`, `boxer_gazebo_plugins`,
and `boxer_msgs`. Each sub-package has its own set of files and directories,
covering control, description, simulation, plugins, and message definitions for
the Boxer robot.

## Differences between ROS versions
The ROS 2 implementations of this package are used for [simulating Albert in ROS 2](../usage/simulation-ros2.md)
but will not be deployed on the robot.

- **Launch Files**: Converted launch files across all sub-packages to Python
  scripts for more dynamic configurations and better integration with the ROS
  2 launch system. For example, `control.launch` was converted to
  `control_launch.py`.
- **Configuration Files**: Updated the `control.yaml` configuration file in
  `boxer_control` to be compatible with ROS 2, ensuring correct interpretation of
  control parameters by ROS 2 controllers.
- **URDF Files**: Updated the URDF files in `boxer_description` to be compatible
  with ROS 2, including modifications to `boxer.xacro`, and
  `boxer.urdf.xacro` files.
- **Gazebo Plugins**: Updated the `boxer.gazebo.xacro` file in `boxer_gazebo.urdf.xacro` to
  use the correct ROS 2 control plugins for Gazebo Ignition, ensuring expected
  simulation behavior.
- **New Configuration Files**: Added ROS 2-specific configuration files,
  `setup.cfg` and `setup.py`, to all relevant sub-packages for managing
  dependencies and build processes.


## Launch files
`control_launch.py`:This launch file is responsible for initializing the control systems of the Albert robot in a ROS 2 environment. It includes the loading of essential controllers, such as the joint_state_broadcaster and the diff_drive_base_controller, ensuring that the robot's state and differential drive systems are active and operational. The controllers are loaded sequentially, with the diff_drive_base_controller activated only after the successful startup of the joint_state_broadcaster, ensuring a smooth initialization process.

Although the launch file is prepared to include an Extended Kalman Filter (EKF) node for localization using the robot_localization package, the EKF node is currently commented out and not functioning as intended. Fixing and properly configuring the EKF node will be a priority in future updates to enable robust localization capabilities for the robot. For now, this file focuses on setting up the core control infrastructure needed for the robot's movement and state management.

`status_launch.py`: This launch file is not being used at the moment and will be updated in the future.

`teleop_launch.py`: This launch file is not being used at the moment and will be updated in the future.
