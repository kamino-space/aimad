from aimad import MakeVideo, CtrlVideo

CtrlVideo.image_to_video("C:\\Users\\lishi\\Desktop\\code\\Python\\aimad\\aimad\\tmp\\",
                         "C:\\Users\\lishi\\Desktop\\code\\Python\\aimad\\aimad\\output\\output.mp4")

"""
try:
    mk = MakeVideo(60, 300)
    mk.work_multi()
except Exception as e:
    print(e)
"""
"""
try:
    c = CtrlVideo("C:\\Users\\lishi\\Desktop\\code\\Python\\aimad\\old\\output.mp4")
    attr = c.get_attr()
    print(attr)
    image = c.get_image(300)
    image = CtrlVideo.image_write(image,1234,(20,50))
    CtrlVideo.image_show(image)
    #CtrlVideo.save_image(image,"C:\\Users\\lishi\\Desktop\\code\\Python\\aimad\\aimad\\temp\\test.jpg")
except Error as e:
    print(e)
"""
