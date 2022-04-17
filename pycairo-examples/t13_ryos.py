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

#----------------------------------------------------------------
def draw_frame(ctx, x, y, w, h, r):
    print("フレームを描く", x, y, w, h, r)
    line_width = 20
    ctx.set_line_width(line_width)

    ctx.move_to(x+r, y)
    ctx.line_to(x+w-r-1, y)
    ctx.arc(x+w-r-1, y+r, r, -0.5*math.pi, 0)
    ctx.line_to(x+w-1, y+h-r-1)
    ctx.arc(x+w-r-1, y+h-r-1, r, 0, 0.5*math.pi)
    ctx.line_to(x+r, y+h-1)
    ctx.arc(x+r, y+h-r-1, r, 0.5*math.pi, math.pi)
    ctx.line_to(x, y+r)
    ctx.arc(x+r, y+r, r, math.pi, 1.5*math.pi)
    ctx.close_path()

    #ctx.set_source_rgb(0xff/float(0xff), 0xff/float(0xff), 0xff/float(0xff))
    set_source_color(ctx, 'tomato')
    ctx.fill_preserve()

    #ctx.set_source_rgb(0xff/float(0xff), 0x99/float(0xff), 0x00/float(0xff))
    #set_source_color(ctx, 'seagreen')
    set_source_color(ctx, 'blueviolet')
    #set_source_color(ctx, 'c')
    ctx.stroke()

#----------------------------------------------------------------
def draw_circle_num(ctx, x, y, r, num, color):
    print("円を描いて番号も描く", x, y, r, num)

    #ctx.set_source_rgb(0, 0, 0)
    ctx.set_source_rgb(color[0], color[1], color[2])

    line_width = 3
    ctx.set_line_width(line_width)
    ctx.arc(x, y, r, 0, math.pi * 2)
    ctx.stroke()

    font_size = 30
    sf = scaled_font.get_scaled_font('Arial', font_size )
    extents = sf.text_extents(num)
    ctx.set_font_size(font_size)
    ctx.move_to(x, y)
    ctx.rel_move_to(-extents.width/2, -extents.height/2)
    ctx.rel_move_to(-extents.x_bearing, -extents.y_bearing)
    ctx.show_text(num)
    ctx.stroke()

#----------------------------------------------------------------
def draw_my_string(ctx, x, y, str, color):
    print('draw_my_string', x, y, str, color)

    ctx.select_font_face('Ricty Diminished', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

    font_size = 30
    #ctx.set_source_rgb(0, 0, 0)
    ctx.set_source_rgb(color[0], color[1], color[2])

    ctx.set_font_size(font_size)
    ctx.move_to(x, y)
    ctx.show_text(str)
    ctx.stroke()
    
#----------------------------------------------------------------
def draw_label(ctx, my_x, my_y, my_num, my_str):
    #print(my_x, my_y, 'に移動して')
    #print(my_num, 'を描画')
    #print(my_str, 'を描画')

    w = 320
    h = 150
    r = 20

    draw_frame     (ctx, my_x     , my_y     , w, h, r)
    draw_circle_num(ctx, my_x + 30, my_y + 75, r, my_num, (0, 0, 0))
    draw_my_string (ctx, my_x + 60, my_y + 85, my_str, (0, 0, 0))

#----------------------------------------------------------------
if __name__ == '__main__':
    image_file = 'image_' + sys.argv[0].replace('.py', '.png')
    width = 400
    height = 200
    line_width = 10
    font_size = 20

    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(surface)

    draw_label(context, 10, 10, '1', 'HelloHelloHello')

    surface.write_to_png(image_file)
