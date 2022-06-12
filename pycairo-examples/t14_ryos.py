import cairo
import math
import sys
import scaled_font

class Drawing: 
    def __init__(self, name, color, width, height):
        # print('初期化してるよ', width, height)
        self.name = name
        self.color = color
        self.width = width
        self.height = height

    def draw_frame(self):
        print(f'  フレームを {self.color} で書く {self.width} {self.height}')

    def draw_circle_num(self):
        print(f'  まるをかく {self.width} {self.height}')

    def draw_my_string(self):
        print(f'  文字を書く {self.width} {self.height}')

    def draw_label(self):
        self.draw_frame()
        self.draw_circle_num()
        self.draw_my_string ()

    def __str__(self):
        return f'Drawing Object {self.name} {self.color} {self.width} {self.height}'

#----------------------------------------------------------------
if __name__ == '__main__':
    dobj_hana = Drawing('hana', 'Blue', 640, 480)

    print(dobj_hana)
    dobj_hana.draw_label()

    dobj_anna = Drawing('anna', 'Red', 320, 240)
    print(dobj_anna)
    dobj_anna.draw_label()
