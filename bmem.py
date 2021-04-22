import random as r
from os import path
import math

filename = "bmem.mem"
sprite_size = 256
sprite_width = 16
nsprites = 35
nloc = 1024


def rhex():
    h = str(hex(math.floor(r.random() * 16)))[2:]
    return h


def rcolor():
    return rhex() + rhex() + rhex()


hexmem = ""

for i in range(nsprites):
    sprite_file_name = f"sprites/{i}.bmp541"
    if path.isfile(sprite_file_name):
        print(f"found {sprite_file_name}")
        hexmem += open(sprite_file_name).read() + "\n"
    else:
        curr = "000000" if i == 0 else rcolor()
        for j in range(sprite_size):
            hexmem += curr + "\n"

with open(filename, "w") as bf:
    bf.write(hexmem[:-1])
