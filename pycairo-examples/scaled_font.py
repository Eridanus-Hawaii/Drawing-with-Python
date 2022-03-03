import cairo

def get_scaled_font(family, font_size, slant = cairo.FONT_SLANT_NORMAL, weight = cairo.FONT_WEIGHT_NORMAL):
    surface =  cairo.ImageSurface(cairo.FORMAT_ARGB32, 100, 100)
    ctx = cairo.Context(surface)
    ctx.select_font_face(family, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(font_size)
    sf = ctx.get_scaled_font()
    ctx = None
    surface = None

    return sf

#----------------------------------------------------------------
if __name__ == '__main__':
    sf = get_scaled_font('Arial', 30 )
    extents = sf.text_extents('1')
    print(extents)
