# theta_speech

## Description

This package contains the necessary means for Theta listen and speak. (speech-to-text and text-to-speech). 

## Install Requirements

```bash
$ pip install -r requirements.txt
```

## 4. Nodes

We developed some nodes that will go help to make the speech-to-text (STT) and text-to-speech (TTS).

The **hotword_node** is a ROS Topic that, when called, listens and waits for a keyword. A possible use to this topic is to make the robot listen a word to make some specific task. We use the _pvporcupine_ Python library to make the recognize (it can be seen in _src/butia_speech/detect_hotword.py_).

The **stt_node** node is a ROS Service that, when called, listens and returns a text of what was spoken.

The **tts_node** node is a ROS Service and a ROS Topic that receive a text and a language (english by default, other languages aren't implemented yet). We developed the node with service and topic because the ROS Topic is no-blocking, so we can make others tasks while the robot speaks. 

## Services
- SpeechToText.srv returns a text as string;
