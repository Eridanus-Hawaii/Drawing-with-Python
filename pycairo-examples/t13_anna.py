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

def draw_frame(ctx, x, y, w, h, r):
    # outside purple frame and background 
    print("draw outside photoframe", x, y, w, h, r)
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
    set_source_color(ctx, 'plum') # now takes matpltlib color
    ctx.fill_preserve()

    #ctx.set_source_rgb(0xff/float(0xff), 0x99/float(0xff), 0x00/float(0xff))
    set_source_color(ctx, 'blueviolet')
    ctx.stroke()

def draw_circle_num(ctx, x, y, r, num, color):
    # first circle at very left including number inside
    print('draw circle and put number inside', x, y, r, num, color)

    #ctx.set_source_rgb(0, 0, 0)
    # drawing circle 
    ctx.set_source_rgb(color[0], color[1], color[2])
    line_width = 3
    ctx.set_line_width(line_width)
    ctx.arc(x, y, r, 0, math.pi * 2)
    ctx.stroke()

    # writing number '1'
    font_size = 30
    sf = scaled_font.get_scaled_font('Arial', font_size )
    extents = sf.text_extents(num)
    ctx.set_font_size(font_size)
    ctx.move_to(x, y)
    ctx.rel_move_to(-extents.width/2, -extents.height/2)
    ctx.rel_move_to(-extents.x_bearing, -extents.y_bearing)
    ctx.show_text(num)
    ctx.stroke()

def draw_my_string(ctx, x, y, str, color):
    # write any word inside the picture 
    print('draw string inside square', x, y, str, color)
    ctx.select_font_face('Hiragino Sans', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

    font_size = 30
    ctx.set_source_rgb(color[0], color[1], color[2])
    ctx.set_font_size(font_size)
    ctx.move_to(x, y)
    ctx.show_text(str)
    ctx.stroke()


def draw_label(ctx, my_num, my_str, width, height):
    """
    Draw a label into ctx.
    Parameters:
    -----------
    ctx: context
        a context of cairo.
    ny_num: string 
        number goes into a first circle. 
    my_str: string 
        words that comes after the numbered circle
    width: integer
        outside frame length of side
    height: integer
        height of the frame
    Returns:
    ---------
        None 
    """
    print('draw', my_num)
    print('draw', my_str)

    #  all function included 
    line_width = 20
    w = width - line_width / 2 - line_width / 2 
    h = height - line_width / 2 - line_width / 2  # linewidth is for top and bottom 
    r = 20

    x = line_width / 2
    y = line_width / 2 
    draw_frame(ctx, x, y, w, h, r)

    x2 = x + line_width / 2 + r + 5 # for circle 1 starting point 
    y2 = y + h / 2
    draw_circle_num(ctx, x2, y2, r, my_num, (0, 0, 0))

    x3 = x2 + r + 5
    y3 = y2 + 10 
    draw_my_string(ctx, x3, y3, my_str, (0, 0, 0))


if __name__ == '__main__':
    image_file = 'image_' + sys.argv[0].replace('.py', '.png')
    image_file1 = 'image_frame_practice.png'
    image_file2 = 'image_num_practice.png'
    image_file3 = 'image_string_practice.png'
    image_file4 = 'image_complete.png'
    width = 400
    height = 100
    line_width = 10
    font_size = 20

    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    ex_context = cairo.Context(surface)

    #draw_frame(ex_context, 140, 50, 380, 100, 40)
    #draw_circle_num(ex_context, 10, 10, 20, '1', (255, 255, 255))
    draw_label(ex_context, '1', 'Aloha', width, height)
    #draw_my_string(ex_context, 10, 30, 'Hello', (255, 255, 255))
    surface.write_to_png(image_file)
