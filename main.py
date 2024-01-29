import cv2
from cvzone.FaceDetectionModule import FaceDetector
import serial
import time

cap = cv2.VideoCapture(0)
detector = FaceDetector()

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    # time.sleep(.05)
    # data = arduino.readline()
    # return data

while True:
    success, img = cap.read()
    img, bBoxes = detector.findFaces(img)
    height, width, _ = img.shape
    if len(bBoxes) > 0:
        face_center = bBoxes[0]['center']
        [face_x, face_y] = face_center
        string = 'X' + str(round(face_x/width * 100)/100)
        (write_read(string))
        string = 'Y' + str(round(face_y/height*100)/100)
        (write_read(string))

    # cv2.imshow("Video", img)

    # cv2.waitKey(1)