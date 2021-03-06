# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:12:58 2017

@author: Meidi
"""
import os
import matplotlib.pyplot as plt
from compareFaces import *
import numpy as np

gallery_dir  = '../test_gallery/'
probe_dir = '../test_prob/'

genuine = {}
imposter = {}

with open('ConfidenceResult.csv', 'a') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for prob_folder in os.listdir(probe_dir):
        confidenceRes = []
    #    print prob_folder # personId in probe
        if prob_folder[0] == '.':
            continue
        confidenceRes.append((prob_folder, []))
        for filename in os.listdir(probe_dir + prob_folder):
            if filename[0] == '.':
                continue
            image1 = probe_dir + prob_folder + '/' + filename
            for gal_folder in os.listdir(gallery_dir):
                if gal_folder[0] == '.':
                    continue
    #            print gal_folder # personId in gallery
                picList = os.listdir(gallery_dir + gal_foler)
                if len(picList) > 15:
                    randomPic = np.random.choice(picList, 15, replace=False)
                else:
                    randomPic = picList
                for fn in randomPic:
                    if fn[0] == '.':
                        continue
                    image2 = gallery_dir + gal_folder + '/' + fn
    #                print image1
    #                print image2
                    try:
                        result = compare(image1, image2)
                    except:
                        print 'error'
                    if result is not None:
                        result = 100 - int(round(result))
                        #save to confidence csv
                        confidenceRes[len(confidenceRes) - 1][1].append((gal_folder, result))
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


#print genuine
#print imposter




#genuine = {96: 6, 80: 1, 82: 2, 83: 3, 84: 3, 85: 10, 86: 3, 87: 3, 88: 7, 89: 5, 90: 10, 91: 10, 92: 11, 93: 6, 94: 12, 95: 8}
#imposter = {10: 6, 15: 10, 20: 4}

# plot genuine and imposter distribution
# gen = sorted(genuine.items())
# x, y = zip(*gen)
# imp = sorted(imposter.items())
# w, z = zip(*imp)
#
# plt.plot(x, y)
# plt.plot(w, z)
# plt.show()
#
# #plot ROC curve
# TMR = []
# FMR = []
#
# sum_gen = sum(y)
# sum_imp = sum(z)
#
# for threshold in range(101):
#     true_match = 0
#     false_match = 0
#     for i in range(threshold + 1):
#         if i in genuine.keys():
#             true_match += genuine[i]
#         if i in imposter.keys():
#             false_match += imposter[i]
#     TMR.append(true_match/float(sum_gen))
#     FMR.append(false_match/float(sum_imp))
#
# plt.plot(FMR, TMR)
