# albert_gazebo

## Differences between ROS versions
- **Launch Files**: Converted XML launch files to Python scripts for better
  dynamic configuration and integration with the ROS 2 launch system. For
  instance, `albert_gazebo.launch` was converted to `albert_gazebo_launch.py`.

    !!! note
        The interactive marker node is now only instantiated when the `example`
        control mode is selected.

- **Bridge Configuration**: Added a new `bridge.yaml` file to create a bridge
  between Gazebo Ignition and ROS 2, ensuring seamless message translation and
  integration.
- **Worlds Directory**: Introduced a new `worlds` directory with files such as
  `AH_store.world` and `empty_world.world`, only the empty_world.world is currently used
  due to compatibility issues with Gazebo Ignition.
- **New Configuration Files**: Added ROS 2-specific configuration files,
  `setup.cfg` and `setup.py`, to manage package build and dependencies.
- **Gazebo Plugins**: The Gazebo Plugins has been in cooperated in the urdf files in `albert_description` package. 


## Launch files

`albert_gazebo.launch.py`: This launch file sets up the simulation environment for the Albert robot in Gazebo, including spawning the robot and visualizing it in RViz. It launches the default Gazebo simulation environment with an empty world. The `spawn_albert_launch.py` file is used to spawn the Albert robot into the simulation environment, ensuring the robot is properly initialized and ready for interaction. RViz is launched with a predefined configuration (`albert.rviz`) to provide a visualization of the robot's state and setup, and it is always active when this launch file is executed. Additionally, the launch file incorporates a Gazebo-ROS bridge to enable seamless communication between Gazebo and ROS, ensuring integration between the simulation and ROS nodes. This file provides a straightforward setup for visualizing and simulating the Albert robot.

`albert_gazebo_navigation.launch.py`: This ROS launch file is designed to integrate Gazebo simulation, RViz visualization, and foundational setup for navigation capabilities for the Albert robot. It incorporates the `albert_gazebo_launch.py` file to initialize the robot in the simulation environment and launches RViz with a dedicated configuration (`albert_navigation.rviz`) for visualizing navigation-related elements. The file ensures that the simulation is prepared for future navigation features by setting up essential components for Gazebo and RViz integration.

Currently, the navigation launch file is still under development as Nav2 has not yet been implemented. Future updates will enhance the robot's navigation capabilities, enabling more advanced planning and localization functionalities tailored to diverse simulation scenarios. This work-in-progress launch file lays the groundwork for adaptive robot behavior and navigation within the simulation.

`spawn_albert.launch.py`:  This launch file sets up and configures the Gazebo simulation environment for the Albert robot. It includes launching the robot description (`load_albert_description_launch.py`) to dynamically generate and load the robot's URDF for simulation, along with the necessary parameters for the simulation. The launch file also includes the activation of the controller interface by launching the `sim_control_launch.py` from the `albert_control` package. This file ensures that the robot's control systems are initialized once the robot is spawned into the simulation. An event handler is used to ensure that the `sim_control_launch.py` file is executed only after the robot has been successfully spawned into Gazebo, providing a smooth transition from robot initialization to control setup.
