cmake_minimum_required(VERSION 3.5)
project(aloam_velodyne)

set(CMAKE_BUILD_TYPE "Release")
set(CMAKE_CXX_FLAGS "-std=c++17")
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -Wall -g")


find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(tf2_ros REQUIRED)
#find_package(Eigen3 REQUIRED)
find_package(PCL REQUIRED)
find_package(Ceres REQUIRED)

include_directories(
        include
        ${PCL_INCLUDE_DIRS}
        ${CERES_INCLUDE_DIRS}
)

set(dependencies rclcpp geometry_msgs nav_msgs std_msgs sensor_msgs tf2_ros)

add_executable(ascanRegistration src/scanRegistration.cpp)
ament_target_dependencies(ascanRegistration ${dependencies})
target_link_libraries(ascanRegistration ${PCL_LIBRARIES})
install(TARGETS ascanRegistration DESTINATION lib/${PROJECT_NAME})

add_executable(alaserOdometry src/laserOdometry.cpp)
ament_target_dependencies(alaserOdometry ${dependencies})
target_link_libraries(alaserOdometry ${PCL_LIBRARIES} ${CERES_LIBRARIES})
install(TARGETS alaserOdometry DESTINATION lib/${PROJECT_NAME})
#
add_executable(alaserMapping src/laserMapping.cpp)
ament_target_dependencies(alaserMapping ${dependencies})
target_link_libraries(alaserMapping ${PCL_LIBRARIES} ${CERES_LIBRARIES})
install(TARGETS alaserMapping DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})

ament_package()

