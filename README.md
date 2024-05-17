# My First ROS2 Robot Simulation

Learn more about this project at <a href="https://tech-multiverse.com/projects/learning-how-to-simulate-robots-with-ros2/" target="_blank">Tech-Multiverse</a>.

<hr />

Thanks to <a href="https://github.com/joshnewans" target="_blank">@joshnewans</a> and his tutorials at <a href="https://articulatedrobotics.xyz/">Articulated Robots</a>, which is what inspired this repo!

<hr />

This repo combines what Josh demos in his <a href="https://youtu.be/dihfA7Ol6Mw?si=zgaU7BsfSOhUVXmX">video about dev containers</a>, with his <a href="https://articulatedrobotics.xyz/tutorials/mobile-robot/project-overview" target="_blank">Build a Mobile Robot with ROS</a> project - without the hardware. 


The result is a containerized robot simulation starter template to kick-off further exploration into using URDF to describe robots and learning how to work with ROS2.

After cloning this repo, and following the directions below, you will have:
- Gazebo Simulation with a starter bot spawned and ready for commands.
- RViz robot visualizer representing the state of the robot, and each component, in relation to the "world".
- An example URDF (XML) description of the "box bot" from the project.
- The ability to control your robot with terminal commands:
  - i = forward
  - , = back
  - u = turn left
  - o = turn right
  - etc...


 Here's a screenshot of this project:

<img src="/images/ros2_robot_sim_static.png" width="720">

<a href="https://youtu.be/V5jJtAAGXfY?si=Gs6j7zukuCje9ydt" target="_blank">Here's a video of everything running!</a>
<hr />

**Follow these steps to get everything up and running:**

- In VS Code, with the <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers" target="_blank"> Dev Containers extention</a> installed, click the blue button in the lower left and choose "reopen with container". 

- Once the container build finishes, open a terminal and navigate to "dev_ws" folder and build the my_bot packge with `colcon build --symlink-install`

- Source the new setup file with `source install/setup.bash`

- Launch the project and open the Gazebo simulator with `ros2 launch my_bot launch_sim.launch.py`

- Open a new terminal and launch the RVIZ visualizer with `rviz2`.

- Open the RVIZ configuration file "/dev_ws/src/my_bot/drive_bot.rviz" to load the bot into the scene.
  
- Open a third teminal and start the transform log with `ros2 topic echo /tf`

- Open a fourth terminal and lauch the controls with `ros2 run teleop_twist_keyboard teleop_twist_keyboard`.

- Use the "u" and "o" keys to have the robot do circles, otherwise it's easy to lose track of it visually.
