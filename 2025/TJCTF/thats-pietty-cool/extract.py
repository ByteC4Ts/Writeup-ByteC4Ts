from PIL import Image

cmap = [
    (0xFF, 0xFF, 0xFF),  # white
    (0x00, 0x00, 0x00),  # black

    (0xFF, 0xC0, 0xC0),  # light red
    (0xFF, 0xFF, 0xC0),  # light yellow
    (0xC0, 0xFF, 0xC0),  # light green
    (0xC0, 0xFF, 0xFF),  # light cyan
    (0xC0, 0xC0, 0xFF),  # light blue
    (0xFF, 0xC0, 0xFF),  # light magenta

    (0xFF, 0x00, 0x00),  # red
    (0xFF, 0xFF, 0x00),  # yellow
    (0x00, 0xFF, 0x00),  # green
    (0x00, 0xFF, 0xFF),  # cyan
    (0x00, 0x00, 0xFF),  # blue
    (0xFF, 0x00, 0xFF),  # magenta

    (0xC0, 0x00, 0x00),  # dark red
    (0xC0, 0xC0, 0x00),  # dark yellow
    (0x00, 0xC0, 0x00),  # dark green
    (0x00, 0xC0, 0xC0),  # dark cyan
    (0x00, 0x00, 0xC0),  # dark blue
    (0xC0, 0x00, 0xC0),  # dark magenta
]

image = Image.open("runme.png").convert("RGB")
width, height = image.size

extracted = []
last_y = -1
for y in range(height):
    for x in range(width):
        r, g, b = image.getpixel((x, y))
        if (r, g, b) in cmap:
            if y != last_y:
                extracted.append([])
                last_y = y
            extracted[-1].append((r, g, b))

extracted_image = Image.new("RGB", (len(extracted[0]), len(extracted)))
for y, row in enumerate(extracted):
    for x, color in enumerate(row):
        extracted_image.putpixel((x, y), color)

extracted_image.save("extracted.png")

# https://www.dangermouse.net/esoteric/piet.html
# https://gabriellesc.github.io/piet/
# tjctf{p1et_pr1nt3r}
