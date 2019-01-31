import cv2
import os
import random
import re
import time
import threading

root_path = os.path.dirname(__file__) + '/'


def readvideo(path=''):
    if not os.path.exists(path):
        return None
    vc = cv2.VideoCapture(path)
    data = {}
    data['fps'] = vc.get(cv2.CAP_PROP_FPS)
    data['width'] = vc.get(cv2.CAP_PROP_FRAME_WIDTH)
    data['height'] = vc.get(cv2.CAP_PROP_FRAME_HEIGHT)
    data['count'] = vc.get(cv2.CAP_PROP_FRAME_COUNT)
    vc.release()
    return data


def getimg(path, num=0):
    vc = cv2.VideoCapture(path)
    vc.set(cv2.CAP_PROP_POS_FRAMES, num)
    a, b = vc.read()
    return b


def randnum(max=0):
    return random.randint(0, max)


def scansrc(path):
    fileList = []
    for top, dirs, nondirs in os.walk(path):
        for item in nondirs:
            c = os.path.join(top, item)
            re.search('.mp4', c) and fileList.append(c)
    return fileList


def single(r1=0, r2=0, tid=0):
    for i in range(r1, r2 + 1):
        print('ID->{0} TID->{1} TIME->{2} '.format(i, tid, int(time.time() - start)), end='')
        vid = random.randint(0, len(video) - 1)
        pid = randnum(video[vid][1])
        print('VID->{0} PID->{1}'.format(vid, pid))
        img = getimg(video[vid][0], pid)
        cv2.imwrite('C:/Users/lishi/Desktop/code/Python/aimad/tmp/' + str(i).zfill(5) + '.jpg', img)


if __name__ == '__main__':
    sec = 255
    start = time.time()
    path_list = scansrc('F:/资源/动漫/物语系列 生肉')
    video = []
    print('INIT...')
    for v in path_list:
        video.append([v, readvideo(v)['count']])
    print('OK', video)
    all = sec * 60
    ths = 5
    for i in range(ths):
        threading.Thread(target=single, args=(int(i * all / ths + 1), int((i + 1) * all / ths), i,)).start()
