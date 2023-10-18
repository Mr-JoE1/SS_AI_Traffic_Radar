
# Converts kicad_sym file into old lib file for stroke font.
# This converter supports only fixed width glyph such as 
# Chinese characters, hiragana and katakana.

import sys

from sexpdata import loads, dumps, Symbol

lib_header = """EESchema-LIBRARY Version 2.4
#encoding utf-8"""

lib_footer = """#
#End Library"""

symbol_header = """#
# {NAME}
#
DEF {NAME} U 0 40 Y Y 1 F N
F0 "U" 0 -250 60 H V C CNN
F1 "{NAME}" 0 -350 60 H V C CNN
F2 "" 0 0 50 H I C CNN
F3 "" 0 0 50 H I C CNN
DRAW"""

symbol_footer = """ENDDRAW
ENDDEF
"""


def read_data(path):
    with open(path) as f:
        return f.read()


symbol_pts = Symbol('pts')
symbol_xy = Symbol('xy')

def write_polyline(pts):
    if pts[0] == symbol_pts:
        points = []
        for xy in pts[1:]:
            if xy[0] == symbol_xy:
                x = xy[1] / 0.0254
                y = xy[2] / 0.0254
                points.append("{:.0f} {:.0f}".format(x, y))
        print("P {COUNT} 0 1 0 {POINTS} N".format(
            COUNT=len(points), POINTS=" ".join(points)))


def write_pin(pin):
    t = {"input": "I"}[pin[1].value()]
    name = ""
    for p in pin[3:]:
        if isinstance(p, list):
            tag = p[0].value()
            if tag == "at":
                x = int(p[1] / 0.0254)
                y = int(p[2] / 0.0254)
                direction = {90: "U"}[p[3]]
            elif tag == "length":
                length = int(p[1] / 0.0254)
            elif tag == "name":
                name = p[1]
                height1 = 50
            elif tag == "number":
                number = p[1]
                height2 = 50
    if name != "":
        s = "X {NAME} {NUMBER} {X} {Y} {LENGTH} {DIRECTION} {HEIGHT1} {HEIGHT2} 1 1 {TYPE}".format(
            NAME=name, NUMBER=number, X=x, Y=y, LENGTH=length,
            DIRECTION=direction, HEIGHT1=height1, HEIGHT2=height2, TYPE=t)
        print(s)


def main():
    if len(sys.argv) != 2:
        print("Pass kicad_sym file to convert")
        return
    path = sys.argv[1]
    data = read_data(path)

    symbol_tag = Symbol('symbol')
    symbol_rectangle = Symbol('rectangle')
    symbol_polyline = Symbol('polyline')
    symbol_pin = Symbol('pin')

    s = loads(data)

    print(lib_header)

    for symbol in s[3:]:
        if symbol[0] == symbol_tag:
            name = symbol[1].split(':')[1]
            header = symbol_header.format(NAME=name)
            print(header)
            for elem in symbol[3:]:
                if elem[0] == symbol_tag:
                    for items in elem[2:]:
                        if items[0] == symbol_rectangle:
                            continue
                        elif items[0] == symbol_polyline:
                            write_polyline(items[1])
                        elif items[0] == symbol_pin:
                            write_pin(items)
            print(symbol_footer)
    print(lib_footer)

main()

