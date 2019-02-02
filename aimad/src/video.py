import os
import cv2
import time
import numpy
import glob
from PIL import Image, ImageFont, ImageDraw
from .error import Error


class CtrlVideo(object):

    def __init__(self, path):
        """初始化"""
        if os.path.exists(path):
            self.vc = cv2.VideoCapture(path)
            self._get_attr()
        else:
            raise Error("File Not Exist %s" % path)

    def __del__(self):
        self.vc.release()

    def _get_attr(self):
        try:
            self.attr = {
                'fps': self.vc.get(cv2.CAP_PROP_FPS),
                'width': self.vc.get(cv2.CAP_PROP_FRAME_WIDTH),
                'height': self.vc.get(cv2.CAP_PROP_FRAME_HEIGHT),
                'count': self.vc.get(cv2.CAP_PROP_FRAME_COUNT)
            }
            if self.attr['count'] == 0.0:
                raise Error('Not A Video')
        except Exception as e:
            raise Error(e)

    def get_attr(self):
        """获取视频属性"""
        return self.attr

    def get_image(self, num=0):
        """根据帧数获取图片"""
        try:
            self.vc.set(cv2.CAP_PROP_POS_FRAMES, num)
            a, b = self.vc.read()
            return b
        except Exception as e:
            raise Error(e)

    @staticmethod
    def image_show(image):
        title = str(int(time.time()))
        try:
            cv2.imshow(title, image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except Exception as e:
            raise Error(e)

    @staticmethod
    def image_save(image, path):
        try:
            cv2.imwrite(path, image)
        except Exception as e:
            raise Error(e)

    @staticmethod
    def image_write(image, text, location=(0, 0), font=os.path.abspath(".") + "/aimad/save/font.otf"):
        try:
            image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype(font, size=40)
            draw.text(location, str(text), font=font, fill=(255, 255, 255))
            return cv2.cvtColor(numpy.asarray(image), cv2.COLOR_RGB2BGR)
        except Exception as e:
            raise Error(e)

    @staticmethod
    def image_resize(image, size=(1920, 1080)):
        try:
            return cv2.resize(image, size)
        except Exception as e:
            raise Error(e)

    @staticmethod
    def image_to_video(image_path, output_path):
        print("IMAGES TO VIDEO")
        videoWriter = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), 60, (1920, 1080))
        for i in range(0, 18000):
            try:
                p = "%s%s.jpg" % (image_path, i)
                frame = cv2.imread(p)
                videoWriter.write(frame)
            except Exception as e:
                print(e)
            print("\r%d/%d" % (i + 1, 18000), end="")
        videoWriter.release()
        print("\nFINISH %s" % output_path)
