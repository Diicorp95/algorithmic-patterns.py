import png


def upscale(image, size=2, stored_ints=False, greyscale=True):
    y = []
    if stored_ints:
        if greyscale:
            for j in image:
                a = []
                for k in j:
                    for l in range(size):
                        a.append(k)
                for l in range(size):
                    y.append(a)
        else:
            x = image
            for i, j in enumerate(x):
                x[i] = [j[n : n + 3] for n in range(0, len(j), 3)]  # Group
            pre_y = []
            for row in x:
                a = []
                for pixel in row:
                    for l in range(size):
                        a.append(pixel)
                for l in range(size):
                    pre_y.append(a)
            # Ungroup
            y = []
            for row in pre_y:
                rown = []
                for pixel in row:
                    for byte in pixel:
                        rown.append(byte)
                y.append(rown)
    else:
        for j in image:
            a = []
            for k in j:
                for l in range(size):
                    a += k
            for l in range(size):
                y.append(a)
    return y


def plot(image, **kwargs):
    """
    **kwargs { stored_ints = False, bitdepth = 4, greyscale = True, width = None, height = None, filename = 'png_test.png' }
    """
    # - kwargs begin -
    stored_ints = kwargs.get("stored_ints", False)
    bitdepth = kwargs.get("bitdepth", 4)
    greyscale = kwargs.get("greyscale", True)
    width = kwargs.get("width", None)
    height = kwargs.get("height", None)
    filename = kwargs.get("filename", "endpix_plot.png")
    # - kwargs end -
    # ~ print('Plotting...')
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
