#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import uuid

# settting of import messaging
sys.path.append("messaging")
from messaging import *

cls = Audio2TextServiceResMessaging
rec1 = cls().connect_and_basic_get_record()
if rec1 is None:
    sys.exit(0)
# transform rec
rec2 = Text2AdviceRecord(rec1.id, rec1.audio2text, None)
rec2.timestamp = rec1.timestamp

Text2AdviceServiceReqMessaging().connect_and_basic_publish_record(rec2)
