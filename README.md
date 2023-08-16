# theta_speech

## 1. Description

This package contains the necessary means for Theta listen and speak. (speech-to-text and text-to-speech). 


## 2. Install Requirements

```
$ pip install -r requirements.txt
```

## 3. Nodes


We developed some nodes that will go help to make the speech-to-text (STT) and text-to-speech (TTS).

The **hotword_node** is a ROS Topic that, when called, listens and waits for a keyword.

The **stt_node** is a ROS Service that, when called, listens and returns a text.

The **tts_node** is a ROS Service and a ROS Topic that receives a text and the robot speaks respectively what was received.


## 4. Services
- SpeechToText.srv returns a text as string.
