# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 15:52:41 2017

@author: Meidi
"""

import rawpy
import imageio

def imageCompress(root, directory, image):
    raw = rawpy.imread(root + directory + '/' + image)
    rgb = raw.postprocess()
    if not os.path.exists(root + 'Faces/' + directory):
        os.makedirs(root + 'Faces/' + directory)
    fn = filename.split('.')[0]
    newFilename = root + 'Faces/' + directory + '/' + fn + '.jpg'
    imageio.imsave(newFilename, rgb)


directory = '../Face Image/'

for dirname in os.listdir(directory):
    for filename in os.listdir(directory + dirname):
        if filename.endswith(".nef"):
            imageCompress(directory, dirname, filename)



