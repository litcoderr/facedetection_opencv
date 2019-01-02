import cv2
import os

class FaceDetector():
    def __init__(self):
        xml_path = os.path.dirname(os.path.realpath(__file__))
        xml_path = xml_path+"/haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(xml_path)

    def detect(self,image_dir):
        image = cv2.imread(image_dir,cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

        return faces