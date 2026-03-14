import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # RED (2 ranges)
    lower_red1 = np.array([0,120,70])
    upper_red1 = np.array([10,255,255])

    lower_red2 = np.array([170,120,70])
    upper_red2 = np.array([180,255,255])

    # GREEN
    lower_green = np.array([40,50,50])
    upper_green = np.array([90,255,255])

    # YELLOW
    lower_yellow = np.array([15,100,100])
    upper_yellow = np.array([35,255,255])

    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    red_mask = mask_red1 + mask_red2

    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    red_pixels = cv2.countNonZero(red_mask)
    green_pixels = cv2.countNonZero(green_mask)
    yellow_pixels = cv2.countNonZero(yellow_mask)

    if red_pixels > 8000:
        text = "Obstacle - STOP"
        color = (0,0,255)
    elif yellow_pixels > 8000:
        text = "Slow Down"
        color = (0,255,255)
    elif green_pixels > 8000:
        text = "Move Forward"
        color = (0,255,0)
    else:
        text = "Searching Path"
        color = (255,255,255)

    cv2.putText(frame, text, (50,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

    cv2.imshow("Robot Vision", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()