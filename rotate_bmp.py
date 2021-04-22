import sys
import numpy as np

rotated = []
with open(f"sprites/{sys.argv[1]}.bmp541", "r") as f:
    arr = np.reshape(f.read().split(), (16, 16))
    rotated = [
        [arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]) - 1, -1, -1)
    ]

flat = ""

for i in rotated:
    for j in i:
        flat += j + "\n"

with open(f"sprites/{sys.argv[2]}.bmp541", "w") as f:
    f.write(flat)
