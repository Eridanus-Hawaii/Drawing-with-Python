import cairo
import math

#----------------------------------------------------------------
if __name__ == '__main__':
    image_file = 't3.png'
    width = 200
    height = 200
    line_width = 10
    font_size = 20

    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(surface)

    x = 40
    y = 50
    w = 120
    h = 100
    r = 20

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

    context.set_source_rgb(0xff/float(0xff), 0xff/float(0xff), 0xff/float(0xff))
    context.fill_preserve()
    context.set_source_rgb(0xff/float(0xff), 0x99/float(0xff), 0x00/float(0xff))
    context.stroke()

    context.set_font_size(font_size)
    context.move_to(15, 35)
    context.show_text("こんにちは")
    context.stroke()

    surface.write_to_png(image_file)

