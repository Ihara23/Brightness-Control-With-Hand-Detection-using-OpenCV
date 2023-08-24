import cv2
import mediapipe as mp
from math import hypot
import screen_brightness_control as sbc
import numpy as np

# Initializing the Model
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, model_complexity=1, min_detection_confidence=0.75, min_tracking_confidence=0.75, max_num_hands=2)

Draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:    
	_, frame = cap.read()	# Read video frame by frame
	
	frame = cv2.flip(frame, 1)# Flip image

	frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# Process the RGB image
	Process = hands.process(frameRGB)

	landmarkList = []
	if Process.multi_hand_landmarks:
		for handlm in Process.multi_hand_landmarks:
			for _id, landmarks in enumerate(handlm.landmark):
				height, width, color_channels = frame.shape

				x, y = int(landmarks.x*width), int(landmarks.y*height)
				landmarkList.append([_id, x, y])

			# draw Landmarks
			Draw.draw_landmarks(frame, handlm, mpHands.HAND_CONNECTIONS)

	if landmarkList != []:
		x_1, y_1 = landmarkList[4][1], landmarkList[4][2]

		x_2, y_2 = landmarkList[8][1], landmarkList[8][2]

		# draw circle on thumb and index finger tip
		cv2.circle(frame, (x_1, y_1), 7, (0, 255, 0), cv2.FILLED)
		cv2.circle(frame, (x_2, y_2), 7, (0, 255, 0), cv2.FILLED)

		cv2.line(frame, (x_1, y_1), (x_2, y_2), (0, 255, 0), 3)# draw line from tip of thumb to tip of index finger
	
		L = hypot(x_2-x_1, y_2-y_1)# calculate the distance between two finger tips
		b_level = np.interp(L, [15, 220], [0, 100])

		# set brightness
		sbc.set_brightness(int(b_level))

	cv2.imshow('Image', frame)
	if (cv2.waitKey(1) & 0xff == ord('q')):   

		break
cap.release()
cv2.destroyAllWindows()
    


