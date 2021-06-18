from PIL import Image, ImageFilter
from PIL import ImageEnhance


class Controller:
    def __init__(self):
        ...

    def apply_brighten(self, path: str, factor: float):
        im = Image.open(path)
        enh = ImageEnhance.Brightness(im)
        enh.enhance(factor / 100).save("brightness." + path.split(".")[-1])

    def apply_color(self, path: str, factor: float):
        im = Image.open(path)
        enh = ImageEnhance.Color(im)
        enh.enhance(factor / 100).save("color." + path.split(".")[-1])

    def apply_sharpness(self, path: str, factor: float):
        im = Image.open(path)
        enh = ImageEnhance.Sharpness(im)
        enh.enhance(factor / 100).save("sharp." + path.split(".")[-1])
