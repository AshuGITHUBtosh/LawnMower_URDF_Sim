# Lawn Mower Bot Simulation in Gazebo
## Overview
This project simulates a manually controlled lawn mower bot in Gazebo using ROS2. As the rover moves, the system subscribes to its odometry data and dynamically traces its path on an empty canvas, providing real-time visualization of its trajectory. This allows users to track the movement of the rover while operating it manually.
## Features
 - Gazebo simulation of an autonomous lawn mower bot.
 - Odometry-based path tracking to visualize the rover's movement.
 - ROS2 integration for real-time data processing.
 - Custom visualization of the bot’s path using an empty canvas.

 ## Execution
 - ``` cd LawnMower_URDF_Sim/colorMarker_dev_ws-main ```
 - ``` colcon build ```
 - ``` source install/setup.bash ```
 - ``` cd src/manual_ctrl/manual_ctrl ```
 - ``` python3 control_gui.py ```
   
   the above commands should open a UI, click on start recording, it will open a gazebo simulation and a empty canvas.

   
   - open a new a terminal
   - ``` ros2 run teleop_twist_keyboard teleop_twist_keyboard ```
   - when you close the UI it will save the path traced in maps folder in
   - ``` src/manual_ctrl/manual_ctrl ```
 
