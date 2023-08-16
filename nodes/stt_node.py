#! /usr/bin/env python3

import os
import rospkg
import rospy
import sounddevice as sd
import whisper
from scipy.io.wavfile import write
from theta_speech.srv import SpeechToText, SpeechToTextResponse


PACK_DIR = rospkg.RosPack().get_path("theta_speech")

def record(req):
    sample_rate = 16000
    duration = 5

    # record start
    rospy.loginfo("Record Start: ")
    rospy.loginfo("listening...")
    recording = sd.rec(int(duration *sample_rate),samplerate=sample_rate,channels=1)
    sd.wait()

    # outputs audio in file
    write("output_whisper.wav", sample_rate, recording)
    text_response = whisp()
    return SpeechToTextResponse(text = text_response)

# whisper func
def whisp():
    audio = os.path.abspath("output_whisper.wav")
    # Models
    # tiny - base - small - medium
    m = whisper.load_model("small.en")
    
    # transcribe audio
    text = whisper.transcribe(model=m,audio=audio)
    
    delete_file(audio)

    return text['text']
    

# deletes file
def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("no file")
        

if __name__ == '__main__':
    rospy.init_node('stt_server', anonymous=True)
    rospy.Service("services/speechToText", SpeechToText , record)
    rospy.spin()