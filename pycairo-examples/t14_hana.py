import cairo
import math
import sys
import scaled_font
import matplotlib.colors as mcolors

class Label:
    def __init__(self, name):
        print('初期化してるよ')
        self.name = name
        self.color = 'blue'
        self.line_width = 20
        self.width = 400
        self.height = 100

        self.surface = None
        self.context = None
    
    def init_surface(self):
        print('Creating initial surface')
        self.width = 400
        self.height = 100
        self.surface = cairo.ImageSurface(cairo.FORMAT_RGB24, self.width, self.height)

    def init_context(self):
        print('Setting up context')
        self.context = cairo.Context(self.surface)
        print('creating context')

    def save_image(self, filename):
        print(f'{filename} にセーブします')
        self.surface.write_to_png(filename)

    def __str__(self):
        return f'Drawing Object {self.name} {self.color} {self.width} {self.height}'

    def set_source_color(self, name):
        for colors in [mcolors.BASE_COLORS, mcolors.TABLEAU_COLORS, mcolors.CSS4_COLORS]:
            for color_name, color in colors.items():
                if name == color_name:
                    #print('icchi', color)
                    # #2E8B57
                    if type(color) == tuple:
                        new_color = color
                    else:
                        new_color = (int(color[1:3], 16)/255, int(color[3:5], 16)/255, int(color[5:7], 16)/255)
                    self.context.set_source_rgb(new_color[0], new_color[1], new_color[2])
                    break

    def draw_frame(self):
        self.set_source_color(self.color)
        self.context.set_line_width(self.line_width)

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
    mochan.save_image('MOCHAN.png')