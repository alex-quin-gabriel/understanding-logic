# albert_navigation 
The `albert_navigation` package primarily focuses on organizing and
deploying resources for robotic navigation. 


## Differences between ROS versions
- Initially, its integration with ROS 2 faced challenges due to a misaligned
  build system and a lack of a typical Python package structure for ROS 2. To
  resolve these issues, the package underwent several strategic upgrades.
  Notably, the addition of a `setup.py` file marked a critical step in
  formalizing installation parameters and resource paths, significantly
  improving the package's compatibility with ROS 2 tools and transitioning it
  to a Python-centric package. 
- The transition also involved converting traditional ROS launch files
  (`.launch`) into Python-based launch scripts (`.py`), leveraging Python's
  superior readability, flexibility, and maintainability. This change
  facilitated easier manipulation and configuration of the launch processes,
  which is essential for robust robotic operations.
- The `move_base` package from ROS 1, pivotal in navigation, lacks a direct
  equivalent in ROS 2. This gap was bridged by integrating its successor `nav2`
  into the new launch scripts, ensuring seamless functionality within the ROS 2
  ecosystem. However, this integration was not straightforward due to
  significant differences in parameter management between ROS 1 and ROS 2.
  Compared to `move_base`, Nav2 supports more sophisticated navigation
  strategies, including but not limited to:
    - **Improved Path Planning Algorithms**: Enhanced algorithms for more efficient route calculation.
    - **Better Obstacle Avoidance**: Advanced sensors and processing capabilities for safer maneuvering.
    - **Recovery Strategies**: Sophisticated recovery options to handle unexpected obstacles or navigation failures.
