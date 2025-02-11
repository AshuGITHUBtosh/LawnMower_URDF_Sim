from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Step 1: Include the original launch file from the 'robot_model' package
    grass_cutter_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('robot_model'), 'launch', 'grass_cutter.launch.xml')
        )
    )

    # Step 2: Add a timer for 5 seconds to delay the 'path_mapper.py' node from the 'manual_ctrl' package
    path_mapper_node = TimerAction(
        period=5.0,  # 5-second delay
        actions=[
            Node(
                package='manual_ctrl',  # This is where 'path_mapper.py' resides
                executable='path_mapper',  # The file should be executable without the '.py' extension
                name='path_mapper',
                output='screen'
            )
        ]
    )

    # Return the launch description with both actions
    return LaunchDescription([
        grass_cutter_launch,
        path_mapper_node
    ])
