import cairo
import sys
import json
import math

def get_scaled_font(family, font_size, slant = cairo.FONT_SLANT_NORMAL, weight = cairo.FONT_WEIGHT_NORMAL):
    surface =  cairo.ImageSurface(cairo.FORMAT_ARGB32, 100, 100)
    ctx = cairo.Context(surface)
    ctx.select_font_face(family, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(font_size)
    sf = ctx.get_scaled_font()
    ctx = None
    surface = None

    return sf

class StringWithFontMetric:
    def __init__(self, str, font_face, font_size):
        self.str = str
        self.font_face = font_face
        self.font_size = font_size
        font_matrix = cairo.Matrix(self.font_size, 0, 0, self.font_size, 0, 0)
        ctm_matrix = cairo.Matrix(1, 0, 0, 1, 0, 0)
        self.sf = cairo.ScaledFont(self.font_face, font_matrix, ctm_matrix, cairo.FontOptions())

    def get_extents(self):
        return self.sf.text_extents(self.str)

    def draw_text(self, ctx):
        point = ctx.get_current_point()
        #print(point, self.str)
        ctx.set_scaled_font(self.sf)

        ctx.show_text(self.str)
        ctx.stroke()
        extents = self.sf.text_extents(self.str)
        rv = ( point[0] + extents.x_advance, point[1] + extents.y_advance )
        ctx.move_to(rv[0], rv[1])
        #print(rv)
        return rv

    def get_total_extents(str_list):
        extents = str_list[0].get_extents()
        width = extents.width
        x_advance = extents.x_advance
        for str_font in str_list[1:]:
            an_extents = str_font.get_extents()
            width += an_extents.width
            x_advance += an_extents.x_advance
        return cairo.TextExtents(extents.x_bearing, extents.y_bearing, width, extents.height, x_advance, extents.y_advance)


def get_extents(str, font_size):
    surface =  cairo.ImageSurface(cairo.FORMAT_ARGB32, 100, 100)
    ctx = cairo.Context(surface)
    ctx.select_font_face('Ricty Diminished', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    #ctx.select_font_face('Arial', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(font_size)
    sf = ctx.get_scaled_font()
    extents = sf.text_extents(str)
    ctx = None
    surface = None

    return extents


def draw_num(ctx, num_str, x, y, r, line_width, font_size, fgcolor, delta):
    ctx.set_source_rgb(fgcolor[0]/float(0xff), fgcolor[1]/float(0xff), fgcolor[2]/float(0xff))
    ctx.set_line_width(line_width)
    ctx.arc(x, y, r, 0, math.pi * 2)
    ctx.stroke()

    ctx.set_font_size(font_size)
    sf = ctx.get_scaled_font()
    str = f'{num_str}'
    extents = sf.text_extents(str)
    ctx.move_to(x+delta[0]-extents.width/2, y+delta[1]+extents.height/2)
    ctx.show_text(str)
    ctx.stroke()

def make_frame(ctx, x, y, w, h, r, line_width, bgcolor, framecolor):
    ctx.set_line_width(line_width)
    x += line_width / 2
    y += line_width / 2
    w -= line_width
    h -= line_width
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

    ctx.set_source_rgb(bgcolor[0]/float(0xff), bgcolor[1]/float(0xff), bgcolor[2]/float(0xff))
    ctx.fill_preserve()
    ctx.set_source_rgba(framecolor[0]/float(0xff), framecolor[1]/float(0xff), framecolor[2]/float(0xff))
    ctx.stroke()

    #ctx.move_to(0, 0)
    #ctx.line_to(width, 0)
    #ctx.line_to(width, height)
    #ctx.line_to(0, height)
    #ctx.line_to(0, 0)
    #ctx.close_path()
    #ctx.clip()

def process_text(ctx, width, height, font_size, line_width, num, blank, str, extents, margins, font_color, bg_color, frame_color, delta, delta_for_str):

    #----------------------------------------------------------------
    r = font_size / 2
    make_frame(ctx, 0, 0, width, height, r, line_width, bg_color, frame_color)

    #----------------------------------------------------------------
    # 数字のフォント
    ctx.set_line_width(1)
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()
    ctx.select_font_face('Arial', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    num_font_size = font_size / 2
    ctx.set_font_size(num_font_size)
    x = line_width + margins[3] + r
    y = line_width + margins[0] + extents.height / 2
    arc_width = 3
    draw_num(ctx, num, x, y, r, arc_width, num_font_size, (0, 0, 0), delta)

    #----------------------------------------------------------------
    x = line_width + margins[3] + font_size + blank + delta_for_str[0]
    y = line_width + margins[0] + int(abs(extents.y_bearing)) + delta_for_str[1]
    ctx.select_font_face('Ricty Diminished', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(font_size)
    ctx.move_to(x, y)
    ctx.show_text(str)
    ctx.stroke()

#----------------------------------------------------------------
def process_text_list(ctx, width, height, font_size, line_width, num, blanks, str_font_list, total_extents, margins, font_color, bg_color, frame_color, delta, delta_for_str):
    #----------------------------------------------------------------
    r = font_size / 2
    make_frame(ctx, 0, 0, width, height, r, line_width, bg_color, frame_color)

    #----------------------------------------------------------------
    # 数字のフォント
    ctx.set_line_width(1)
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()
    ctx.select_font_face('Arial', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    num_font_size = font_size / 2
    ctx.set_font_size(num_font_size)
    x = line_width + margins[3] + r
    y = line_width + margins[0] + total_extents.height / 2
    arc_width = 3
    draw_num(ctx, num, x, y, r, arc_width, num_font_size, (0, 0, 0), delta)

    #print('num:', num)

    #----------------------------------------------------------------
    x = line_width + margins[3] + font_size + delta_for_str[0]
    y = line_width + margins[0] + int(abs(total_extents.y_bearing)) + delta_for_str[1]
    ctx.move_to(x, y)
    for i, str_font in enumerate(str_font_list):
        ctx.rel_move_to(blanks[i], 0)
        new_point = str_font.draw_text(ctx)

#----------------------------------------------------------------
def create_str_list(raw_str_list, font_family, font_size):
    lst = []
    for str in raw_str_list:
        toy_font = None
        for ast_x in (('***', cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_BOLD), ('**', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD), ('*',cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)):
            ast = ast_x[0]
            la = len(ast)
            #print( len(str) > (la*2), str[:la] , ast, str[-la:] , ast)
            #print(f'_{str[:la]}_{str[-2:]}_')
            if ( len(str) > (la*2) and str[:la] == ast and str[-la:] == ast):
                toy_font = cairo.ToyFontFace(font_family, ast_x[1], ast_x[2])
                new_str = str.strip('***')
                break

        if toy_font == None:
            toy_font = cairo.ToyFontFace(font_family, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            str_font = StringWithFontMetric(str, toy_font, font_size)
        else:
            str_font = StringWithFontMetric(new_str, toy_font, font_size)
        lst.append(str_font)
                
    return lst

#----------------------------------------------------------------
def draw_to_png(font_family, font_size, line_width, num, blanks, raw_str_list, margins, font_color, bg_color, frame_color, delta, delta_for_str, image_file):

        str_font_list = create_str_list(raw_str_list, font_family, font_size)
        total_extents = StringWithFontMetric.get_total_extents(str_font_list)

        total_blank = 0
        for e in blanks:
            total_blank += e
        #print('total_blank:', total_blank)
        width = int(line_width + margins[3] + font_size + total_blank + total_extents.x_advance + margins[1] + line_width)
        height = int(line_width + margins[0] + total_extents.height + margins[2] + line_width)
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        context = cairo.Context(surface)

        process_text_list(context, width, height, font_size, line_width, num, blanks, str_font_list, total_extents, margins, font_color, bg_color, frame_color, delta, delta_for_str)

        surface.write_to_png(image_file)

#----------------------------------------------------------------
if __name__ == '__main__':
    output_name = 'test.png'

    font_size = 60
    line_width = 20
    blanks = [50, 50, 0, 0]
    margins = (20, 40, 20, 20)

    num = '1'
    delta = (-3 , -1)

    raw_str_list = ['こんにちは', 'さよ', '**おなら**', 'です']
    blanks = [0] * len(raw_str_list)
    blanks[0] = 50
    delta_str = (0, -2)
    file_name = 'test0.png'

    if len(sys.argv) > 3:
        file_name = sys.argv[1]
        num = sys.argv[2]
        raw_str_list = sys.argv[3:]
        blanks = [0] * len(raw_str_list)
        blanks[0] = 20
        if num == '1':
            delta = (-3, -1)
        else:
            delta = (-1, -1)

    #blanks[2] -=20
    #blanks[3] +=40

    #margins = (120, 70, 150, 120)
        

    '''
    #sf = get_scaled_font('Ricty Diminished', font_size, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    #print(sf.get_font_matrix())

    num = 'IV'
    delta = (-4 , -1)

    str = '100円を入れる'
    str = 'あ〜こりゃこりゃ'
    str = '無駄にいろいろ調整可能'
    delta_str = (0, -2)

    toy_font0 = cairo.ToyFontFace('Ricty Diminished', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    str_font0 = StringWithFontMetric(str, toy_font0, 60)
    toy_font1 = cairo.ToyFontFace('Ricty Diminished', cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_BOLD)
    str_font1 = StringWithFontMetric(str, toy_font1, 60)

    str_list = [str_font0, str_font1]
    total_extents = StringWithFontMetric.get_total_extents(str_list)

    #print(width, height)

    #fo = cairo.FontOptions()
    #fo.set_antialias(cairo.ANTIALIAS_SUBPIXEL)
    #sf = cairo.ScaledFont(cairo.ToyFontFace('Ricty Diminished', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL) , cairo.Matrix(), cairo.Matrix(), fo)
    #print(sf.text_extents('Hello'))

    #process_text(context, width, height, font_size, line_width, num, blank, str, esize, margins, (0, 0, 0), (255, 255, 255), (0xFF, 0x99, 0), delta, delta_str)
    '''

    draw_to_png('Ricty Diminished', font_size, line_width, num, blanks, raw_str_list, margins, (0, 0, 0), (255, 255, 255), (0xFF, 0x99, 0), delta, delta_str, file_name)


