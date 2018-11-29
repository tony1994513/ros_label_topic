from ros_label_topic.srv import label_info,label_infoRequest
import rospy
import sys


def main(): 
    rospy.init_node("tag_topic_label_client", anonymous=True)
    rospy.wait_for_service('label_topic_service')
    client = rospy.ServiceProxy('label_topic_service', label_info)
    rospy.loginfo("input the lable name")

    # label_name = raw_input()
    # req = label_infoRequest()
    # req.label_name = label_name
    rospy.loginfo(rospy.Time.now())
    req1 = req = label_infoRequest()
    req1.label_name = "test_1"
    res = client(req1)
    rospy.sleep(1)
    req2 = req = label_infoRequest()
    req2.label_name = "test_2"
    rospy.loginfo(rospy.Time.now())
    res = client(req2)
    





if __name__ == '__main__':
    sys.exit(main())
