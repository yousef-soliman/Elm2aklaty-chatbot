#! /usr/local/bin/python  -*- coding: UTF-8 -*-
import json
from pprint import pprint
import random
def eat():
        msg = [u'عارف مكانك ولا هتتعبنا',u'طيب اشطة حدد مكانك',u'طب يلا عشان تعزمني ']
        randmsg=random.choice(msg)
        json_string = {"message": randmsg,"do":"locate()",
                       "buttons":[{"name":"fish","value":u'سمك'},
                                  {"name":"meat","value":u'لحمة'},
                                  {"name": "italian", "value": u'ايطالي'}
                                  ]
                        }
        return (json_string["message"])
