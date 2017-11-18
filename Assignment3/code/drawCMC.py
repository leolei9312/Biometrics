# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 10:10:28 2017

@author: Meidi
"""

import os
import matplotlib.pyplot as plt
from compareFaces import *

gallery_dir  = '../gallery_face/'
probe_dir = '../prob_face/'

recognition_matrix = {} # key: prob personId value: list of tuples(gallery personId, confidence)

for prob_folder in os.listdir(probe_dir):
#    print prob_folder # personId in probe
    if prob_folder not in recognition_matrix.keys():
        recognition_matrix[prob_folder] = []
    for filename in os.listdir(probe_dir + prob_folder):
        image1 = probe_dir + prob_folder + '/' + filename
        for gal_folder in os.listdir(gallery_dir):
#            print gal_folder # personId in gallery
            for fn in os.listdir(gallery_dir + gal_folder):
                image2 = gallery_dir + gal_folder + '/' + fn
#                print image1
#                print image2
                result = compare(image1, image2)
                if result is not None:
                    result = 100 - int(round(result))
                    val = (gal_folder, result)
                    recognition_matrix[prob_folder].append(val)

# sort each Prob person list
for personId in recognition_matrix.keys():
    data = recognition_matrix[personId]
    recognition_matrix[personId] = sorted(data, key=lambda x: x[1])
#   
CMCvalue = []
total_prob = len(os.listdir(probe_dir))

for i in range(1, total_prob + 1):
    count = 0;
    for personId in recognition_matrix.keys():
        valueList = recognition_matrix[personId]
        for j in range(i):
            if valueList[j][0] == personId:
                count += 1
                continue # next person
    CMCvalue.append(count / float(total_prob))

plt.plot(range(1, total_prob + 1), CMCvalue)

#print 3/float(5)
    
    