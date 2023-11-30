#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import uuid

# settting of import messaging
sys.path.append("messaging")
from messaging import *

cls = Audio2TextServiceReqMessaging

rec1 = RecoderServiceMessaging().connect_and_basic_get_record()
# transform rec
rec2 = Audio2TextRecord("ident1", rec1.raw_audio_byte, "")
rec2.timestamp = rec1.timestamp

print(rec1.timestamp)
print(len(rec1.raw_audio_byte))

Audio2TextServiceReqMessaging().connect_and_basic_publish_record(rec2)
