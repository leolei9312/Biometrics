

import cv2 as cv
import numpy as np
import os
import csv
import pandas as pd
from shutil import copyfile
from FaceDetectAndCrop import *



# def copyFile(src, dest, fileName):
#     if not os.path.exists(dest):
#         os.makedirs(dest)
#     copyfile(src, dest + fileName)



def splitName(name):
    return name.split('d')[0]


def processImg(dest, file, fileName):
    print file
    runFaceCrop(dest, file, fileName)



path = "../test/"
if not os.path.exists('../gallery_detect'):
    os.makedirs('../gallery_detect')
if not os.path.exists('../gallery_face'):
    os.makedirs('../gallery_detect')
if not os.path.exists('../prob_detect'):
    os.makedirs('../gallery_detect')
if not os.path.exists('../prob_face'):
    os.makedirs('../gallery_detect')
for folder in os.listdir(path):
    count = 1
    if not os.path.isdir(folder):
        for img in os.listdir(path + folder):
            if img[0] != '.':
                if count % 3 != 0:
                    processImg('../gallery_detect/' + folder, path + folder + '/' + img, img)
                    personName = splitName(img)
                else:
                    processImg('../prob_detect/' + folder, path + folder + '/' + img, img)
                    personName = splitName(img)
                count = count + 1
        faceCrop('../gallery_face/' + folder, '../gallery_detect/' + folder + '/*', boxScale=1)
        faceCrop('../prob_face/' + folder, '../prob_detect/' + folder + '/*', boxScale=1)
