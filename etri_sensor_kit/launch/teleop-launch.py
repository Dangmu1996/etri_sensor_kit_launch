import os
from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable, IncludeLaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from pathlib import Path
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    ld = LaunchDescription()
    
    velodyne_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            launch_file_path=PathJoinSubstitution([
                FindPackageShare('velodyne'), 'launch', 'velodyne-all-nodes-VLP16-launch.py'
                ]),
            )
        )
    ld.add_action(velodyne_launch)

    imu_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            launch_file_path=PathJoinSubstitution([
                FindPackageShare('bluespace_ai_xsens_mti_driver'), 'launch', 'xsens_mti_node.launch.py'
                ]),
            )
        )
    ld.add_action(imu_launch)

    return ld
