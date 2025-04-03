# albert_moveit_config 
The `albert_moveit_config` package houses everything in regards the assembly of
the robot base, its control drivers in the form of launch files and files about
the environment.


## Differences between ROS versions
This package remained unedited and is only applicable for ROS 1 (noetic).
!!! question "TODO"
    The above statement doesn't appear to be true...


## Launch files
!!! question "TODO"
    Establish the current state of each launch file
    
    - have they been ported to ROS 2?
    - Are they working?

The `albert_moveit_config` package and consequently the
launch files house all the environments, robot configuration, controllers,
navigators, planners, sensors and actuators. Without this package these
packages will not be loaded and the robot will not work. Since this package has
many launch files for many different components a short explanation will be
provided:

1. `albert_description_moveit_controller_manager_launch.py`: This launch file
   is responsible for configuring the **MoveIt!** controller manager,
   specifying a controller manager plugin, and loading controller configu-
   rations. By default, it uses the
   `moveit_simple_controller_manager/MoveItSimpleControllerManager` plugin and
   loads parameters from `albert_moveit_config/config/ros_controllers.yaml`,
   facilitating the management of robot motion controllers within the
   **MoveIt!** framework.

1. `albert_description_moveit_sensor_manager_launch.py`:
    !!! question "TODO"
        Fill in description for this launch file.

1. `chomp_planning_pipeline_launch.py`: This launch file sets up the CHOMP
   (Covariant Hamiltonian Optimization for Motion Planning) planner plugin for
   **MoveIt!**, defining planning adapters, planner parameters, and loading
   specific YAML configuration files. It enables customization of motion
   planning behavior by adjusting parameters like start state bounds error and
   loading configurations.

1. `default_warehouse_db_launch.py`: This launch file initializes the **MoveIt!**
   warehouse database, allowing optional database reset and specifying the
   database path. It launches the warehouse with the configured database
   location and resets it if the `reset` argument is provided, facilitating
   storage and retrieval of motion planning data.

1. `demo_launch.py`: Orchestrating a comprehensive demo environment for
   **MoveIt!**, this launch file includes joint state publishers, robot state
   publishers, the **MoveIt!** main executable, and RViz visualization. It
   offers flexibility in configuring parameters such as planning pipeline,
   database usage, debug mode, and visualization settings, providing an
   integrated setup for demonstration purposes.

1. `demo_gazebo_launch.py`: Extending the demo environment to Gazebo simulation,
   this launch file incorporates Gazebo-specific options like GUI visibility
   and pause state. It integrates joint state publishers, robot state
   publishers, **MoveIt!** executable, and RViz visualization tailored for
   Gazebo simulation, facilitating realistic robot testing and development
   within the Gazebo environment.

1. `fake_moveit_controller_manager_launch.py`: Configuring a fake controller
   manager for **MoveIt!**, this launch file sets parameters for execution type
   and specifies a controller manager plugin `MoveItFakeControllerManager`.
   It also loads controller configurations from
   `albert_moveit_config/config/fake_controllers.yaml`, enabling simulation of
   controller behavior without physical hardware.

1. `gazebo_launch.py`: Setting up the Gazebo simulator environment for robot
   simulation, this launch file handles options like GUI visibility and pause
   state. It loads the robot's URDF description, spawns the robot in Gazebo,
   and launches ROS controllers, facilitating robot simulation within the
   Gazebo environment.

1. `joystick_control_launch.py`: Configuring joystick control for **MoveIt!**,
   this launch file launches the joy node to interface with the joystick and
   the `moveit_joy.py` script for controlling the robot using joystick input,
   enabling intuitive teleoperation of the robot via joystick.

1. `move_group_launch.py`: Initializing **MoveIt!**'s `move_group` node, this launch
   file sets various parameters related to trajectory execution, planning
   pipeline, execution type, and other functionalities like sensor management
   and publishing monitored planning scene, providing the core functionality
   for motion planning and execution within **MoveIt!**.

