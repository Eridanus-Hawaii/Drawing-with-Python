import cairo
import math
import sys
import scaled_font

import matplotlib.colors as mcolors

def set_source_color(context, name):
    for colors in [mcolors.BASE_COLORS, mcolors.TABLEAU_COLORS, mcolors.CSS4_COLORS]:
        for color_name, color in colors.items():
            if name == color_name:
                #print('icchi', color)
                # #2E8B57
                if type(color) == tuple:
                    new_color = color
                else:
                    new_color = (int(color[1:3], 16)/255, int(color[3:5], 16)/255, int(color[5:7], 16)/255)
                context.set_source_rgb(new_color[0], new_color[1], new_color[2])
                break

class Label: 
    def __init__(self, my_num, name):
        self.my_num = my_num
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
        self.surface.write_to_png(filename)

    #----------------------------------------------------------------
    def draw_frame(self, x, y, w, h, r):
        print(f'  フレームを {self.color} で書く {self.width} {self.height}')
        line_width = 20
        self.context.set_line_width(line_width)

        self.context.move_to(x+r, y)
        self.context.line_to(x+w-r-1, y)
        self.context.arc(x+w-r-1, y+r, r, -0.5*math.pi, 0)
        self.context.line_to(x+w-1, y+h-r-1)
        self.context.arc(x+w-r-1, y+h-r-1, r, 0, 0.5*math.pi)
        self.context.line_to(x+r, y+h-1)
        self.context.arc(x+r, y+h-r-1, r, 0.5*math.pi, math.pi)
        self.context.line_to(x, y+r)
        self.context.arc(x+r, y+r, r, math.pi, 1.5*math.pi)
        self.context.close_path()

        #self.context.set_source_rgb(0xff/float(0xff), 0xff/float(0xff), 0xff/float(0xff))
        set_source_color(self.context, 'tomato')
        self.context.fill_preserve()

        #self.context.set_source_rgb(0xff/float(0xff), 0x99/float(0xff), 0x00/float(0xff))
        #set_source_color(self.context, 'seagreen')
        set_source_color(self.context, 'blueviolet')
        #set_source_color(self.context, 'c')
        self.context.stroke()

    def draw_circle_num(self, x, y, r, color):
        print(f'  まるをかく {self.width} {self.height}')
        #self.context.set_source_rgb(0, 0, 0)
        self.context.set_source_rgb(color[0], color[1], color[2])

        line_width = 3
        self.context.set_line_width(line_width)
        self.context.arc(x, y, r, 0, math.pi * 2)
        self.context.stroke()

        font_size = 30
        sf = scaled_font.get_scaled_font('Arial', font_size )
        extents = sf.text_extents(self.my_num)
        self.context.set_font_size(font_size)
        self.context.move_to(x, y)
        self.context.rel_move_to(-extents.width/2, -extents.height/2)
        self.context.rel_move_to(-extents.x_bearing, -extents.y_bearing)
        self.context.show_text(self.my_num)
        self.context.stroke()

    def draw_my_string(self, x, y, color):
        print(f'  文字を書く {self.width} {self.height}')
        self.context.select_font_face('Ricty Diminished', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

        font_size = 30
        #self.context.set_source_rgb(0, 0, 0)
        self.context.set_source_rgb(color[0], color[1], color[2])

        self.context.set_font_size(font_size)
        self.context.move_to(x, y)
        self.context.show_text(self.name)
        self.context.stroke()

    def draw_label(self):
        print(f'ラベルを作ります')
        line_width = 20

        w = self.width - line_width/2 - line_width/2
        h = self.height - line_width/2 - line_width/2 
        r = 20

        x = line_width/2
        y = line_width/2

        self.draw_frame(x, y, w, h, r)

        #----------------------------------------------------------------
        x2 = x + line_width/2 + r + 5
        y2 = y + h/2

        self.draw_circle_num(x2, y2, r, (0, 0, 0))

        #----------------------------------------------------------------
        font_h = 10
        x3 = x2 + r + 10
        y3 = y2 + font_h

        self.draw_my_string(x3, y3, (0, 0, 0))

    def __str__(self):
        return f'Drawing Object {self.name} {self.color} {self.width} {self.height}'

#----------------------------------------------------------------
if __name__ == '__main__':
    mochan = Label('1', 'Aloha Mochan')

    mochan.init_surface()
    mochan.init_context()

    mochan.draw_label()
    mochan.save_image('mochan.png')
