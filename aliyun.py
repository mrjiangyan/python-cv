import cv2
from alibabacloud_imagesearch20200212.client import Client
from alibabacloud_imagesearch20200212.models import SearchImageByPicAdvanceRequest
from alibabacloud_oss_util.models import RuntimeOptions
from alibabacloud_tea_rpc.models import Config
from PIL import Image
import numpy as np
import io

basePath = '/System/Volumes/Data/Users/jiangyan/Library/Python/3.9/lib/python/site-packages/cv2/data/'
cascPath = basePath + 'haarcascade_frontalface_alt.xml'
eyePath = basePath + "haarcascade_eye.xml"
smilePath = basePath + "haarcascade_smile.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

'''ECS Example'''
# init Config
config = Config(
    access_key_id='LTAI5tKccvWLPmDmxuqonZXV',
    access_key_secret='BhbUhbGvOubU3CEQQuPmhjxBOC7NKj',
    # 访问的域名
    endpoint='facebody.cn-shanghai.aliyuncs.com',
    # 访问的域名对应的region
    region_id='cn-shanghai',
    type='access_key'
)

# init RuntimeObject
runtime_option = RuntimeOptions()

# init Client
client = Client(config)

    
font = cv2.FONT_HERSHEY_SIMPLEX


# 设置初始窗口大小
# cv2.namedWindow("Source", cv2.WINDOW_AUTOSIZE)x

cv2.namedWindow("Target", cv2.WINDOW_AUTOSIZE)

#  产品办公区域 rtsp://admin:a12345678@192.168.122.41:554/Streaming/Channels/101
#  前台 rtsp://admin:a12345678@192.168.122.42:554/Streaming/Channels/101


cap = cv2.VideoCapture('rtsp://admin:a12345678@192.168.122.41:554/Streaming/Channels/101')
# cap = cv2.VideoCapture(0)
waitTime=50
while (True):
    ret, frame = cap.read()
    # cv2.imshow('Source', frame)

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

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
        crop = frame[y:y+h, x:x+w]
        cv2.imshow("crop", crop)
        # init Request
        request = SearchImageByPicAdvanceRequest(
                instance_name='name',
                pic_content_object= io.BytesIO(crop.tobytes())  # File stream or BytesIO
        )
        # call api
        response = client.search_image_by_pic_advance(request, runtime_option)
        print(response)
        print('request id:', response.request_id)
        print('code:', response.code)
        print('message:', response.msg)

        # head
        print('docs return:', response.head.docs_return)
        print('docs found:', response.head.docs_found)
        print('search time:', response.head.search_time)

        # pic info
        print('category id:', response.pic_info.category_id)
        print('region:', response.pic_info.region)
        print('all categories:', response.pic_info.all_categories)

        # Auctions
        for aut in response.auctions:
                print('category id:', aut.category_id)
                print('product id:', aut.product_id)
        
     
    # Draw a rectangle around the faces
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

   
    
    
   
    cv2.putText(frame,'Number of Faces : ' + str(len(faces)),(40, 40), font, 1,(255,0,0),3)     
    # Display the resulting frame
    cv2.imshow('Target', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cap.release()
# cv2.destroyAllWindows()
