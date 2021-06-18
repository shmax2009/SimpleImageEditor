Height = int(720 / 1.5)
Width = int(1280 / 1.5)
DisplayHeight = 768
DisplayWidth = 1366
Image_position = (int(180 / 1.5), int(40 / 1.5))
Image_scale = (int(920 / 1.5), int(517 / 1.5))
coficient = (1, 1)


def update(vect2: (int, int)):
    a, b = vect2
    x, y = screen_cof
    return (a * x, b * y)
