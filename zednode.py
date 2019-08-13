#!/usr/bin/env python
# license removed for brevity
import rospy
import sys
import cv2

from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

from zedcv2 import Camera

class image_converter:

    def __init__(self):
        # ROS
        self.image_pub = rospy.Publisher("/zed/zed_node/rgb/image_rect_color", Image, queue_size=1)
        self.bridge = CvBridge()
        # zedcv2
        self.zed = Camera()
        self.zed.set_resolution("720p")    # "2K", "1080p", "720p", "WVGA"
        self.zed.set_eye("left")         # "left", "right", "both"

    def get_image(self):
        # Capture frame-by-frame
        cv2_image = self.zed.retrieve_image()
        self.callback(cv2_image)

    def callback(self, cv2_image):
        try:
            pass
            ros_img = self.bridge.cv2_to_imgmsg(cv2_image, "bgr8")
            self.image_pub.publish(ros_img)
        except CvBridgeError as e:
            print(e)

def main(args):
    ic = image_converter()
    
    rospy.init_node('zedcv2_raw_image', anonymous=True)

    r = rospy.Rate(30) # 30hz, same as zed-ros-wrapper
    while not rospy.is_shutdown():
        ic.get_image()
        r.sleep()


if __name__ == '__main__':
    main(sys.argv)