import cairo
import math
import sys
import scaled_font
import matplotlib.colors as mcolors

class Label:
    def __init__(self, my_num, name):
        self.my_num = my_num
        self.name = name

        self.fill_color = 'blue'
        self.line_color = 'tomato'
        self.circle_color = 'yellow'
        self.string_color = 'white'

        self.font_size = 30

        self.line_width = 10

        self.width = 400
        self.height = 400

        self.frame_r = 20
        self.circle_r = 20

        self.surface = None
        self.context = None
    
    def init_surface(self):
        print('Creating initial surface')
        self.width = 400
        self.height = 400
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

    def draw_frame(self, x, y, w, h, r):
        print(f'Draw frames{self.fill_color} {self.width} {self.height}')

        self.set_source_color(self.fill_color)
        self.context.set_line_width(self.line_width)

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

        self.context.fill_preserve()        #ベースとなる色
        self.set_source_color(self.line_color)
        self.context.stroke()       #周りを囲う線

    def draw_circle_num(self, x, y, r):
    # print("円を描いて番号も描く", x, y, r, num, color)
        print(f'Draw circle {self.width} {self.height}')
        self.set_source_color(self.circle_color)
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

    def draw_my_string(self, x, y):
        print(f'Write word{self.width} {self.height}')

        self.context.select_font_face('Hiragino Sans', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

        self.set_source_color(self.string_color)
        self.context.set_font_size(self.font_size)
        self.context.move_to(x, y)
        self.context.show_text(self.name)
        self.context.stroke()

    def draw_label(self, x, y, w, h):
        frame_r = 20
        self.draw_frame(x, y, w, h, self.frame_r)

        circle_r = 20
        self.draw_circle_num(x +35, y +h/2, self.circle_r)

        self.draw_my_string(x +65, y +h/2)

#----------------------------------------------------------------
if __name__ == '__main__':
    mochan = Label('1', 'Aloha Mochan')

    mochan.init_surface()
    mochan.init_context()

    mochan.draw_label(10, 10, 380, 180)
    # mochan.draw_frame(10, 10, 380, 80, 20)
    # mochan.draw_circle_num(45, 50, 20)
    # mochan.draw_my_string(75, 60)
    mochan.save_image('MOCHAN.png')