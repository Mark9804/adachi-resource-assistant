#!/usr/bin/env python3

import sys
from utils import rootdir, findImages, fillImage

if "__main__" == __name__:
    argc = len(sys.argv)
    images = sys.argv[1:] if argc > 1 else findImages(rootdir, extension=".png")

    for image in images:
        fillImage(image)
