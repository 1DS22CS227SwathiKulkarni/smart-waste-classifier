import os #operating system
import cvzone
#1.5.6 version
from cvzone.ClassificationModule import Classifier
import cv2
#import the video capture device
cap = cv2.VideoCapture(0)
classifier = Classifier('Resources/Model/keras_model.h5', 'Resources/Model/labels.txt')
imgArrow = cv2.imread('Resources/arrow.png',cv2.IMREAD_UNCHANGED)
classIDBin = 0

#Import all waste
imgWasteList = []
pathFolderWaste = "Resources/Waste"
pathList = os.listdir(pathFolderWaste)
#only names of images are stored
print(pathList)
for path in pathList:
    imgWasteList.append(cv2.imread(os.path.join(pathFolderWaste, path), cv2.IMREAD_UNCHANGED))
    #join paths of the image and the location of the image

#Import all bins
imgBinsList = []
pathFolderBins = "Resources/Bins"
pathList = os.listdir(pathFolderBins)
print(pathList)
for path in pathList:
    imgBinsList.append(cv2.imread(os.path.join(pathFolderBins, path), cv2.IMREAD_UNCHANGED))

classDic = {0:None,
            1:0, #ziptopcans:recyclable
            2:0, #newspaper:recyclable
            3:3, #oldshoes:residual
            4:3, #watercolorpen:residual
            5:1, #Disinfectant:hazardous
            6:1, #Battery:hazardous
            7:2, #vegetableleaf:food
            8:2} #apple:food

while True:
    _,img = cap.read()
    #read from the frame
    imgResize= cv2.resize(img,(454,340))
    #640/480 to 454/340
    imgBackground = cv2.imread('Resources/background.png')
    #to clear the previous image

    predection = classifier.getPrediction(img)

    classID = predection[1]
    print(classID)
    if classID!=0:
        imgBackground = cvzone.overlayPNG(imgBackground, imgWasteList[classID-1],(909,127))
        imgBackground = cvzone.overlayPNG(imgBackground, imgArrow, (978, 320))
        classIDBin = classDic[classID]

    imgBackground = cvzone.overlayPNG(imgBackground, imgBinsList[classIDBin], (895, 374))

    imgBackground[148:148+340,159:159+454] = imgResize
    #img[height, width]
    #Display
    #cv2.imshow("Image", img)
    cv2.imshow("Output", imgBackground)
    cv2.waitKey(1)
    #wait for 1 millisecond