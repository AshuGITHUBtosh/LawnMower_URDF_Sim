# colorMarker_ws

## The Autonomous Lawn Mower

This project is dedicated to developing an autonomous lawn mower using ROS2. The lawn mower is equipped with various sensors and software components to navigate a defined area, avoid obstacles, and efficiently mow the lawn.

## Installation

To get started with the `colorMarker_ws` project, follow these steps:

### ROS2 Humble Installation

First, ensure that you have ROS2 Humble installed. Follow the [official ROS2 Humble installation guide](https://docs.ros.org/en/humble/Installation.html).

### Install Necessary Dependencies

Run the following commands in your terminal to install the required dependencies:

```bash
# Install colcon-extensions
sudo apt install python3-colcon-common-extensions

# Install Gazebo 11
sudo apt-get install gazebo11 libgazebo11-dev

# Install TurtleBot3
sudo apt-get install ros-humble-turtlebot3*

# Install Nav2 Stack
sudo apt-get install ros-humble-nav2*

# Install SLAM Toolbox
sudo apt-get install ros-humble-slam-toolbox

# Resolve python dependencies
pip install opencv-contrib-python==4.6.0 empy==3.3.4 setuptools==58.2.0
```
## How to run

## Project Structure
```
colorMarker_ws/
├── src/
|   ├── bringup/
│   |   └── launch/
│   ├── robot_model/
│   │   └── urdf/
│   
```
