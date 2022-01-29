from PIL import Image
import os
import sys


def find_images():
    pendingImages = []
    for root, dirs, files in os.walk(working_dir, topdown=True):
        for file in files:
            if file.endswith(".png"):
                pendingImages.append(os.path.join(root, file))

    return pendingImages


def fill_image(imagePath):
    image = Image.open(imagePath)
    imageSize = image.size
    if imageSize == (320, 1024):
        print(imagePath + " 不需要处理")
    else:
        print(imagePath + " 处理中")
        basename = os.path.splitext(imagePath)  # (path_til_basename, ext)
        newImage = Image.new("RGBA", (320, 1024), (255, 0, 0, 0))
        pastebin = image.copy()
        pastePosition = (
            newImage.size[0] - imageSize[0], newImage.size[1] - imageSize[1])
        newImage.paste(pastebin, pastePosition)
        os.rename(imagePath, basename[0] + "_backup.png")
        newImage.save(imagePath, quality=95)


if __name__ == "__main__":
    working_dir = os.path.dirname(__file__)

    images = sys.argv[1:] if len(sys.argv) >= 2 else find_images()

    for img in images:
        fill_image(img)

    globals().pop("img", None)
