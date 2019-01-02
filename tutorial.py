from FaceDetection.detector import FaceDetector
import os

# Step 1) Make FaceDetector Object
detector = FaceDetector()

# Step 2) Set directory path to image file
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path+"/pic/iu.jpg"

# Step 3) Detect
# result --> (x,y, width, height)
result = detector.detect(dir_path)
print(result)