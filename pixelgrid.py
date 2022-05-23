# ANSI output functions

# ~ def widen_colorhex(colorhex):
    # ~ if len(colorhex) == 3:
        # ~ x = colorhex
        # ~ y = ''
        # ~ for j in x:
            # ~ y += j * 2
    # ~ return colorhex

# ~ def rgb2ansi(colorhex):
    # ~ #print(f'rgb2ansi({colorhex})')
    # ~ trans = {
        # ~ '000000': 47,
        # ~ '808080': 100,
        # ~ 'FFFFFF': 107
    # ~ }
    # ~ x = trans.get(widen_colorhex(colorhex.strip().replace('#', '').lower()), 107)
    # ~ return x - 10

def boxshade(color):
    # ~ #print(f'boxshade({color})')
    # ~ '''trans = {
    # ~ 107: ' ',
    # ~ 100: '\2592'
    # ~ }'''
    # ~ color += 10
    # ~ if color == 107:
        # ~ return ' '
    # ~ elif color == 100:
        # ~ #return '\2592'
        # ~ return '▓'
    # ~ elif color > 100 and color < 107:
        # ~ #return '\2593'
        # ~ return '▒'
    # ~ else:
        # ~ #return '\2588'
        # ~ return '░'
    # ~ #result = trans.get(color, ' ')
    # ~ #return result
    palette = [
        '\u20',
        '\u2591',
        '\u2592',
        '\u2593',
        '\u2588'
    ]
    return palette[color % len(palette)]

def plot(pixels, widenchars = False, size = 1, doPrint = True, useANSI = False):
    mt = size
    if widenchars:
        mt *= 2
    clear = lambda: (print('\033[0;0m', end = ''),
        print('\033[2J', end = ''),
        print('\033[0;0H', end = '')) if useANSI else None
    clear()
    _f = []
    # ~ if colors:
        # ~ codes = []
    for i, j in enumerate(pixels):
        _ = ''
        # ~ tm = len(pixels[i])
        # ~ for k in range(tm):
        for i2, k in enumerate(pixels[i]):
            # ~ color = palette[j[k]]
            # ~ r1 = rgb2ansi(color)
            # ~ _ += '\033[0;{0:}m{1:}'.format(r1, boxshade(r1) * 2 * size)
            # ~ _ += '{}'.format(boxshade(color) * 2 * size)
            _ += '{}'.format(boxshade(k) * mt)
            # ~ if colors:
                # ~ for i in range(size):
                    # ~ codes.append('\033[0;{}m'.format(r1))
        # ~ if colors:
            # ~ codes.append('')
        _f.append(_)
    #input('\n\033[30;40m')
    y = ''
    for i, j in enumerate(_f):
        _ = ''
        for k in j:
            # ~ _ += codes[i]# if colors else ''
            _ += k # ~ * size
        else:
            y += (_ + '\n') * size
    if doPrint:
        print(y)
    else:
        return y
    input('\n')
    clear()
