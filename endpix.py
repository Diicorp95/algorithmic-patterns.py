#!/usr/bin/python3

#  endpix.py
#  ASCII image processing and output script. A part of the repository
#  < algorithmic_patterns.py >.
# -----------------------------------------------------------------------------
#  Coded by Larry "Diicorp95" Holst. UNLICENSE license. Read LICENSE file for
#  more information.

import png


def upscale(image, **kwargs):
    greyscale = kwargs.get("greyscale", True)
    size = kwargs.get("size", 2)
    stored_ints = kwargs.get("stored_ints", False)

    res = []
    if stored_ints:
        if greyscale:
            for j in image:
                a = []
                for k in j:
                    for l in range(size):
                        a.append(k)
                for l in range(size):
                    res.append(a)
        else:
            x = image

            # Group
            for i, j in enumerate(x):
                x[i] = [j[n : n + 3] for n in range(0, len(j), 3)]
            pre_res = []
            for row in x:
                line = []
                for pixel in row:
                    for l in range(size):
                        line.append(pixel)
                for l in range(size):
                    pre_res.append(line)

            # Ungroup
            res = []
            for row in pre_res:
                line = []
                for pixel in row:
                    for byte in pixel:
                        line.append(byte)
                res.append(line)
    else:
        for j in image:
            line = []
            for k in j:
                for l in range(size):
                    line += k
            for l in range(size):
                res.append(a)
    return res


def plot(image, **kwargs):
    stored_ints = kwargs.get("stored_ints", False)
    bitdepth = kwargs.get("bitdepth", 4)
    greyscale = kwargs.get("greyscale", True)
    width = kwargs.get("width", None)
    height = kwargs.get("height", None)
    filename = kwargs.get("filename", "endpix_plot.png")

    if not stored_ints:
        image = [[int(c, 16) for c in row] for row in image]
    if width is None:
        width = len(image[0])
    if height is None:
        height = len(image)
    w = png.Writer(width, height, greyscale=greyscale, bitdepth=bitdepth)
    f = open(filename, "wb")
    w.write(f, image)
    f.close()
