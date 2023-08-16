#! /usr/bin/env python3
import os
import pvporcupine
import rospy
import playsound as ps
import rospkg
from pvrecorder import PvRecorder
from std_msgs.msg import Empty


def hotword():
    rospy.init_node('hotword_detect', anonymous=True)
    pub = rospy.Publisher('/hotword', Empty, queue_size=1)
    #rate = rospy.Rate(1)

    #Access key
    key = "/7tRhhsTIGC6F0L6x2sJ1L2Is8d4OVZnYOMVLm/YljgwgyPvfd10NA=="

    #DIR
    PACK_DIR = rospkg.RosPack().get_path("theta_speech")
    KEYWORD_DIR = os.path.join(PACK_DIR,"resources/Hey-Theta_en_linux_v2_2_0.ppn")
    DIN_DIR = os.path.join(PACK_DIR,"resources/bark.ogg")

    keyword_p = KEYWORD_DIR
    din =  DIN_DIR
    pp = pvporcupine.create(access_key=key, keyword_paths=[keyword_p],  sensitivities=[0.9])
    recorder = PvRecorder(device_index=-1,frame_length=pp.frame_length)

    print("Say hotword:")

    detect =  False

    while not detect:
        recorder.start()
        pcm = recorder.read()
        audio_frame = pcm
        keyword_index = pp.process(audio_frame)

        if keyword_index >=0:
            
            pub.publish(Empty())
            rospy.loginfo("Detected")
            detect = True
            ps.playsound(din) 
            recorder.stop()
            #rate.sleep()

if __name__ == '__main__':
    try:
        hotword()
    except rospy.ROSInterruptException:
        pass               
