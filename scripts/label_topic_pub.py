#!/usr/bin/env python
from ros_label_topic.srv import label_info
from ros_label_topic.msg import label_topic_msg
import sys
import rospy
import ipdb

label_names = None
_rate = 1

def label_info_cb(req):
    global label_names
    label_names = req.label_names
    return True

def main():
    global label_names
    rospy.init_node("tag_topic_label", anonymous=True)
    s = rospy.Service('label_topic_service', label_info, label_info_cb)
    pub = rospy.Publisher('tag_label_topic', label_topic_msg, queue_size=1)

    rate = rospy.Rate(_rate)
    
    while not rospy.is_shutdown():
        pub_msg = label_topic_msg()
        if label_names == None:      
            pub_msg.label_names = ""
            pub_msg.time_stamp = rospy.Time.now()
        else:
            pub_msg.label_names = label_names
            pub_msg.time_stamp = rospy.Time.now()
            label_names = None
        pub.publish(pub_msg)
        rate.sleep()

if __name__ == '__main__':
    sys.exit(main())
