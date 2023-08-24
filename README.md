# Brightness-Control-With-Hand-Detection-using-OpenCV

Uses OpenCV and Mediapipe to control hand gestures and accordingly set the brightness of the screen  from the range 0 to 100. HandTracking module was used to track all the points on the hand and detects the hand landmarks. Then calculate the distance between the thumb tip and index fingerand maps the distance between them.

Requirenments:  
- mediapipe==0.10.1  
- numpy==1.24.3  
- opencv_contrib_python==4.7.0.72  
- opencv_python==4.7.0.72  
- screen_brightness_control==0.21.0
