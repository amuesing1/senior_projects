from picamera import PiCamera
from time import sleep

camera = PiCamera()

sleep(2)
camera.capture('image.jpg')
# camera.start_recording('video.h264')
# camera.wait_recording(25)
# camera.stop_recording
