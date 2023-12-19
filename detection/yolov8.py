from ultralytics import YOLO
from PIL import Image
import os

WEIGHTS_PATH = "weights/pipe_s.pt"

class YOLOCount:
    def __init__(self):
        self.model = YOLO(WEIGHTS_PATH)
        self.confidence = 0.4

    def __call__(self, img_path):
        res = self.model.predict(img_path, conf=self.confidence)
        obj_count = len(res[0].boxes)
        img_detection = res[0].plot(labels=False, conf=False)[:, :, ::-1]
        img_detection = Image.fromarray(img_detection)
        filename, file_extension = os.path.splitext(img_path)
        img_detection_path = filename + '_d' + file_extension
        img_detection.save(img_detection_path)
        return obj_count, img_detection_path
