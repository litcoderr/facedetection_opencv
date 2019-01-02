# Face Detector
## Tutorial
#### Step 1 ) Make Face Detector Object
``detector = FaceDetector()``
#### Step 2 ) Set Directory path to image file
``dir_path = os.path.dirname(os.path.realpath(__file__))``<br>
``dir_path = dir_path+"/pic/iu.jpg"``
#### Step 3 ) Detect
``result = detector.detect(dir_path)``
<br>
result has 4 dimensions --> (x, y, width, height) <br>
Use . It. Well ~