1. `moveit_rviz_launch.py`: Setting up RViz visualization for **MoveIt!**, this
   launch file launches RViz with specified configuration files and debug
   options, offering a graphical interface for visualizing robot states,
   planning trajectories, and debugging **MoveIt!** functionality.

1. `ompl_planning_pipeline_launch.py`: Configuring the OMPL (Open Motion
   Planning Library) plugin for **MoveIt!**, this launch file specifies
   planning adapters, planner parameters, and loads configuration files for the
   planning pipeline, enabling efficient and customizable motion planning using
   OMPL algorithms.

1. `pilz_industrial_motion_planner_planning_pipeline.launch.xml`: Configuring
   the Pilz Industrial Motion Planner plugin for **MoveIt!**, this launch file
   sets planning adapters, parameters, capabilities, and disables certain
   functionalities, providing an alternative motion planning solution tailored
   for industrial applications.

1. `planning_context.launch`: Loading and configuring the robot description,
   semantic description, joint limits, and kinematics settings for
   **MoveIt!**'s planning context, this launch file allows overriding URDF
   descriptions and loading specific parameter files, providing essential setup
   for motion planning tasks.

1. `planning_pipeline.launch.xml`: This launch file offers a unified interface for
   incorporating different planning pipelines into **MoveIt!**, simplifying the
   process of switching between various planning algorithms. By including the
   specified planning pipeline launch file based on the provided `pipeline`
   argument, along with optional capabilities and disable capabilities, it
   enhances flexibility and modularity in motion planning setups.

1. `ros_controllers.launch`: Responsible for managing joint controllers in
   **MoveIt!**, this launch file loads joint controller configurations from a
   YAML file to the ROS parameter server. It then spawns the controllers using
   the controller_manager package, facilitating the control of robot joints and
   enabling seamless integration with **MoveIt!** for trajectory execution.

1. `run_benchmark_ompl.launch`: This launch file facilitates benchmarking of
   OMPL planners within **MoveIt!**, streamlining the process of evaluating and
   comparing motion planning performance. It initializes the benchmarking
   environment by loading the URDF description, starting the database, and
   executing the **MoveIt!** benchmarking tool with specified configuration
   files, providing valuable insights into planner efficiency and
   effectiveness.

1. `sensor_manager.launch.xml`: Handling sensor management configurations, this
   launch file loads parameters for 3D sensors and octomap monitoring,
   essential for environment perception and collision detection in motion
   planning. It dynamically loads a robot-specific sensor manager launch file
   based on the `moveit_sensor_manager` argument, ensuring compatibility with
   different robotic setups.

1. `setup_assistant.launch`: Offering convenience in configuring **MoveIt!**
   for specific robot models, this launch file relaunches the **MoveIt!** Setup
   Assistant with a predefined configuration package already loaded. It
   simplifies the setup process by providing a guided interface for configuring
   **MoveIt!** components such as robot description, planning scene, and
   kinematics settings.

1. `trajectory_execution.launch.xml`: This launch file handles settings related
   to trajectory execution in **MoveIt!**, including parameters for allowed
   execution duration scaling, goal duration margin, and start tolerance. It
   dynamically loads a robot-specific controller manager launch file based on
   the `moveit_controller_manager` argument, ensuring proper execution of
   planned trajectories on the robot.

1. `warehouse.launch`: Responsible for initializing the **MoveIt!** warehouse, this
   launch file specifies the database path and launches the **MongoDB** server. It
   creates the necessary environment for storing and retrieving motion planning
   data, facilitating efficient data management and analysis within MoveIt!.

1. `warehouse_settings.launch.xml`: Configuring parameters for the **MoveIt!**
   warehouse, this launch file sets the port and host for communication,
   specifies the **MongoDB** server executable, and defines the warehouse plugin.
   It ensures proper communication and functionality of the **MoveIt!** warehouse,
   enhancing data storage and retrieval capabilities for motion planning tasks.
