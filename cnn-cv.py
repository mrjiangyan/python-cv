import cv2
import dlib


font = cv2.FONT_HERSHEY_SIMPLEX


# 设置初始窗口大小
cv2.namedWindow("Source", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Target", cv2.WINDOW_AUTOSIZE)

#  产品办公区域 rtsp://admin:a12345678@192.168.122.41:554/Streaming/Channels/101
#  前台 rtsp://admin:a12345678@192.168.122.42:554/Streaming/Channels/101


cap = cv2.VideoCapture('rtsp://admin:a12345678@192.168.122.41:554/Streaming/Channels/101')
dnnFaceDetector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")

while (True):
    ret, frame = cap.read()
    cv2.imshow('Source', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    rects = dnnFaceDetector(gray, 1)
    for (i, rect) in enumerate(rects):
        x1 = rect.rect.left()
        y1 = rect.rect.top()
        x2 = rect.rect.right()
        y2 = rect.rect.bottom()
        
        print(x1)
        # Rectangle around the face
        cv2.rectangle(gray, (x1, y1), (x2, y2), (255, 255, 255), 3)

    # Display the video output
    cv2.imshow('Target', frame)
    
     # Quit video by typing Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
