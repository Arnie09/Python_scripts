import cv2,time

video = cv2.VideoCapture(0)

a =1
first_frame  = None

while True:
    a = a+1
    check,frame = video.read()
    print(frame)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)
    
    if(first_frame is None):
        first_frame = gray
        continue
    
    deltaframe = cv2.absdiff(first_frame,gray)

    edge = cv2.Canny(frame,100,200)

    thresh_data = cv2.threshold(deltaframe,30,255,cv2.THRESH_BINARY)[1]
    thresh_data = cv2.dilate(thresh_data,None,iterations = 0)

    (cnts,_) = cv2.findContours(thresh_data.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    # for contours in cnts:
    #     if cv2.contouframe:
    #         continue
    #     x,y,h,w = cv2.boundingRect(contours)
    #     cv2.rectangle(frame,(x,y),(x+h,y+w),(255,0,0),3)

    cv2.imshow('RealtimeFrame:',frame)
    cv2.imshow('Capturing',gray)
    #cv2.imshow('deltaframe',deltaframe)
    cv2.imshow('thresh',thresh_data)
    cv2.imshow("edge",edge)

    key = cv2.waitKey(1)

    if(key  == ord('q')):
        break

print(a)
video.release()
cv2.destroyAllWindows()
