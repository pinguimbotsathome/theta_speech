#! /usr/bin/env python3
import sys
import os
import rospy
import rospkg
from transformers import pipeline

PACK_DIR = rospkg.RosPack().get_path("theta_speech")
TEXT_DIR = os.path.join(PACK_DIR,"resources/context.txt")

def answer(model, question, context):
    rospy.init_node('question_answering_node', anonymous=True)

    qa_model = pipeline("question-answering", model=model)
    a = qa_model(question = question, context = context)
    print(a['answer'])

# reads context file
def archive():
    try:
        with open(TEXT_DIR, 'r') as file:
            text = file.read()
            return text
    except Exception as e:
        print("Not found.")

def main(question):
    # fastest model
    model = "deepset/tinyroberta-squad2"
    context = archive()
    answer(model, question, context)

if __name__ == "__main__":
    try:
        input_string = sys.argv[1]
        main(input_string) 
    except rospy.ROSInterruptException:
        pass 
