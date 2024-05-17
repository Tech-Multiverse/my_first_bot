# My First ROS2 Robot Simulation

Learn more about this project at https://tech-multiverse.com/projects/learning-how-to-simulate-robots-with-ros2/



**Follow these steps to get everything up and running:**

- In VS Code, with the <a href="https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers" target="_blank"> Dev Containers extention</a> installed, click the blue button in the lower left and choose "reopen with container". 

- Once the container build finishes, open a terminal and navigate to "dev_ws" folder and build the my_bot packge with `colcon build --symlink-install`

- Source the new setup file with `source install/setup.bash`

- Launch the project and open the Gazebo simulator with `ros2 launch my_bot launch_sim.launch.py`

- Open a new terminal and launch the RVIZ simulator with `rviz2`.

- Open the RVIZ configuration file "/dev_ws/src/my_bot/drive_bot.rviz" to load the bot into the scene.

- Open another terminal and lauch the contros with `ros2 run teleop_twist_keyboard teleop_twist_keyboard`.

- Use the "u" and "o" keys to have the robot do circles, otherwise it's easy to lose track of it visually.

Here's a screenshot of this project running:

<img src="/images/ros2_robot_sim_static.png" width="720">
