from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='controller_manager',
            executable='spawner.py',
            arguments=['joint_state_controller', 'joint1_position_controller', 'joint2_position_controller'],
            output='screen'
        ),
    ])
