#!/usr/bin/python3

#  pixelgrid.py
#  ASCII, ANSI output script. A part of the repository
#  < algorithmic_patterns.py >.
# -----------------------------------------------------------------------------
#  Coded by Larry "Diicorp95" Holst. UNLICENSE license. Read LICENSE file for
#  more information.

def boxshade(color):
    palette = ["\u0020", "\u2591", "\u2592", "\u2593", "\u2588"]
    return palette[color % len(palette)]


def plot(pixels, **kwargs):
    size = kwargs.get("size", 1)
    widen_characters = kwargs.get("widen_characters", False)
    actually_print = kwargs.get("actually_print", True)
    use_ANSI_codes = kwargs.get("use_ANSI_codes", False)

    if widen_characters:
        size *= 2

    clear = (
        lambda: (
            print("\033[0;0m", end=""),
            print("\033[2J", end=""),
            print("\033[0;0H", end=""),
        )
        if use_ANSI_codes
        else None
    )
    clear()

    rows = []
    for j in pixels:
        line = ""
        for i, k in enumerate(j):
            line += "{}".format(boxshade(k) * size)
        rows.append(line)

    res = ""
    for i, j in enumerate(_f):
        line = ""
        for k in j:
            line += k
        res += (line + "\n") * size

    res = res[:-1]  # Remove the last new line character
    if actually_print:
        print(res)
    else:
        return res
    input("")  # Wait for user reaction
    clear()
