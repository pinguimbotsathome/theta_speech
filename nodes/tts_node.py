#! /usr/bin/env python3
import playsound as ps
import os
import rospy
from TTS.api import TTS
from std_msgs.msg import String
import rospkg

def coqui(text, model):
    tts = TTS(model)
    
    # path to file
    PACK_DIR = rospkg.RosPack().get_path("theta_speech")
    OUTPUT_DIR =  os.path.join(PACK_DIR, "resources/output.wav")
    path = OUTPUT_DIR 
    
    # transforms to audio and saves in wav format
    wav  = tts.tts_to_file(text=text, speed=2, file_path=path)
    
    # plays audio
    ps.playsound(sound=path)
    # deletes the file
    delete_file(path)

# deletes file
def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("no file")

# tts main func
def tts(text): 
    ## Models - english only
    ## 7 - 12 - 13 - 23(jenny)
    n = 23
    # loads model
    model = TTS.list_models()[n]
    # coqui
    coqui(text.data,model)


if __name__ == "__main__":
    rospy.init_node('textToSpeech', anonymous=True)
    sub = rospy.Subscriber('/textToSpeech', String, tts)
    rospy.spin()


