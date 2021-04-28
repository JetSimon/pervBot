import cv2
from random import randint
import datetime

def takePic(text = None):
    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # Check success
    if not video_capture.isOpened():
        raise Exception("Could not open video device")
    # Read picture. ret === True on success
    ret, frame = video_capture.read()
    
    #Text adding stuff
    if text:
        h,w,c = frame.shape
        font = cv2.FONT_HERSHEY_TRIPLEX
        processedText = text.split("%n")

        lh = 25
        
        for line in processedText:
            cv2.putText(frame,line,(10,lh), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
            lh+=25

    # Save file to computer w random name
    path = str(randint(0,10000)) + ".jpg"
    cv2.imwrite(path, frame)

    # Close device
    video_capture.release()
    cv2.destroyAllWindows()
    return path #return path for discord to load from

def makeMeme(top, bottom):
    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # Check success
    if not video_capture.isOpened():
        raise Exception("Could not open video device")
    # Read picture. ret === True on success
    ret, frame = video_capture.read()

    h,w,c = frame.shape
    font = cv2.FONT_HERSHEY_TRIPLEX

    cv2.putText(frame,top,(int(w/4),25), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(frame,bottom,(int(w/4),h-25), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

    # Save file to computer w random name
    path = str(randint(0,10000)) + ".jpg"
    cv2.imwrite(path, frame)

    # Close device
    video_capture.release()
    cv2.destroyAllWindows()
    return path #return path for discord to load from

#https://github.com/thegabriele97/AmiRunning-code/blob/2ef3732a30eb12c3ad12e35c9f13ae28bcab8559/src/RaspberryPi/fitbitPackage/fitbit_api.py#L31
def get_right_dateFormat(offset: int = 0) -> str:
    return str((datetime.datetime.now() - datetime.timedelta(days=offset)).strftime("%Y-%m-%d"))