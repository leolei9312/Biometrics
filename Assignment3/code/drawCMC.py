# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 10:10:28 2017

@author: Meidi
"""

import os
import matplotlib.pyplot as plt
from ast import literal_eval as make_tuple
import json

recognition_matrix = {} # key: prob personId value: list of tuples(gallery personId, confidence)

json_data=open('recognition.json').read()

recognition_matrix = json.loads(json_data)

CMCvalue = []
CMCvalue.append(0.0)
total_prob = len(recognition_matrix)
for i in range(1, total_prob + 1):
    count = 0
    for personId in recognition_matrix.keys():
        print personId
        valueList = recognition_matrix[personId]
        for j in range(i):
            if j < len(valueList):
                if valueList[j][0] == personId:
                    count += 1
                    break # next person
    print count / float(total_prob)
#    break
    CMCvalue.append(count / float(total_prob))

plt.plot(range(0, total_prob + 1), CMCvalue)

   