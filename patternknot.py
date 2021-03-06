#!/usr/bin/python3

#  PatternKnot. patternknot.py v0.8.
#  PatternKnot is a parser and evaluator for *.ptkn files. A part of the
#  repository < algorithmic_patterns.py >.
# -----------------------------------------------------------------------------
#  Coded by Larry "Diicorp95" Holst. UNLICENSE license. Read LICENSE file for
#  more information.

import os
import math
import endpix


CONSOLE_HELP = """\
PatternKnot is a parser and evaluator for *.ptkn files. A part of the
repository < algorithmic_patterns.py >.

Copyleft (c) Larry "Diicorp95" Holst. Licensed under UNLICENSE license.

Usage: %s < filename > [ output file (PNG) ]

Arguments:
    filename ....................... The path to a PatternKnot file
    output file (PNG) .............. The path to a PNG file
                                     (optional)
"""

def __parse_arguments():
    parser = argparse.ArgumentParser(prog='PatternKnot', conflict_handler='resolve')
    parser.add_argument('-f', '--foo', help='old foo help')
    parser.add_argument('--foo', help='new foo help')
    parser.print_help()

    if x:
        print('x')
    else:
        print(CONSOLE_HELP)


def __display_help():
    text = CONSOLE_HELP % os.path.basename(sys.argv[0])
    print(text)
    raise SystemExit


def decode_and_run(string):
    # decode_and_run(string)
    # string: str
    #         a PatternKnot expression
    # return: str

    evaluated = []
    ops = {
        "$": "x",
        "~": "255 ^ ",
    }
    allowed = [
        "%",
        "&",
        "|",
        "^",
        "+",
        "-",
        "*",
        "/",
        "//",
        "(",
        ")",
        "<",
        ">",
        "=",
        ".",
        "w",
        "h",
    ]
    ints = [str(i) for i in range(10)]
    keywords = ["if", "else", "int", "ceil", "floor"]

    # 2 quick tests:
    ts = string.replace(" ", "")
    found_keyword = False
    for key in keywords:
        if key in ts:
            found_keyword = True
            break
    for char in ts:
        if (
            not char in allowed
            and not char in list(ops.keys())
            and not char in ints
            and not found_keyword
        ):
            raise SyntaxError

    # Flags
    flagc = 2 + len(keywords)
    """
        Flags information table
        .......................................................................
        Total count:            in $flagc
        #1                      Replacing "~$" with "(255 ^ x)" instead of
                                automatic "255 ^ x" to achieve separation.
                                If you really want to have it without
                                separation, then specify "255 ^ $" in files.
        #2                      <reserved>
        from #3 to #7           A safe way of adding keywords for eval call.
    """
    flagv = [0] * flagc

    # Main loop
    cmd = cmdquery = ""
    length = len(string)
    for i, j in enumerate(string):
        lastchar = i == length - 1
        j = j.strip()
        if j in allowed or j in ints:
            cmd = j.replace("w", "b").replace("h", "a")
        else:
            cmd = ops.get(j, None)

        key = keywords[0]
        if j == key[0] and flagv[2] == 0:
            flagv[2] += 1
        elif j == key[-1] and flagv[2] == 1:
            flagv[2] = 0
            cmd = " {} ".format(key)

        key = keywords[1]
        if (
            (j == key[0] and flagv[3] == 0)
            or (j == key[1] and flagv[3] == 1)
            or (j == key[2] and flagv[3] == 2)
        ):
            flagv[3] += 1
            # ~ continue
        elif j == key[-1] and flagv[3] == 3:
            flagv[2] = 0
            cmd = " {} ".format(key)

        key = keywords[2]
        if (j == key[0] and flagv[4] == 0) or (j == key[1] and flagv[4] == 1):
            flagv[4] += 1
            # ~ continue
        elif j == key[2] and flagv[4] == 2:
            flagv[4] = 0
            cmd = key

        key = keywords[3]
        if (
            (j == key[0] and flagv[5] == 0)
            or (j == key[1] and flagv[5] == 1)
            or (j == key[2] and flagv[5] == 2)
        ):
            flagv[5] += 1
        elif j == key[-1] and flagv[5] == 3:
            flagv[5] = 0
            cmd = "math.{}".format(key)

        key = keywords[4]
        if (
            (j == key[0] and flagv[6] == 0)
            or (j == key[1] and flagv[6] == 1)
            or (j == key[2] and flagv[6] == 2)
            or (j == key[3] and flagv[6] == 3)
        ):
            flagv[6] += 1
        elif j == key[-1] and flagv[6] == 4:
            flagv[6] = 0
            cmd = "math.{}".format(key)

        if cmd is None:
            continue

        if flagv[0] == 1:
            if j == "$":
                # Solution 1: cmd = '(~$)'
                cmd = "(255 ^ x)"  # Solution 2
            else:
                cmd = cmdquery + cmd
                cmdquery = ""
            flagv[0] = 0  # skip
        elif j == "~" and not lastchar:
            if flagv[0] == 0:
                flagv[0] = 1  # search
                continue
            else:
                continue
        evaluated.append(cmd)
        cmd = ""
    # Solution 1: evaluated = ' '.join(evaluated)
    evaluated = "".join(evaluated)  # Solution 2
    print(evaluated)
    if evaluated:
        return evaluated


