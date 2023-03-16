#include <ros/ros.h>
#include <std_msgs/String.h>

int main (int argc, char **argv)
{
    ros::init(argc, argv, "robot_news_radio_transmitter_cpp");
    ros::NodeHandle nh;

    ros::Publisher pub = nh.advertise<std_msgs::String>("/robot_news_radio_cpp", 10);

    ros::Rate rate (3);

    while (ros::ok()){
        std_msgs::String msg;
        msg.data = "Hi, This is Kong from the robot news Radio";
        pub.publish(msg);
        rate.sleep();


    }


}