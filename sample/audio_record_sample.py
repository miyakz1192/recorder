#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# settting of import messaging
sys.path.append("messaging")
from messaging import *

rec = RecoderServiceMessaging().connect_and_basic_get_record()

print(rec.timestamp)
print(len(rec.raw_audio_byte))

with open("/tmp/sample.wav", "wb") as f:
    f.write(rec.raw_audio_byte)
