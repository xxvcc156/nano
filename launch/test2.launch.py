from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os

def generate_launch_description():
  param_dir = LaunchConfiguration(
    'param_dir',
    default=os.path.join(
        get_package_share_directory('my_package'),
        'param',
        'turtlesim.yaml'))

  return LaunchDescription([
    DeclareLaunchArgument(
      'param_dir',
      default_value=param_dir,
    ),
    Node(
      package='turtlesim',
      executable='turtlesim_node',
      parameters=[param_dir]
    ),
    ExecuteProcess(
      cmd=['ros2 service call '
          '/spawn ',
          'turtlesim/srv/Spawn ',
          '"{x: 3, y: 7, theta: 0.2, name: ''turtle2''}"'],
      shell=True
    ),
		Node(
      package='my_package',
      executable='moveturtle2',
    )
	])
