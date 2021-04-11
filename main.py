import handy.handy as handy
import cv2
import math
from gestureControl import *

# getting video feed from webcam
cap = cv2.VideoCapture(0)

# capture the hand histogram by placing your hand in the box shown and
# press 'A' to confirm
# source is set to inbuilt webcam by default. Pass source=1 to use an
# external camera.
hist = handy.capture_histogram(source=0)
lastAngle = None
sensitivity = 100

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (1920, 1080))

    # to block a faces in the video stream, set block=True.
    # if you just want to detect the faces, set block=False
    # if you do not want to do anything with faces, remove this line
    handy.detect_face(frame, block=True)

    # detect the hand
    hand = handy.detect_hand(frame, hist)

    # to get the outline of the hand
    # min area of the hand to be detected = 10000 by default
    custom_outline = hand.draw_outline(
        min_area=10000, color=(0, 255, 255), thickness=2)

    # to get a quick outline of the hand
    quick_outline = hand.outline

   # sum_of_fingertip_x = 0
   # sum_of_fingertip_y = 0

    # draw fingertips on the outline of the hand, with radius 5 and color red,
    # filled in.
    for fingertip in hand.fingertips:
        cv2.circle(quick_outline, fingertip, 5, (0, 0, 255), -1)

    # calculate and display angle of the hand based on the line of greatest distance (Hand.line)
    line_points = hand.line
    angle = 1.5708
    if len(line_points) >= 2:
        cv2.line(quick_outline, line_points[0], line_points[1], (255, 0, 0), 5)
        try:
            angle = math.atan(float(
                line_points[0][1] - line_points[1][1])/float(line_points[0][0] - line_points[1][0]))
            font = cv2.FONT_HERSHEY_SIMPLEX
        except:
            print("Angle is vertical")
        cv2.putText(quick_outline, str(angle),
                    (5, 50), font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

    # set previous angle if this is the first angle detected
    if lastAngle is None:
        lastAngle = angle

    # to get the centre of mass of the hand
    com = hand.get_center_of_mass()
    if com:
        cv2.circle(quick_outline, com, 10, (255, 0, 0), -1)

    cv2.imshow("Handy", quick_outline)

    # display the unprocessed, segmented hand
    # cv2.imshow("Handy", hand.masked)

    # display the binary version of the hand
    # cv2.imshow("Handy", hand.binary)

    k = cv2.waitKey(5)

    # Press 'q' to exit
    if k == ord('q'):
        break

    # Press 'k' to start panning
    if k == ord('k'):
        #drag_mouse(sensitivity * (angle - lastAngle))
        try:
            move_cursor(com[0], com[1])
        except TypeError:
            pass

    lastAngle = angle

cap.release()
cv2.destroyAllWindows()
