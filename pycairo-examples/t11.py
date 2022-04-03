import cairo
import math
import sys
import scaled_font
from t12 import set_source_color

#----------------------------------------------------------------
if __name__ =='__main__':
    image_file = 'image_' + sys.argv[0].replace('.py', '.png')
    width = 400
    height = 550
    line_width = 10
    font_size = 20

    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(surface)

    x = 40
    y = 30
    w = 320
    h = 500
    r = 20

    line_width = 20
    context.set_line_width(line_width)

    context.move_to(x+r, y)
    context.line_to(x+w-r-1, y)
    context.arc(x+w-r-1, y+r, r, -0.5*math.pi, 0)
    context.line_to(x+w-1, y+h-r-1)
    context.arc(x+w-r-1, y+h-r-1, r, 0, 0.5*math.pi)
    context.line_to(x+r, y+h-1)
    context.arc(x+r, y+h-r-1, r, 0.5*math.pi, math.pi)
    context.line_to(x, y+r)
    context.arc(x+r, y+r, r, math.pi, 1.5*math.pi)
    context.close_path()


    context.set_source_rgb(0xff/float(0xff), 0xff/float(0xff), 0x00/float(0xff))
    context.fill_preserve()
    context.set_source_rgb(0x00/float(0xff), 0x00/float(0xff), 0xff/float(0xff))

    context.stroke()

    x = 75
    y = 95

    context.set_source_rgb(0, 0, 0)
    r = 20
    line_width = 3
    context.set_line_width(line_width)
    context.arc(x, y, r, 0, math.pi * 2)
    context.stroke()

    str = '1'
    font_size = 30
    sf = scaled_font.get_scaled_font('Arial', font_size )
    extents = sf.text_extents(str)
    context.set_source_rgb(0, 0, 0)
    context.set_font_size(font_size)
    context.move_to(x, y)
    context.rel_move_to(-extents.width/2, -extents.height/2)
    context.rel_move_to(-extents.x_bearing, -extents.y_bearing)
    context.show_text(str)
    context.stroke()

    context.select_font_face('Hiragino Sans', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    x = 115
    y = 113
    str = 'こんにちは!'
    font_size = 40
    context.set_source_rgb(0, 0, 0)
    context.set_font_size(font_size)
    context.move_to(x, y)
    context.show_text(str)
    context.stroke()

    #surface.write_to_png(image_file)
    surface.write_to_png('3.png')

