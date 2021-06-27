#!/bin/bash

apt-get update && apt-get install espeak -y

pip3 install pyttsx3 

apt-get install alsa-utils -y

printf "defaults.pcm.card 3 \ndefaults.ctl.card 3 \n" > /etc/asound.conf



python3 ./my_detectnet.py  --model=/jetson-inference/python/training/detection/ssd/models/saif1/ssd-mobilenet.onnx --labels=/jetson-inference/python/training/detection/ssd/models/saif1/labels.txt --input-blob=input_0 --output-cvg=scores --output-bbox=boxes /dev/video1
