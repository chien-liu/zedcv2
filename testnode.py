#!/usr/bin/env python
from __future__ import print_function
import rospy
import sys
import cv2

from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()

def callback(data):
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    print("shape: {}".format(cv_image.shape))
    # rospy.loginfo("")
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('testnode', anonymous=True)

    rospy.Subscriber("/zed/zed_node/rgb/image_rect_color", Image, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()