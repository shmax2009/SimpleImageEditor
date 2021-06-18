Height = 720
Width = 1280
Image_position = (180, 40)
Image_scale = (920, 517)
screen_cof = 0


def update(vect2: (int, int)):
    a, b = vect2
    x, y = screen_cof
    return (a * x, b * y)
