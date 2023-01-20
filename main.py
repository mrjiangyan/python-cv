import cv2
import sys

basePath = '/System/Volumes/Data/Users/jiangyan/Library/Python/3.9/lib/python/site-packages/cv2/data/'
cascPath = basePath + 'haarcascade_frontalface_alt.xml'
eyePath = basePath + "haarcascade_eye.xml"
smilePath = basePath + "haarcascade_smile.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
eyeCascade = cv2.CascadeClassifier(eyePath)
smileCascade = cv2.CascadeClassifier(smilePath)

font = cv2.FONT_HERSHEY_SIMPLEX


# 设置初始窗口大小
# cv2.namedWindow("Source", cv2.WINDOW_AUTOSIZE)

cv2.namedWindow("Target", cv2.WINDOW_AUTOSIZE)

#  产品办公区域 rtsp://admin:a12345678@192.168.122.41:554/Streaming/Channels/101
#  前台 rtsp://admin:a12345678@192.168.122.42:554/Streaming/Channels/101


# cap = cv2.VideoCapture('rtsp://admin:a12345678@192.168.122.41:554/Streaming/Channels/101')
cap = cv2.VideoCapture(0)
waitTime=50
while (True):
    ret, frame = cap.read()
    # cv2.imshow('Source', frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )


    for (x, y, w, h) in faces:
        print(x, y, w, h)
        # if w > 250 :
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        smile = smileCascade.detectMultiScale(
                roi_gray,
                scaleFactor= 1.16,
                minNeighbors=35,
                minSize=(25, 25),
                flags=cv2.CASCADE_SCALE_IMAGE
        )
        print(str(len(smile)))
        for (sx, sy, sw, sh) in smile:
                cv2.rectangle(roi_color, (sh, sy), (sx+sw, sy+sh), (255, 255, 0), 2)
                cv2.putText(frame,'Smile',(x + sx,y + sy), 1, 1, (0, 255, 0), 1)
                
        eyes = eyeCascade.detectMultiScale(roi_gray)
        print(str(len(eyes)))
        for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                cv2.putText(frame,'Eye',(x + ex,y + ey), 1, 1, (0, 255, 0), 1)   
     
    # Draw a rectangle around the faces
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

   
    
    
   
    cv2.putText(frame,'Number of Faces : ' + str(len(faces)),(40, 40), font, 1,(255,0,0),3)     
    # Display the resulting frame
    cv2.imshow('Target', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
