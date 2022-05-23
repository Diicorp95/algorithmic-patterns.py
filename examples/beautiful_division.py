from wrap import *

s = []
h1 = []
width = 24
height = width
for i in range(height):
    i += 1
    _ = []
    for j in range(width):
        j += 1
        color = 0
        y = i / j
        if y in h1:
            color = 3
        else:
            h1.append(y)
        _.append(color)
    s.append(_)

s = endpix.upscale(s, 18, True)
endpix.plot(s, stored_ints = True, bitdepth = 2)
