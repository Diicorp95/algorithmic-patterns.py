# ANSI manipulations functions

def horizontal_reflection(image):
    result = ''
    for line in image.split('\n'):
    result += line[::-1] + '\n'
    return result

def vertical_reflection(image):
    result = '\n'.join(image.split('\n')[::-1])
    return result

def add_horizontal_reflection(image, to_right_side = True):
    result = ''
    for line in image.split('\n'):
    if to_right_side:
        result += line + line[::-1]
    else:
        result += line[::-1] + line
    result += '\n'
    return result

def add_vertical_reflection(image, to_bottom = True):
    part = '\n'.join(image.split('\n')[::-1])
    result = part + '\n' + image
    return result
