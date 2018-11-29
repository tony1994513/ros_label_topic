#!/usr/bin/env python
from ros_label_topic.srv import label_info,label_infoRequest
import rospy
import sys
import ipdb

def main(): 
    rospy.init_node("tag_topic_label_client", anonymous=True)
    rospy.wait_for_service('label_topic_service')
    client = rospy.ServiceProxy('label_topic_service', label_info)
    req = label_infoRequest()
    rospy.loginfo("using comma as tag separator. \nlable tags:  ")
    raw_name = raw_input()
    split_names = raw_name.split(',')
    for name in split_names:
        req.label_names.append(name.strip()) # delete space in string
    res = client(req)
    

if __name__ == '__main__':
    sys.exit(main())
