from lineus import LineUs

my_line_us = LineUs()

def drawing():
    my_line_us.connect()

    my_line_us.g01(900, 300, 1500)
    my_line_us.g01(900, -300, 1500)
    my_line_us.g01(900, -300, 1000)

    print('Hello')

    my_line_us.g01(1500, 300, 1500)
    my_line_us.g01(1500, -300, 1500)
    my_line_us.g01(1500, -300, 1000)

    my_line_us.g01(1500, 0, 1500)
    my_line_us.g01(1500, 0, 1500)
    my_line_us.g01(1500, 0, 1000)

    my_line_us.g01(1500, 150, 0)
    my_line_us.g01(1500, -300, 0)
    my_line_us.g01(1500, -300, 1000)

    my_line_us.g01(1500, 250, 0)
    my_line_us.g01(1500, 300, 0)
    my_line_us.g01(1500, 300, 1000)
    return drawing

def main():
    drawing()