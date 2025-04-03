# albert_bringup
The albert_bringup package is responsible for calling the robot base model and
its drivers, the panda robot arm model and the franka robot arm package Franka
ROS2 control interface together with the necessary models and the necessary
control package.

## Differeces between ROS versions
!!! failure "Not yet updated"
    An attempt was made to setup the robot base with the necessary drivers for
    control in ROS 2 humble. This only is limited to control in the simulation
    as the physical robot base is exclusively compatible with ROS 1 Kinetic. The
    current status of this port is that it is able to launch in gazebo, but
    without actually showing up do to problems with the camera drivers causing
    the error that, this should be changed in the Semantic description file
    called `boxer.sdf`, the camera instances can be found by searching for
    camera with the command ++ctrl+f++. The exact contents of this package will
    be provided in the package diagram.

## Launch files
!!! question "TODO"
    Establish the current state of each launch file
    
    - have they been ported to ROS 2?
    - Are they working?

The bringup package houses 3 launch files, which are `albert.launch.py`,
`boxer.launch.py`, and `panda.launch.py` respectively. 

`albert.launch.py`: Initialize the robot when operation has started. This allows
the robot to localize itself. 

`boxer.launch.py`: Initialize Albert's interface. This allows it to accept
controls. 

`panda.launch.py`: Intialize the robot's panda controller.
