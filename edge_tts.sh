#!/usr/bin/bash

edge-tts --text "$1" --voice en-US-JennyNeural --write-media temp.mp3
ffplay -nodisp -autoexit temp.mp3
rm temp.mp3
