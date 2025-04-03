# albert_description
This package provides the definition of the robot model, houses meshes of parts
of the robot that altogether form the robot assembly and consequently define
the physical (collision) constraints.


## Differences between ROS versions
- **Launch Files**: Converted from XML format to Python scripts to enhance
  flexibility and maintainability. For example, `load_albert_description.launch`
  was converted to `load_albert_description_launch.py`.
- **New Configuration Files**: Added `setup.cfg` and `setup.py` to support the ament
  build system, ensuring proper dependency management and package building.
- **Resource Directory**: Introduced a new `resource` directory to store package
  resources for better organization and accessibility.
- **URDF Files**: Updated existing URDF files to ensure compatibility with ROS 2
  and Gazebo Ignition, including necessary modifications to plugins and
  parameters. Additional URDF files were added for future reference. New xacro files has been added to handle the ros2_control interface in simulation and sensors has been added for the simulation.
- **RViz Configurations**: Updated RViz files to work with RViz2, such as changing
  `rviz/Displays` to `rviz_common/Displays` and `rviz/RobotModel` to
  `rviz_default_plugins/RobotModel`.

## Launch files

The `albert_description` package is responsible for providing the minimal
parameters (description) needed for gazebo to spawn the robot in the simulation
environment. It houses 2 launch files:

`load_albert_description.launch.py`: This launch file sets up the initial parameters for the Albert robot's description in a ROS-based environment. Its primary function is to dynamically generate the robot_description parameter by invoking the xacro command to process the `albert_gazebo.xacro` file. This parameter defines the robot's physical and visual properties, which are critical for both simulation and real-world deployment. The launch file does not handle Gazebo-specific settings or simulations directly but lays the foundation for the robot's environment by generating and publishing its description. Future updates will expand this launch file to include configurations for the Panda arm, allowing for the selection of different end-effectors such as a gripper, gripper with a camera, vacuum, or none, enabling further customization and functionality.

`view_albert.launch.py`: This ROS launch file is used for visualizing the Albert robot in RViz, independent of Gazebo simulation. It includes the `load_albert_description.launch.py` file from the albert_description package to dynamically load the robot's configuration, ensuring the robot's description is properly set up. The file starts RViz with a preconfigured visualization setup (`albert.rviz`) that accurately displays the robot's structure and configuration. Additionally, it initializes the `joint_state_publisher_gui node`, allowing interactive visualization and adjustment of the robot's joint states. This launch file provides a comprehensive setup for visualizing the Albert robot in RViz and does not involve specific end-effector or arm configurations, focusing solely on visualization tasks.
