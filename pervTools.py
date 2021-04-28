import cv2
import base64
from random import randint
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