#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import uuid

# settting of import messaging
sys.path.append("messaging")
from messaging import *

byte_data = b'\xde\xad\xbe\xef'

if len(sys.argv) != 2:
    print("nothing to do!")
    sys.exit(1)

cls = Audio2TextServiceResMessaging

if sys.argv[1] == "publish":
    rec = Audio2TextRecord(uuid.uuid4(), byte_data, "sample_text")
    cls().connect_and_basic_publish_record(rec)
elif sys.argv[1] == "consume":
    rec = cls().connect_and_basic_get_record()
    print(rec.id)
    print(rec.raw_audio_byte)
    print(rec.audio2text)
else:
    print("nothing to do!")
