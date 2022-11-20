def __ajustYiq2Rgb(pixel):
    if pixel < 0: pixel = 0
    elif pixel > 255: pixel = 255
    return pixel

