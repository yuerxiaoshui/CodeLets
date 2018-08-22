import os
import sys
import cv2
import time
import re


def gen_regenVideos_dir(projDir, name='regenVideos'):
    regenVideosDir = os.path.join(projDir, name)
    if os.path.exists(regenVideosDir):
        return regenVideosDir
    os.mkdir(regenVideosDir)
    return regenVideosDir

def gen_video_path(dir, name, suffix='.mp4'):
    return os.path.join(dir, name+suffix)

def name_sort(x, y):
    xNum = int(re.sub('\D', '', x))
    yNum = int(re.sub('\D', '', y))
    if xNum < yNum:
        return -1
    if xNum > yNum:
        return 1
    return 0


def regen_video(regenVideoPath, imgsDir):
    imgNames = os.listdir(imgsDir)
    # imgNames = sorted(imgNames, lambda x, y: name_sort(x, y))
    imgNames.sort(name_sort)
    frameRate = 25.0
    stdImgPath = os.path.join(imgsDir, 'capture00.jpg')
    stdImg = cv2.imread(stdImgPath)
    imgShape = list(stdImg.shape)
    imgSize = (imgShape[1], imgShape[0])
    video_writer = cv2.VideoWriter(regenVideoPath, cv2.VideoWriter_fourcc('D', 'I', 'V', 'X'), frameRate, imgSize)
    for imgName in imgNames:
        imgPath = os.path.join(imgsDir, imgName)
        img = cv2.imread(imgPath)
        video_writer.write(img)
    video_writer.release()


if __name__ == "__main__":
    projDir = os.path.dirname(os.getcwd())
    regenVideosDir = gen_regenVideos_dir(projDir)
    videosDir = os.path.join(projDir, 'videos')
    videoNames = os.listdir(videosDir)
    for videoName in videoNames:
        startTime = time.time()
        regenVideoPath = gen_video_path(regenVideosDir, videoName)
        imgsDir = os.path.join(videosDir, videoName)
        regen_video(regenVideoPath, imgsDir)
        duration = time.time() - startTime
        print 'duration:', duration

