import cv2
import glob

videoWriter = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 60, (1280, 720))
imgs = glob.glob('C:/Users/lishi/Desktop/code/Python/aimad/tmp/*.jpg')
for imgname in imgs:
    frame = cv2.imread(imgname)
    videoWriter.write(frame)
videoWriter.release()