def __param_proc(line, which):
    # __param_proc(line, which)
    # string: str
    #         a PatternKnot expression
    # return: None / int / bool

    value = line.replace(" ", "_").replace("_", "").replace("or", "our")
    if which == 0:
        key = "width"
    elif which == 1:
        key = "height"
    elif which == 2:
        key = "upscalex"
    elif which == 3:
        key = "bitdepth"
    elif which == 4:
        key = "colourful"
    if not value[0 : len(key) + 1].lower() == key + ":":
        if which >= 2:  # Optional parameters
            return -1
        raise SyntaxError
    if which == 4:
        return True
    try:
        value = int(value[len(key) + 1 :][0:4])
    except:
        raise SyntaxError
    if which < 2 and value >= 2048:
        raise ArithmeticError
    elif which >= 2:
        if value >= 128:
            raise ArithmeticError
        elif which == 2 and value <= 1:
            return -2
    return value


def parse(filepath):
    # parse(filepath)
    # filepath: a string object
    #           a path to a PatternKnot file

    real_fn = os.path.abspath(filepath)
    content = open(real_fn, "r").readlines()
    fsize = os.path.getsize(real_fn)

    if fsize <= 0:
        raise IOError or SyntaxError

    print("File size:", fsize, "B")
    to_test = content
    content = []

    for i, j in enumerate(to_test):
        # Remove the comments
        comment = j.find("#")
        if comment > -1:
            j = j[:comment]

        re_line = j.strip().replace("\n", "").replace("\r", "")
        if re_line:  # ~ and re_line[0] != "#"
            content.append(re_line)

    magic_beginning = "--- BEGIN PATTERNKNOT FILE ---"
    magic_end = "--- END PATTERNKNOT FILE ---"
    verified = content[0] == magic_beginning and content[-1] == magic_end

    if verified:
        content = content[1:-1]
    else:
        raise SyntaxError
    if not content:
        return None
    width = __param_proc(content[0], 0)
    height = __param_proc(content[1], 1)
    upscale = __param_proc(content[2], 2)
    next_index = 2
    if upscale < 0:
        upscale = 1
    else:
        next_index += 1
    bitdepth = __param_proc(content[next_index], 3)
    if bitdepth == -1:
        bitdepth = 4
    else:
        next_index += 1
    colourful = __param_proc(content[next_index], 4)
    if colourful == -1:
        colourful = False
    else:
        next_index += 1
    first = content[next_index]
    if first.replace(" ", "")[0] == "=":
        first_equality = first.find("=")
        cut_from = first.find("#")
        if cut_from > -1:
            first = first[:cut_from]
        line = first[first_equality + 1 :].strip()
    else:
        raise SyntaxError(first + " " + str(next_index))
    evaluated = decode_and_run(line.lower())

    res = [lambda x: int(eval(evaluated)), width, height, upscale, bitdepth,
        colourful]
    return res


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        fn = sys.argv[1]
    else:
        __display_help()
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    else:
        output_file = "patternknot_render.png"  # Default
    content = parse(fn)
    for i, j in enumerate(content):
        if i == 0:
            func = j
        elif i == 1:
            width = j
        elif i == 2:
            height = j
        elif i == 3:
            upscale = j
        elif i == 4:
            bitdepth = j
        elif i == 5:
            colourful = j

    if func:
        i = 0
        line_1 = []
        for b in range(height):
            line_2 = []
            for a in range(width):
                line_2.append(func(i))
                i += 1
            line_1.append(line_2)
            i += 1

    image = []
    real_limit = 2 ** bitdepth
    for row in line_1:
        row_2 = []
        for pixel in row:
            # Solution 1: b2 += hex(pixel % real_limit)[2:].zfill(real_limit // 16)
            # Solution 2: b2.append(pixel % 256)
            b2.append(pixel % real_limit)  # Solution 3
        image.append(row_2)

    if upscale > 1:
        greyscale = not colorful
        image = endpix.upscale(
            image,
            greyscale=greyscale,
            upscale=upscale,
            stored_ints=True
        )
    rw = width * upscale
    rh = height * upscale
    greyscale = not colorful
    endpix.plot(
        image,
        stored_ints=True,
        bitdepth=bitdepth,
        greyscale=greyscale,
        width=rw,
        height=rh,
        filename=output_file,
    )

    out_size = os.path.getsize(output_file)
    print("Output file size:", out_size, "B")
