from PIL import Image
import numpy as np
import math

with open("flag.raw", "rb") as f:
    data = f.read()

samples = list(data)
pixels = []
t = 0.0

# ptr[0] = (int)((sin(t/12480 * 15079.64) * (gray * 0.7 / 255) + 1.0) * 255 * 0.5)
for i in range(0, len(samples), 3):
    p = samples[i]
    sin_val = math.sin(t / 12480.0 * 15079.64473723101)

    if abs(sin_val) > 0.01:
        gray = ((p / (255 * 0.5)) - 1.0) / (sin_val * 0.7)
        gray *= 255.0
    else:
        gray = 0

    pixels.append(max(0, min(255, int(gray))))
    t += 3.0

output = np.array(pixels, dtype=np.uint8)
img = Image.fromarray(output.reshape((-1, 2080)))
img.save("extracted_signal.png")
