"""Remove the sports-team logo from the cap and crop the portrait for the badge."""
import random
from PIL import Image, ImageFilter

src = Image.open("source/brandon-illustration.png").convert("RGB")
im = src.copy()
px = im.load()
random.seed(7)

# Fill the cap logo area row by row, blending between clean cap pixels on each side.
X0, X1, Y0, Y1 = 268, 404, 274, 350
for y in range(Y0, Y1):
    left = [sum(c) / 3 for c in (px[X0 - 6, y], px[X0 - 4, y], px[X0 - 2, y])]
    right = [sum(c) / 3 for c in (px[X1 + 2, y], px[X1 + 4, y], px[X1 + 6, y])]
    lc = sorted([px[X0 - k, y] for k in (2, 4, 6, 8)], key=sum)[2]
    rc = sorted([px[X1 + k, y] for k in (2, 4, 6, 8)], key=sum)[2]
    for x in range(X0, X1):
        t = (x - X0) / (X1 - X0)
        n = random.randint(-4, 4)
        px[x, y] = tuple(int(lc[i] * (1 - t) + rc[i] * t + n) for i in range(3))

# Soften the patch edges so it blends in.
patch = im.crop((X0 - 4, Y0 - 2, X1 + 4, Y1 + 2)).filter(ImageFilter.GaussianBlur(1.6))
im.paste(patch, (X0 - 4, Y0 - 2))
im.save("source/brandon-clean.png")

# Square crop centered on the face, head and shoulders.
im.crop((8, 236, 648, 876)).save("source/brandon-square.png")
