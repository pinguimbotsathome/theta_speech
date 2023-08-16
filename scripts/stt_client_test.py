#!/usr/bin/env python3
import rospy
from theta_speech.srv import SpeechToText, SpeechToTextResponse
import rospkg

PACK_DIR = rospkg.RosPack().get_path("theta_speech")

def call_speech_to_text_service():
    rospy.init_node("stt_client")
    rospy.wait_for_service("services/speechToText")
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        try:
            speech_to_text = rospy.ServiceProxy("services/speechToText", SpeechToText)
            #rospy.loginfo(speech_to_text.text)
            
            text = speech_to_text()
            rospy.loginfo(text.text)
            rate.sleep()
        except rospy.ServiceException as e:
            print("Service call failed:", str(e))
            
if __name__ == "__main__":
    call_speech_to_text_service()
