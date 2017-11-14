import glob
from PIL import Image
from PIL import *
import cv2
import os

def DetectFace(image, faceCascade, returnImage=False):
    min_size = (20,20)
    haar_scale = 1.1
    min_neighbors = 3
    haar_flags = 0
    cv2.cv.EqualizeHist(image, image)
    faces = cv2.cv.HaarDetectObjects(
            image, faceCascade, cv2.cv.CreateMemStorage(0),
            haar_scale, min_neighbors, haar_flags, min_size
        )

    if faces and returnImage:
        for ((x, y, w, h), n) in faces:
            pt1 = (int(x), int(y))
            pt2 = (int(x + w), int(y + h))
            cv2.cv.Rectangle(image, pt1, pt2, cv2.cv.RGB(255, 0, 0), 5, 8, 0)

    if returnImage:
        return image
    else:
        return faces

def pil2cvGrey(pil_im):
    pil_im = pil_im.convert('L')
    cv_im = cv2.cv.CreateImageHeader(pil_im.size, cv2.IPL_DEPTH_8U, 1)
    cv2.cv.SetData(cv_im, pil_im.tobytes(), pil_im.size[0]  )
    return cv_im

def cv2pil(cv_im):
    return Image.frombytes("L", cv2.cv.GetSize(cv_im), cv_im.tostring())

def imgCrop(image, cropBox, boxScale=1):

    # Calculate scale factors
    xDelta=max(cropBox[2]*(boxScale-1),0)
    yDelta=max(cropBox[3]*(boxScale-1),0)

    PIL_box=[cropBox[0]-xDelta, cropBox[1]-yDelta, cropBox[0]+cropBox[2]+xDelta, cropBox[1]+cropBox[3]+yDelta]

    return image.crop(PIL_box)

def faceCrop(dest, imagePattern,boxScale=1):
    faceCascade = cv2.cv.Load('haarcascade_frontalface_default.xml')
    if not os.path.exists(dest):
        os.makedirs(dest)
    imgList=glob.glob(imagePattern)
    if len(imgList)<=0:
        print imagePattern + ': No Images Found'
        return
    print len(imgList)
    for img in imgList:
        fileName = img.split('/')[-1]
        print 'croping: ' + fileName
        if fileName[0] == '.':
            continue
        pil_im=Image.open(img)
        cv_im=pil2cvGrey(pil_im)
        faces=DetectFace(cv_im,faceCascade)
        if faces:
            n=1
            for face in faces:
                croppedImage=imgCrop(pil_im, face[0],boxScale=boxScale)
                fname,ext=os.path.splitext(img)
                croppedImage.save(dest + '/' + fileName)
                n+=1
        else:
            print 'No faces found:', img

def runFaceCrop(dest, imageFilePath, fileName):
    pil_im=Image.open(imageFilePath)
    cv_im=pil2cvGrey(pil_im)
    faceCascade = cv2.cv.Load('haarcascade_frontalface_default.xml')
    face_im=DetectFace(cv_im,faceCascade, returnImage=True)
    img=cv2pil(face_im)
    if not os.path.exists(dest):
        os.makedirs(dest)
    img.save(dest + '/' + fileName)
