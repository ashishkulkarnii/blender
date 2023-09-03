"""Convert all PNG files in a folder passed to this program into a single GIF file, sorted by filename."""
from PIL import Image
import os
import sys

if len(sys.argv) < 2:
    print("Usage: python png_to_gif.py <folder>")
    sys.exit(1)

folder = sys.argv[1]

files = os.listdir(folder)
files.sort()

images = []
for file in files:
    if file.endswith(".png"):
        images.append(Image.open(os.path.join(folder, file)))

images[0].save(os.path.join(folder, "out.gif"), save_all=True, append_images=images[1:], duration=100, loop=0)
