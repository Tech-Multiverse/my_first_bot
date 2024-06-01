FROM osrf/ros:foxy-desktop

# Set the display host
# You may need to make sure xhost is running locally if you find the GUIs don't load.
# I have to run "C:\Program Files\VcXsrv\xlaunch.exe" with access control disabled for everything to work.
ENV DISPLAY=host.docker.internal:0.0

# Add vscode user with same UID and GID as your host system
# (copied from https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user#_creating-a-nonroot-user)
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
# Switch from root to user
USER $USERNAME

# Add user to video group to allow access to webcam
RUN sudo usermod --append --groups video $USERNAME

# Update all packages
RUN sudo apt update && sudo apt upgrade -y

# Install Git
RUN sudo apt install -y git

# Rosdep update
RUN rosdep update

# Install Gazebo ROS packages and Xacro
RUN sudo apt install -y \
    ros-foxy-gazebo-ros-pkgs \
    ros-foxy-xacro \
    ros-foxy-ros2-control \
    ros-foxy-ros2-controllers \
    && rm -rf /var/lib/apt/lists/*

# Source the ROS setup file
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc
