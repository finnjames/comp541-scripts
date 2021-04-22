filename = "smem.mem"

sprite_size = 256
screen_size = 1200
rows = 30
cols = 40


def d2c(d):
    h = hex(d)
    return h[2:].zfill(2) + "\n"


smem_arr = [
    [1, 2, 3, 2, 4, 0, 7, 2, 2, 8, 0, 7, 2, 2, 8, 0, 15, 0, 0, 0, 15],
    [0, 0, 5, 0, 0, 0, 5, 0, 0, 5, 0, 5, 0, 0, 5, 0, 9, 2, 8, 0, 5],
    [0, 0, 5, 0, 0, 0, 9, 2, 3, 10, 0, 5, 0, 0, 5, 0, 5, 0, 5, 0, 5],
    [0, 0, 5, 0, 0, 0, 5, 0, 5, 0, 0, 5, 0, 0, 5, 0, 5, 0, 12, 2, 14],
    [0, 0, 6, 0, 0, 0, 6, 0, 12, 4, 0, 12, 2, 2, 10, 0, 6, 0, 0, 0, 6],
]

charsize = 3
bg = "00\n"

screenmem = "07\n" + "02\n" * 38 + "08\n"
screenmem += ("05\n" + bg * (cols - 2) + "05\n") * 11
for i in smem_arr:
    screenmem += "05\n" + bg * 8
    for j in i:
        screenmem += d2c(j)
    screenmem += bg * 9 + "05\n"
screenmem += ("05\n" + bg * (cols - 2) + "05\n") * 12
screenmem += "0c\n" + "02\n" * 38 + "0a\n"

# print(screen_size, int(len(screenmem)/charsize))
assert screen_size == int(len(screenmem) / charsize)

hexmem = screenmem[:-1]

with open(filename, "w") as bf:
    bf.write(hexmem)
