import cairo
import math
import sys
import scaled_font

class Drawing:
    def __init__(self, name, color, width, height):
        print('初期化してるよ', width, height)
        self.name = name
        self.color = color
        self.width = width
        self.height = height

    def __str__(self):
        return f'Drawing Object {self.name} {self.color} {self.width} {self.height}'

    def draw_frame(self):
        print(f'Draw frames{self.color} {self.width} {self.height}')

    def draw_circle_num(self):
        print(f'Draw circle {self.width} {self.height}')

    def draw_my_string(self):
        print(f'Write word{self.width} {self.height}')

    def draw_label(self):
        self.draw_frame()
        self.draw_circle_num()
        self.draw_my_string ()

if __name__ == '__main__':
    dobj = Drawing('hana', 'Purple', 640, 480)
    print(dobj)
    dobj.draw_label()

    dobj1 = Drawing('anna', 'Blue', 87, 30)
    print(dobj1)
    dobj1.draw_label()