- The creation of a new parameter file, `nav2_params.yaml`, was essential. This
  file consolidates the parameters needed by the `nav2` system, addressing both
  legacy and new settings required by the updated navigation stack. The details
  of these parameters, including their functions, are systematically outlined
  in the [table](#nav2-parameters) at the end of this page.

## Launch files
!!! question "TODO"
    Establish the current state of each launch file
    
    - have they been ported to ROS 2?
    - Are they working?

The albert navigation launch is responsible for launching
the correct algorithm (acml or gmapping) for localization and navigation
purposes, it also launches

1. `amcl.launch.py`: This launch file launches the Adaptive Monte Carlo
   Localization (AMCL) node for robot localization in a map. It allows for
   dynamic configuration of parameters such as the usage of map topics, laser
   scan topics, and initial pose. Parameters controlling AMCL's behavior
   include settings for scan publishing rate, odometry model, laser parameters,
   particle filter parameters, map frame IDs, and recovery behavior.
   Additionally, it specifies initial pose values and enables AMCL to receive
   map topics directly instead of through a service call, with an option to use
   only the first received map. Finally, it remaps the laser scan topic to a
   specified topic or defaulting to `front/scan`.

1. `amcl_demo.launch.py`: This launch file sets up map servers for both `nav2`
   and AMCL, specifying map files and keepout map files for each. It then
   launches AMCL for localization and move_base for navigation, passing initial
   pose and base local planner parameters. Finally, it launches RViz for
   visualization, loading a specific RViz configuration file if specified. The
   key difference between this launch file and the previous one lies in the
   inclusion of map servers for `nav2` and AMCL, which load different map
   files and remap the map topics accordingly. Additionally, this launch file
   includes setup for a keepout map server, which was not present in the
   previous launch file.

1. `gmapping.launch.py`: This launch file initializes the GMapping SLAM
   (Simultaneous Localization and Mapping) algorithm, providing parameters
   for laser sensor characteristics, map updates, particle filter settings, and
   scan processing intervals. It configures GMapping to subscribe to a laser
   scan topic specified by the user or defaults to `front/scan`. Parameters
   control various aspects of map generation, including map resolution, size,
   and initial position. Additionally, it sets parameters for sensor
   characteristics such as maximum range and sensor noise. The algorithm
   processes laser scans based on linear and angular update thresholds,
   adjusting the map accordingly. Finally, it remaps the laser scan topic to
   the specified topic or the default `front/scan`. Compared to previous launch
   files, this one focuses specifically on initializing and configuring
   GMapping for SLAM-based mapping and localization, without involving
   components like AMCL or `nav2` for navigation.

1. `gmapping_demo.launch.py`: This launch file is responsible for the execution of
   GMapping for SLAM and Move Base for navigation, along with RViz for
   visualization. It includes launch files for both GMapping, `nav2` and `move_base`,
   passing necessary parameters such as the base local planner YAML file.
   Additionally, it launches RViz with a specific configuration file if the
   `rviz` argument is set to true. The key difference between this launch file
   and the previous one is that it doesn't directly configure GMapping
   parameters like sensor characteristics, map updates, or particle filter
   settings. Instead, it relies on the configurations provided in the included
   launch file for GMapping. Furthermore, it integrates either Move Base or `nav2` for
   navigation, which was not present in the previous launch file focusing
   solely on GMapping initialization.

1. `move_base.launch.py`: This launch file (confusingly) initializes the Nav2 node, a core
   component of ROS navigation stack, responsible for navigating a robot to a
   specified goal location. It loads various parameter files to configure the
   global and local costmaps, as well as the local planner used for obstacle
   avoidance. Parameters for costmaps and local planner are loaded from YAML
   files located in the `albert_navigation/config` directory. Additionally, it
   loads general move_base parameters from
   `albert_navigation/config/nav2_params.yaml`. The
   `base_local_planner_yaml` argument specifies the path to the YAML file
   defining parameters for the local planner. The `map_topic` argument
   specifies the topic on which the map is published. This launch file also
   includes remappings for `odom` and `map` topics, redirecting them to
   `odometry/filtered` and the specified `map_topic` respectively. Overall,
   this launch file sets up Nav2 with configured costmaps, local plan-
   ner, and general navigation parameters, enabling the robot to plan and
   execute navigation tasks within its environment.

    !!! question "TODO"
        Rename this launch file to `nav2.launch.py`.

1. `odom_navigation_demo.launch.py`: This launch file initializes the Move Base
   node in the ROS navigation stack, configuring global and local costmaps as
   well as the local planner for obstacle avoidance through parameter files. It
   specifies the global and local planner plugins to be used, and remaps the
   `odom` topic for receiving filtered odometry data. This setup enables the
   robot to effectively plan and execute navigation tasks within its
   environment, ensuring smooth and reliable movement.

## Nav2 Parameters
The parameters were configured according to this [Nav2 AMCL code example](https://github.com/open-navigation/navigation2/blob/main/nav2_amcl/src/amcl_node.cpp)
and the [Nav2 configuration docs](https://github.com/open-navigation/navigation2/tree/main/nav2_bringup/launch).

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| alpha1 | double | 0.2 | Expected process noise in odometry's rotation estimate from rotation. |
| alpha2 | double | 0.2 | Expected process noise in odometry's rotation estimate from translation. |
| alpha3 | double | 0.2 | Expected process noise in odometry's translation estimate from translation. |
| alpha4 | double | 0.2 | Expected process noise in odometry's translation estimate from rotation. |
| alpha5 | double | 0.2 | For Omni models only: translation noise. |
| base_frame_id | string | "base_footprint" | Robot base frame. |
| beam_skip_distance | double | 0.5 | Ignore beams that most particles disagree with in Likelihood field model. Maximum distance to consider skipping for (m). |
| beam_skip_error_threshold | double | 0.9 | Percentage of beams after not matching map to force full update due to bad convergence. |
| beam_skip_threshold | double | 0.3 | Percentage of beams required to skip. |
| do_beamskip | bool | False | Whether to do beam skipping in Likelihood field model. |
| global_frame_id | string | "map" | The name of the coordinate frame published by the localization system. |
| lambda_short | double | 0.1 | Exponential decay parameter for z_short part of model. |
| laser_likelihood_max_dist | double | 2.0 | Maximum distance to do obstacle inflation on map, for use in likelihood_field model. |
| laser_max_range | double | 100.0 | Maximum scan range to be considered, -1.0 will cause the laser's reported maximum range to be used. |
| laser_min_range | double | -1.0 | Minimum scan range to be considered, -1.0 will cause the laser’s reported minimum range to be used. |
| laser_model_type | string | "likelihood_field" | Which model to use, either beam, likelihood_field, or likelihood_field_prob. |
| set_initial_pose | bool | False | Causes AMCL to set initial pose from the initial_pose* parameters instead of waiting for the initial_pose message. |
| initial_pose | Pose2D | {x: 0.0,<br />y: 0.0,<br />z: 0.0,<br />yaw: 0.0} | X, Y, Z, and yaw coordinates of initial pose (meters and radians) of robot base frame in global frame. |
| max_beams | int | 60 | How many evenly-spaced beams in each scan to be used when updating the filter. |
| max_particles | int | 2000 | Maximum allowed number of particles. |
| min_particles | int | 500 | Minimum allowed number of particles. |
| odom_frame_id | string | "odom" | Which frame to use for odometry. |
| pf_err | double | 0.05 | Particle Filter population error. |
| pf_z | double | 0.99 | Particle filter population density. |
| recovery_alpha_fast | double | 0.0 | Exponential decay rate for the fast average weight filter. |
| recovery_alpha_slow | double | 0.0 | Exponential decay rate for the slow average weight filter. |
| resample_interval | int | 1 | Number of filter updates required before resampling. |
| robot_model_type | string | "nav2_amcl::<br />DifferentialMotionModel" | The fully-qualified type of the plugin class. |
| save_pose_rate | double | 0.5 | Maximum rate (Hz) at which to store the last estimated pose. |
| sigma_hit | double | 0.2 | Standard deviation for Gaussian model used in z_hit part of the model. |
| tf_broadcast | bool | True | Set this to false to prevent AMCL from publishing the transform between the global frame and the odometry frame. |
| transform_tolerance | double | 1.0 | Time with which to post-date the transform that is published. |
| update_min_a | double | 0.2 | Rotational movement required before performing a filter update. |
| update_min_d | double | 0.25 | Translational movement required before performing a filter update. |
| z_hit | double | 0.5 | Mixture weight for z_hit part of model. |
| z_max | double | 0.05 | Mixture weight for z_max part of model. |
| z_rand | double | 0.5 | Mixture weight for z_rand part of model. |
| z_short | double | 0.005 | Mixture weight for z_short part of model. |
| always_reset_initial_pose | bool | False | Requires that AMCL is provided an initial pose when reset. |
| scan_topic | string | "scan" | Laser scan topic to subscribe to. |
| map_topic | string | "map" | Map topic to subscribe to. |
| first_map_only | bool | False | Allows AMCL to accept maps more than once on the map_topic.  |
