import cairo

#----------------------------------------------------------------
if __name__ == '__main__':
    image_file = 't2.png'
    width = 200
    height = 200
    line_width = 10
    font_size = 20

    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(surface)

    context.set_line_width(line_width)
    context.set_source_rgb(0xff/0xff, 0x99/0xff, 0)
    context.rectangle(10, 10, 100, 100)
    context.stroke()

    context.set_font_size(font_size)
    context.move_to(15, 35)
    context.show_text("こんにちは")
    context.stroke()

    surface.write_to_png(image_file)

