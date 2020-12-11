import numpy as np
import cv2
import time
import cvui

height = 640
width = 360

WINDOW_NAME = 'ARDOV'

cap = cv2.VideoCapture("PATH") #https://youtu.be/gFuuCwHrmbM i used this video for tests
#cap = cv2.VideoCapture(0) #webcam

params = cv2.SimpleBlobDetector_Params()
blobcolor = [255]
minthreshold=[232]
maxthreshold=[255]
mrepetability = [1]
minarea=[500]
maxarea=[50000]
minconvexity = [0.001]
maxconvexity = [10]
mininertia = [0.01]
maxinertia = [1]
mincircularity = [0.1]
maxcircularity = [1]
disbetween = [10]
xthreshold = [40]
giuheight = 300
giuwidth = 1800

params.blobColor = blobcolor[0]
params.minThreshold = minthreshold[0]
params.maxThreshold = maxthreshold[0]
params.minRepeatability = mrepetability[0]
params.minArea = minarea[0]
params.maxArea = maxarea[0]
params.minConvexity = minconvexity[0]
params.maxConvexity = maxconvexity[0]
params.minInertiaRatio = mininertia[0]
params.maxInertiaRatio = maxinertia[0]
params.minCircularity = mincircularity[0]
params.maxCircularity = maxcircularity[0]
params.minDistBetweenBlobs = disbetween[0]

ver = (cv2.__version__).split('.')
if(int(ver[0]) < 3):
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create(params)
frame = np.zeros((giuheight,giuwidth,3),np.uint8)

params.filterByArea = True
params.filterByCircularity = False
params.filterByConvexity =  True
params.filterByInertia = True

trackbarlength = 850

isdisbetween = [True]
if(isdisbetween == True):
    params.minDistBetweenBlobs = disbetween
isrepeatability = [True]
if(isrepeatability == True):
    params.minRepeatability = mrepetability
isblobcolor = [True]
if(isblobcolor == True):
    params.blobColor = 255

cvui.init(WINDOW_NAME)
while(True):
    
    frame[:] = (49,52,49)
    ###########################################################
    cvui.window(frame,10,giuheight-180,300,150,"Parametre1")
    cvui.checkbox(frame,12,giuheight-150,"MinDisBetweenBlob",isdisbetween)#if komutu eklemeyi unutma
    cvui.counter(frame,160,giuheight-150,disbetween,1,"%.0d")
    
    cvui.checkbox(frame,12,giuheight-120,"MinRepeatability",isrepeatability)#if komutu eklemeyi unutma
    cvui.counter(frame,160,giuheight-120,mrepetability,1,"%.0d")
    
    cvui.text(frame,32,giuheight-90,"MinThreshold")
    cvui.counter(frame,160,giuheight-90,minthreshold,1,"%.0d")
    params.minThreshold = minthreshold[0]
    cvui.text(frame,32,giuheight-60,"MaxThreshold")
    cvui.counter(frame,160,giuheight-60,maxthreshold,1,"%.0d")
    params.maxThreshold = maxthreshold[0]
    ######################################################
    cvui.window(frame,giuwidth-1400,giuheight-280,900,250,"Parametre2")

    #cvui.text(frame,giuheight-250,480,"MinArea")
    #cvui.trackbar(frame, 380, 470, trackbarlength, threshold, 0, 50000, 1, '%0d', cvui.TRACKBAR_DISCRETE, 500)
    
    cvui.text(frame,giuwidth-1390,giuheight-250,"MinArea")
    cvui.counter(frame,giuwidth-1300,giuheight-255,minarea,500,"%.0d")
    params.minArea = minarea[0]

    cvui.text(frame,giuwidth-1390,giuheight-220,"MaxArea")
    cvui.counter(frame,giuwidth-1300,giuheight-225,maxarea,500,"%d")
    params.maxArea = maxarea[0]

    cvui.text(frame,giuwidth-1100,giuheight-250,"MinCircularity")
    cvui.counter(frame,giuwidth-1010,giuheight-255,mincircularity,0.01,"%.02f")
    params.minCircularity = mincircularity[0]

    cvui.text(frame,giuwidth-1100,giuheight-220,"MaxCircularity")
    cvui.counter(frame,giuwidth-1010,giuheight-225,maxcircularity,0.1,"%d")
    params.maxCircularity = maxcircularity[0]

    cvui.text(frame,giuwidth-800,giuheight-250,"MinConvexity")
    cvui.counter(frame,giuwidth-710,giuheight-255,minconvexity,0.01,"%.03f")
    params.minConvexity = minconvexity[0]

    cvui.text(frame,giuwidth-800,giuheight-220,"MaxConvexity")
    cvui.counter(frame,giuwidth-710,giuheight-225,maxconvexity,1,"%d")
    params.maxConvexity = maxconvexity[0]

    cvui.text(frame,giuwidth-1390,giuheight-160,"MinInertiaRatio")
    cvui.counter(frame,giuwidth-1300,giuheight-165,mininertia,0.01,"%.02f")
    params.minInertiaRatio = mininertia[0]

    cvui.text(frame,giuwidth-1390,giuheight-130,"MaxInertiaRatio")
    cvui.counter(frame,giuwidth-1300,giuheight-135,maxinertia,1,"%d")
    params.maxInertiaRatio = maxinertia[0]

    cvui.text(frame,giuwidth-1100,giuheight-160,"BlobColor")
    cvui.checkbox(frame,giuwidth-1030,giuheight-162,"255",isblobcolor)
    
    options = cvui.TRACKBAR_DISCRETE | cvui.TRACKBAR_HIDE_SEGMENT_LABELS
    cvui.text(frame,giuwidth-1000,giuheight-80,"Threshold")
    #cvui.trackbar(frame, giuwidth-1390, giuheight-70, trackbarlength, xthreshold, 0, 255, 1)
    cvui.trackbar(frame, giuwidth-1390, giuheight-70, trackbarlength, xthreshold, 0, 255, 1, '%.0Lf', options, 2)
    threshold = xthreshold[0]
    cvui.update()
    cv2.imshow(WINDOW_NAME, frame)
    _, frame1 = cap.read()
    b = cv2.resize(frame1,(640,360),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
    frame1 = cv2.cvtColor(b,cv2.COLOR_BGR2GRAY)
    ret, Threshold = cv2.threshold(frame1,threshold,255,cv2.THRESH_BINARY)
    
# Detect blobs.
    keypoints = detector.detect(Threshold)
    cv2.circle(Threshold,(int(height/2),int(width/2)),5,(0,0,255))
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob
    for kp in keypoints:
        print("----")
        print(kp.pt[0]," ",kp.pt[1]," ",kp.size," ",kp.response)
        cv2.circle(Threshold, (int(kp.pt[0]), int(kp.pt[1])), int(kp.size), (0, 0, 255))
        #cv2.circle(Threshold, (int(kp.pt[0]), int(kp.pt[1])), 1, (0, 0, 255))
    #im_with_keypoints = cv2.drawKeypoints(Threshold, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    #print(len(keypoints))
    
    # Show blobs
    cv2.imshow("Frame1",frame1)
    cv2.imshow("Keypoints", Threshold)
    #cv2.imshow("Keypoints", im_with_keypoints)
    if cv2.waitKey(1) == 27:
	    break

    