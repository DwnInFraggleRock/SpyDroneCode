from djitellopy import Tello
import cv2
import time

tello = Tello()


tello.connect()
print(tello.get_battery())

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()
time.sleep(1)
tello.move_up(100)

cv2.imwrite("picture1.png", frame_read.frame)
time.sleep(1)

tello.move_left(100)
time.sleep(1)

cv2.imwrite("picture2.png", frame_read.frame)
time.sleep(1)

tello.move_right(200)
time.sleep(1)

cv2.imwrite("picture3.png", frame_read.frame)
time.sleep(1)

tello.move_up(100)
time.sleep(1)

cv2.imwrite("picture.png", frame_read.frame)
time.sleep(1)

tello.move_down(200)
tello.land()
