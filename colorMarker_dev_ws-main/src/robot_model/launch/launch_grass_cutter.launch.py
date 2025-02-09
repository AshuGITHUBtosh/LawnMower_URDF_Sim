from launch import LaunchDescription
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, TimerAction
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    urdf_file_path = '$(find-pkg-share robot_model)/urdf/lawm_mower.urdf.xacro'

    # Use the installed path for the RViz configuration file
    rviz_config_file = PathJoinSubstitution([
        get_package_share_directory('bringup'),
        'rviz',
        'rviz_config.rviz'
    ])

    return LaunchDescription([
        # Declare the RViz configuration argument
        DeclareLaunchArgument(
            name='rviz_config',
            default_value=rviz_config_file,
            description='Full path to the RViz config file to use'
        ),
        
        # Launch Gazebo with an empty world
        Node(
            package='gazebo_ros',
            executable='/usr/bin/gzserver',
            output='screen',
            arguments=['-s', 'libgazebo_ros_factory.so', '--verbose', 'empty.world']
        ),
        Node(
            package='gazebo_ros',
            executable='/usr/bin/gzclient',
            output='screen'
        ),
        
        # Launch the joint state publisher
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            output='screen'
        ),
        
        # Load the URDF into the parameter server
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': Command(['xacro ', urdf_file_path])}],
        ),
        
        # Spawn the robot in Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            output='screen',
            arguments=['-entity', 'lawn_mover', '-file', urdf_file_path]
        ),
        
        # Launch RViz
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', LaunchConfiguration('rviz_config')]
        ),
    ])
