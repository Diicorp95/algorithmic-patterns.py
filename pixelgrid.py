# ANSI output functions

def boxshade(color):
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
    for i, j in enumerate(pixels):
        _ = ''
        for i2, k in enumerate(pixels[i]):
            _ += '{}'.format(boxshade(k) * mt)
        _f.append(_)
    y = ''
    for i, j in enumerate(_f):
        _ = ''
        for k in j:
            _ += k
        else:
            y += (_ + '\n') * size
    if doPrint:
        print(y)
    else:
        return y
    input('\n')
    clear()
