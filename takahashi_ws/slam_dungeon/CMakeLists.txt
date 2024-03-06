cmake_minimum_required(VERSION 3.0.2)
project(slam_dungeon)

find_package(OpenCV REQUIRED)
find_package(catkin REQUIRED COMPONENTS
  move_base
  roscpp
  rospy
  std_msgs
  tf
  move_base_msgs
  actionlib
  actionlib_msgs
  geometry_msgs
  nav_msgs
  move_base_msgs
  roslib
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
  include
  ${OpenCV_INCLUDE_DIRS}
)