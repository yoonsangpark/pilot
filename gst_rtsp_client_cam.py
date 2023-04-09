import cv2
import time

# vid = cv2.VideoCapture(0) # For webcam
vid = cv2.VideoCapture("rtsp://192.168.10.104:8554/test") # For streaming links

while True:
    rdy,frame = vid.read()
    print(rdy)
    try:
        cv2.imshow('Video Live IP cam',frame)
        key = cv2.waitKey(1) & 0xFF
        if key ==ord('q'):
            break
    except:
        pass

    time.sleep(0.5)
    print(">> ooSSoo")

vid.release()
cv2.destroyAllWindows()
