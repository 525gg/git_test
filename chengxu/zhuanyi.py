import shutil


def zhuanyi(s):
    path="D:/download_edge/yolov5-master/runs/train/exp"+s+"/weights/best.pt"
    print(path)
    shutil.copy(path,"D:/download_edge/yolov5-master/best.pt")


zhuanyi("54")