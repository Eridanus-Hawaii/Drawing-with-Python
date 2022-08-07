import cairo
import math
import sys
import scaled_font

class Label: 
    def __init__(self, name):
        self.name = name

        self.color = 'Blue'

        self.width = None
        self.height = None

        self.surface = None
        self.context = None

    def init_surface(self):
        self.width = 400
        self.height = 100

        self.surface = cairo.ImageSurface(cairo.FORMAT_RGB24, self.width, self.height)
        print('init_surface しました', self.surface)
        
    def init_context(self):
        self.context = cairo.Context(self.surface)
        print('init_context しました')

    def save_image(self, filename):
        print(f'{filename} にセーブします')

    def draw_frame(self):
        print(f'  フレームを {self.color} で書く {self.width} {self.height}')

    def draw_circle_num(self):
        print(f'  まるをかく {self.width} {self.height}')

    def draw_my_string(self):
        print(f'  文字を書く {self.width} {self.height}')

    def draw_label(self):
        print(f'ラベルを作ります')

        self.draw_frame()
        self.draw_circle_num()
        self.draw_my_string ()

    def __str__(self):
        return f'Drawing Object {self.name} {self.color} {self.width} {self.height}'

#----------------------------------------------------------------
if __name__ == '__main__':
    mochan = Label('Aloha Mochan')

    mochan.init_surface()
    mochan.init_context()

    mochan.draw_label()
    mochan.save_image('mochan.png')
