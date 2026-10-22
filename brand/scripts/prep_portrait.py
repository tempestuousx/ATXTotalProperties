"""Remove the sports-team logo from the cap and crop the portrait for the badge."""
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

src = Image.open("source/brandon-illustration.png").convert("RGB")
a = np.asarray(src).astype(float)
H, W, _ = a.shape

# Tight outline around the old cap logo, kept inside the cap's front panel.
LOGO = [(282, 288), (300, 276), (330, 272), (345, 272), (380, 274), (398, 280), (405, 300),
        (403, 330), (393, 349), (340, 350), (290, 349), (271, 335), (265, 310)]
mask = Image.new("L", (W, H), 0)
ImageDraw.Draw(mask).polygon(LOGO, fill=255)
m = np.asarray(mask) > 0

# Learn the cap's shading from clean cap pixels around the logo (plane fit per color).
ring = np.asarray(mask.filter(ImageFilter.MaxFilter(31))) > 0
ring &= ~(np.asarray(mask.filter(ImageFilter.MaxFilter(5))) > 0)
s = a.sum(axis=2)
capish = ring & (s > 270) & (s < 470) & (np.abs(a[..., 0] - a[..., 2]) < 25)
ys, xs = np.nonzero(capish)
X = np.c_[xs, ys, np.ones_like(xs)]
coef = [np.linalg.lstsq(X, a[ys, xs, c], rcond=None)[0] for c in range(3)]

rng = np.random.default_rng(7)
my, mx = np.nonzero(m)
fill = a.copy()
for c in range(3):
    fill[my, mx, c] = coef[c][0] * mx + coef[c][1] * my + coef[c][2] + rng.normal(0, 2.5, len(mx))
fill_im = Image.fromarray(np.clip(fill, 0, 255).astype("uint8")).filter(ImageFilter.GaussianBlur(0.8))

# Feather the edge so the patch blends in.
soft = mask.filter(ImageFilter.GaussianBlur(2))
im = Image.composite(fill_im, src, soft)
im.save("source/brandon-clean.png")

# Square crop centered on the face, head and shoulders.
im.crop((8, 236, 648, 876)).save("source/brandon-square.png")
