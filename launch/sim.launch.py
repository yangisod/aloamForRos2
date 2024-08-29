from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
import yaml


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='aloam_velodyne',
            executable='ascanRegistration',
            name='ascanRegistration'
        ),
        Node(
            package='aloam_velodyne',
            executable='alaserOdometry',
            name='alaserOdometry'
        ),
        Node(
            package='aloam_velodyne',
            executable='alaserMapping',
            name='alaserMapping'
        )
    ])
