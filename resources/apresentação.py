#!/usr/bin/env python3
import rospy
from theta_speech.srv import SpeechToText
from std_msgs.msg import String
from std_msgs.msg import Empty
import time

tts_pub  = rospy.Publisher('/textToSpeech', String, queue_size=10)
face_pub = rospy.Publisher('/hri/affective_loop', String, queue_size=10)

def start():
    rospy.logwarn("Start")
    face_pub.publish('littleHappy')

    tts_pub.publish('Ola pessoal, sou o theta')
    time.sleep(2)
    tts_pub.publish('Finish')
    face_pub.publish('happy')
    time.sleep(1)
 

if __name__ == "__main__":
    rospy.init_node("speech_recognition_task")
    start()
    while not rospy.is_shu
