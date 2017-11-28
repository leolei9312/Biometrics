# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:12:58 2017

@author: Meidi
"""
import os
# import matplotlib.pyplot as plt
from compareFaces import *
import numpy as np
import csv

gallery_dir  = '../gallery_face/'
probe_dir = '../prob_face/'

genuine = {}
imposter = {}

with open('ConfidenceResult.csv', 'a') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for prob_folder in os.listdir(probe_dir):
        confidenceRes = []
        if prob_folder[0] == '.':
            continue
        probList = os.listdir(probe_dir + prob_folder)
        if len(probList) > 3:
            randPic = np.random.choice(probList, 3, replace=False)
        else:
            randPic = probList
#        print 'prob folder: ' +prob_folder # personId in probe
        confidenceRes.append((prob_folder, []))
        for filename in randPic:
            if filename[0] == '.':
                continue
            image1 = probe_dir + prob_folder + '/' + filename
            for gal_folder in os.listdir(gallery_dir):
                if gal_folder[0] == '.':
                    continue
#                print 'gallery folder: ' + gal_folder # personId in gallery
                picList = os.listdir(gallery_dir + gal_folder)
                if len(picList) > 15:
                    randomPic = np.random.choice(picList, 15, replace=False)
                else:
                    randomPic = picList
                for fn in randomPic:
                    if fn[0] == '.':
                        continue
                    print 'file name: ' + fn
                    image2 = gallery_dir + gal_folder + '/' + fn
                    try:
                        result = compare(image1, image2)
                    except:
                        print 'compare error'
                    if result is not None:
                        result = 100 - int(round(result))
                        #save to confidence csv
                        confidenceRes.append((gal_folder, result))
    #                    print result
                        if(prob_folder == gal_folder):
                            if(result not in genuine.keys()):
                                genuine[result] = 0
                            genuine[result] = genuine[result] + 1
                        else:
                            if(result not in imposter.keys()):
                                imposter[result] = 0
                            imposter[result] = imposter[result] + 1
            print genuine
            print imposter
        wr.writerow(confidenceRes)