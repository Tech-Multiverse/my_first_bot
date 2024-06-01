from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_share = get_package_share_directory('my_bot')
    default_model_path = os.path.join(pkg_share, 'urdf', 'robot_description.urdf.xacro')

    return LaunchDescription([
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'robot', '-file', default_model_path, '-x', '0', '-y', '0', '-z', '0.5'],
            output='screen'),
        
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('my_bot'), 'launch', 'controller_spawner.launch.py')]),
        ),
    ])
