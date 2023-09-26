#!/usr/bin/env python3
import rospy
from theta_speech.srv import SpeechToText, SpeechToTextResponse
import rospkg
from std_msgs.msg import String
from std_msgs.msg import Empty
import time

PACK_DIR = rospkg.RosPack().get_path("theta_speech")

tts_pub  = rospy.Publisher('/textToSpeech', String, queue_size=10)
face_pub = rospy.Publisher('/hri/affective_loop', String, queue_size=10)

def get_question(self):
    face =  String
    face.data = "littleHappy'"
    face_pub.publish(face)
    time.sleep(5)
    
    tts_pub.publish('what is your question?')
    time.sleep(5)
    
    rospy.logwarn("ready")
    rospy.wait_for_service("services/speechToText")
    speech_to_text = rospy.ServiceProxy("services/speechToText", SpeechToText)
    text = speech_to_text()
    rospy.loginfo(text.text)
    # rospy.sleep(3)

    tts_pub.publish(text.text)
    # rospy.sleep(3)

    

    # while not rospy.is_shutdown():
    #     try:
            
    #         #rospy.loginfo(speech_to_text.text)
            
    #         text = speech_to_text()
    #         rospy.loginfo(text.text)
    #         rate.sleep()
    #     except rospy.ServiceException as e:
    #         print("Service call failed:", str(e))

# def call_speech_to_text_service():
#     rospy.init_node("")
#     rospy.wait_for_service("services/speechToText")
#     rate = rospy.Rate(1)
#     while not rospy.is_shutdown():
#         try:
#             speech_to_text = rospy.ServiceProxy("services/speechToText", SpeechToText)
#             #rospy.loginfo(speech_to_text.text)
            
#             text = speech_to_text()
#             rospy.loginfo(text.text)
#             rate.sleep()
#         except rospy.ServiceException as e:
#             print("Service call failed:", str(e))
            
if __name__ == "__main__":
    rospy.init_node("speech_recognition_task")

    rospy.Subscriber("hotword", Empty, get_question)

    while not rospy.is_shutdown():
        pass

