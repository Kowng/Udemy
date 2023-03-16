#include <ros/ros.h>

int main (int argc , char **argv)
{
    ros::init(argc, argv, "my_firstcpp_node_cpp");
    ros::NodeHandle nh;
    ROS_INFO("Node has been started");

    ros::Rate rate(10);

    while (ros::ok()){
        ROS_INFO("Hello");
        rate.sleep();
    }
}