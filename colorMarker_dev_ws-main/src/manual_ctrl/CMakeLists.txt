cmake_minimum_required(VERSION 3.8)
project(manual_ctrl)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(ament_cmake_python REQUIRED)

ament_python_install_package(${PROJECT_NAME})

install(
  PROGRAMS
    manual_ctrl/path_mapper.py
    manual_ctrl/control_gui.py
    DESTINATION lib/${PROJECT_NAME}
)

install (
  DIRECTORY manual_ctrl
  DESTINATION share/manual_ctrl/
)

ament_package()
