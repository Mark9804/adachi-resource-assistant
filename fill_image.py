import sys
from lib.APIs import *

if __name__ == "__main__":
    working_dir = os.path.dirname(__file__)

    images = sys.argv[1:] if len(sys.argv) >= 2 else find_images(working_dir, extension=".png")

    for img in images:
        fill_image(img)

    globals().pop("img", None)
