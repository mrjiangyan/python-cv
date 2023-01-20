import cv2
import matplotlib.pyplot as plt
import dlib
from imutils import face_utils

basePath = '/System/Volumes/Data/Users/jiangyan/Library/Python/3.9/lib/python/site-packages/cv2/data/'
cascPath = basePath + 'haarcascade_frontalface_default.xml'
eyePath = basePath + "haarcascade_eye.xml"
smilePath = basePath + "haarcascade_smile.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
eyeCascade = cv2.CascadeClassifier(eyePath)
smileCascade = cv2.CascadeClassifier(smilePath)

font = cv2.FONT_HERSHEY_SIMPLEX


# 设置初始窗口大小
cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Video", 800, 600)

#  产品办公区域 rtsp://admin:a12345678@192.168.122.41:554/Streaming/Channels/101
#  前台 rtsp://admin:a12345678@192.168.122.42:554/Streaming/Channels/101


cap = cv2.VideoCapture('rtsp://admin:a12345678@192.168.122.41:554/Streaming/Channels/101')
waitTime=50
while (True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    face_detect = dlib.get_frontal_face_detector()
    rects = face_detect(gray, 1)
    for (i, rect) in enumerate(rects):
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 255, 255), 3)
    
        # Display the resulting frame
        cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
