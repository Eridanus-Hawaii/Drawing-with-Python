import cairo
import math
import sys
import scaled_font

class Drawing:
    def __init__(self, width, height):
        # print('初期化してるよ', width, height)
        self.width = width
        self.height = height

    def __str__(self):
        return f'Drawing Object {self.width} {self.height}'

if __name__ == '__main__':
    dobj = Drawing(640, 480)
    print(dobj)

    dobj1 = Drawing(87, 30)
    print(dobj1)