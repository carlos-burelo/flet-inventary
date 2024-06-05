from flet import Image, ImageFit

def img(src: str, w: int, h: int):
    return Image(
        src=src,
        width=w,
        height=h,
        fit=ImageFit.CONTAIN,
    )