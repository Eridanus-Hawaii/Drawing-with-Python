import cairo
import math
import sys
import scaled_font

class Label:
    def __init__(self, name):
        print('初期化してるよ')
        self.name = name
        self.color = 'blue'
        self.width = 400
        self.height = 100
    
    def init_surface(self):
        print('サーフェス作ったよ')

    def init_context(self):
        print('コンテキスト作ったよ')

    def save_image(self, filename):
        print('ファイルネームにセーブするよ', filename)

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

#----------------------------------------------------------------
if __name__ == '__main__':
    mochan = Label('Aloha Mochan')

    mochan.init_surface()
    mochan.init_context()

    mochan.draw_label()
    mochan.save_image('mochan2.png')