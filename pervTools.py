import cv2
import base64
from random import randint
import fitbit
import datetime



def takePic():
    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # Check success
    if not video_capture.isOpened():
        raise Exception("Could not open video device")
    # Read picture. ret === True on success
    ret, frame = video_capture.read()
    path = str(randint(0,10000)) + ".jpg"
    cv2.imwrite(path, frame)
    # Close device
    video_capture.release()
    cv2.destroyAllWindows()
    return path

def getBPM():
    pass

#https://github.com/thegabriele97/AmiRunning-code/blob/2ef3732a30eb12c3ad12e35c9f13ae28bcab8559/src/RaspberryPi/fitbitPackage/fitbit_api.py#L31
def get_right_dateFormat(offset: int = 0) -> str:
    return str((datetime.datetime.now() - datetime.timedelta(days=offset)).strftime("%Y-%m-%d"))