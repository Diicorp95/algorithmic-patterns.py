# ANSI output functions


def boxshade(color):
    palette = ["\u0020", "\u2591", "\u2592", "\u2593", "\u2588"]
    return palette[color % len(palette)]


def plot(pixels, widenchars=False, size=1, doPrint=True, useANSI=False):
    mt = size
    if widenchars:
        mt *= 2
    clear = (
        lambda: (
            print("\033[0;0m", end=""),
            print("\033[2J", end=""),
            print("\033[0;0H", end=""),
        )
        if useANSI
        else None
    )
    clear()
    _f = []
    for j in pixels:
        _ = ""
        for i2, k in enumerate(j):
            _ += "{}".format(boxshade(k) * mt)
        _f.append(_)
    y = ""
    for i, j in enumerate(_f):
        _ = ""
        for k in j:
            _ += k
        y += (_ + "\n") * size
    # else: ???
    y = y[:-1]  # Remove the last new line character
    if doPrint:
        print(y)
    else:
        return y
    input("")
    clear()
