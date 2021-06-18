from transform import brighten, adjust_contrast, blur
from image import Image

class Controller:
    def __init__(self):
        pass

    def apply_brighten(self, image_name, p):
        image = Image(filename=image_name)
        apply_brightened = brighten(image, p)
        return apply_brightened

    def apply_adjust_contrast(self, image_name, factor, mid=0.5):
        image = Image(filename=image_name)
        apply_contrast = adjust_contrast(image, factor, mid)
        return apply_contrast

    def apply_blur(self, image_name, k_s):
        image = Image(filename=image_name)
        applied_blur = blur(image, k_s)
        return applied_blur


