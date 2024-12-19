from __future__ import print_function
from imutils.video import FPS
from imutils.video import WebcamVideoStream
import argparse
import imutils
import cv2

AP = argparse . ArgumentParser()
AP.add_argument ( "-n" , "--num-frames" , type = int , default = 100 , help = "# of frames to loop over for FPS test" )
AP.add_argument ( "-d" , "--display" , type = int , default = -1 , help = "wheter or not frames should be desplayed" )
args = vars ( AP.parse_args() )

print ( "[INFO] sampling frames from webcam..." )
stream = cv2 . VideoCapture(0)

fps = FPS() . start()
while fps._numFrames < args["num_frames"]:
    ( grabbed , frame ) = stream . read()
    frame = imutils . resize ( frame , width = 400 )
    if args ["display"] > 0:
        cv2 . imshow ( "Frame" , frame )
        key = cv2 . waitKey(1)
    fps . update()
fps . stop()
print ("[INFO] elapsed time: {: .2f}" . format( fps.elapsed() ))
print ("[INFO] approx. FPS: {: .2f}" . format( fps . fps() ))
stream . release()
cv2 . destroyAllWindows()

print ("[INFO] sampling THREADED frames from webcam ... ")
vs = WebcamVideoStream ( src = 0 ).start()
fps = FPS() . start()
while fps._numFrames < args["num_frames"]:
    frame = vs . read()
    frame = imutils . resize(frame , width=400)
    if args["display"] > 0:
        cv2 . imshow ( "Frame" , frame )
        key = cv2 . waitKey(1)
    fps . update()
fps .stop()
print("[INFO] elapsed time: {: .2f}" . format( fps.elapsed() ))
print("[INFO] approx. FPS: {: .2f}" . format( fps.fps() ))
vs . stop()
cv2 . destroyAllWindows()

vs = WebcamVideoStream( src = 0 ).start()
frame = vs . read()
while True:
    frame = imutils . resize( frame , width = 400)
    cv2 . imshow ( "preview" , frame )
    frame = vs.read()
    key = cv2 . waitKey(20)
    if key == 27:
         break
vs . stop()
cv2 . destroyAllWindows()