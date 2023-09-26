#! /usr/bin/env python3
import sys
import os
import rospy
import rospkg
from transformers import pipeline
from theta_speech.srv import QuestionAnswer, QuestionAnswerResponse

PACK_DIR = rospkg.RosPack().get_path("theta_speech")
TEXT_DIR = os.path.join(PACK_DIR,"resources/context.txt")

def answer_question(model, question, context):
    qa_model = pipeline("question-answering", model=model)
    rospy.logwarn("log3")
    a = qa_model(question = question, context = context)
    rospy.logwarn("log4")
    return a['answer']

# reads context file
def archive():
    try:
        with open(TEXT_DIR, 'r') as file:
            text = file.read()
            return text
    except Exception as e:
        print("Not found.")

def question_answering(question):
    # fastest model
    model = "deepset/tinyroberta-squad2"

    context = archive()
    answer = answer_question(model, question.question, context)

    return QuestionAnswerResponse(answer = answer)

if __name__ == "__main__":
    
    rospy.init_node('question_answering', anonymous=True)
    
    s = rospy.Service("services/questionAnswering", QuestionAnswer, question_answering)
    rospy.spin()
