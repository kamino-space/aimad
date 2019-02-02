import os
import re
import random
import glob
import threading
import queue
from .video import CtrlVideo
from .error import Error


class MakeVideo(object):
    source_path = "F:\\资源\\动漫\\物语系列 生肉\\"
    temp_path = "C:\\Users\\lishi\\Desktop\\code\\Python\\aimad\\aimad\\tmp\\"

    def __init__(self, fps=60, sec=0):
        """"""
        self.work_count = fps * sec
        print("INIT: Work -> %d" % self.work_count)
        self.scan_source()
        print("INIT: Source -> %d" % len(self.source_list))
        self.work_init()

    def scan_source(self):
        self.source_list = []
        for top, dirs, nondirs in os.walk(self.source_path):
            for item in nondirs:
                c = os.path.join(top, item)
                re.search('.mp4', c) and self.source_list.append(c)

    def eggs(self):
        return {
            1104: "kamino",
            1314: "MMloveU",
            205: "HAPPY BIRTHDAY CZY"
        }

    def work_init(self):
        self.work_queue = queue.Queue(self.work_count)
        print("INIT: Queue -> %d" % self.work_queue.qsize())
        # for i in range(0, int(self.work_count)):
        for i in range(5440, 5441):
            self.work_queue.put(i)
            """if i in self.eggs():
                self.work_queue.put(self.eggs()[i])
            else:
                self.work_queue.put(i)"""
        self.source_attr = []

        print("INFO: loading video attrs")
        for k, v in enumerate(self.source_list):
            print("\r(%d/%d)" % (k, len(self.source_list)), end="")
            vc = CtrlVideo(v)
            self.source_attr.append(vc.get_attr())
        print("\rFINISH")

    def work_single(self, tid=0):
        print("INFO: Thread %d Start" % tid)
        while True:
            key = random.randint(0, len(self.source_list) - 1)
            vc = CtrlVideo(self.source_list[key])
            va = self.source_attr[key]
            for i in range(random.randint(1, 10)):
                if self.work_queue.empty():
                    print("\nINFO: Thread %d Exit" % tid)
                    return None
                id = self.work_queue.get_nowait()
                print("\rWORKING: %d/%d" % (self.work_count - self.work_queue.qsize(), self.work_count), end="")
                try:
                    image = vc.get_image(random.randint(0, va['count']))
                    if va['width'] != 1920:
                        image = CtrlVideo.image_resize(image, (1920, 1080))
                    if id in self.eggs():
                        image = CtrlVideo.image_write(image, self.eggs()[id],
                                                      (50, 20))
                    else:
                        image = CtrlVideo.image_write(image, id, (50, 20))
                    CtrlVideo.image_save(image,
                                         "C:\\Users\\lishi\\Desktop\\code\\Python\\aimad\\aimad\\tmp\\%s.jpg" % id)
                except Error as e:
                    print("\nERROR: %s" % e)

    def work_multi(self):
        for i in range(5):
            threading.Thread(target=self.work_single, args=(i,)).start()
