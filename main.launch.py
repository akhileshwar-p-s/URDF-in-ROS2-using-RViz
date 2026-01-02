import os
import launch
import launch_ros
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription

def generate_launch_description():
    pkg_share= launch_ros.substitutions.FindPackageShare(package='robot_project').find('robot_project')
    default_model_path= os.path.join(pkg_share, 'models/urdf/robot_project.xacro')
    default_rviz_config= os.path.join(pkg_share, 'config/rviz_config.rviz')
    
    state_publisher_launch_dir= os.path.join(pkg_share, 'launch')
    rviz_launch_dir= os.path.join(pkg_share, 'launch')

#state publishers launch
    state_publisher_launch_cmd= IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                state_publisher_launch_dir, 
                'state_publisher.launch.py'
            )
        )

    )

#RViz launch
    rviz_launch_cmd= IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                rviz_launch_dir,
                'rviz.launch.py'
            )
        )
    )

    return LaunchDescription((
        launch.actions.DeclareLaunchArgument(
            name= 'model',
            default_value= default_model_path,
            description= 'Absolute path to Robot URDF'
       ),
       launch.actions.DeclareLaunchArgument(
           name= 'rviz_config',
           default_value= default_rviz_config,
           description= 'Absolute path to RViz config file'
       ),

       state_publisher_launch_cmd,
       rviz_launch_cmd

    )
    )
