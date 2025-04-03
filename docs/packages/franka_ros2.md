# franka_ros2
This package provides support for the Franka Emika Panda robot. It includes
launch files, configuration files, and URDF files specific to the Franka robot.

!!! question "TODO"
    - Add package specific information.
    - Update the modification comments below?


## Installation of `libfranka`
Franka Panda arm is communicated with via the Franka Control Interface (FCI). This
requires `libfranka-0.13.2`. Follow the steps below to clone and build it locally.

!!! question "TODO"
    The Franka Panda arm that we have is only compatible with `libfranka-0.9.2`
    and using it with ROS 2 requires [this fork](https://github.com/LCAS/franka_arm_ros2) of the `fanka_ros2` library.
    Consider modifying these instructions to accomodate that version instead.

    See the [Limitations and Requirements](../architecture/index.md#limitations-and-requirements) section.


### Clone the libfranka Repository

```bash
git clone https://github.com/frankaemika/libfranka.git --recursive
cd libfranka
```

## Checkout the Specific Version

```bash
git checkout 0.13.2
git submodule update --init --recursive
```

### Create a Build Directory and Navigate into It

```bash
mkdir build
cd build
```

### Configure the Build

```bash
cmake -DCMAKE_BUILD_TYPE=Release ..
```

### Build the Library

```bash
cmake --build .
```

### Install the Library

```bash
sudo make install
```

### Verify the installation

```bash
ls /usr/local/lib/libfranka.so.0.13.2
ls /usr/local/include/franka
ls /usr/local/lib/cmake/Franka
```


## Changelog
- **Inertia Addition**: Inertia properties were added to the URDF file to
  ensure proper functioning of the robot model in simulations.
- **Discontinuation of Gazebo Support**: Gazebo support was discontinued in the
  ROS 2 version of the package, which was previously available in ROS 1.
  Necessary adjustments were made to bridge the changes and ensure
  compatibility with ROS 2.
