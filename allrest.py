#! /usr/local/bin/python  -*- coding: UTF-8 -*-
import json
from pprint import pprint
import random
def restaurant():
    rest = [u'كل المطاعم اهي يا عم']
    rest_str = {"allrest": rest, "do": "", "buttons": {}}
    print(rest_str["allrest"])