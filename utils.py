import os

class Utils:
    def __init__(self):
        ...

    @staticmethod
    def check_file(file: str):
        expansions = ("png", "jpg", "jpeg")
        print(file)
        return file != None and file.split(".")[-1] in expansions
