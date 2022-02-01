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


def fill_with_blank(original, originalSize, width, height):
    newImage = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    pastebin = original.copy()
    pastePosition = (width - originalSize[0], height - originalSize[1])
    newImage.paste(pastebin, pastePosition)

    return newImage


def fill_image(imagePath):
    standards = [(320, 1024), (256, 256)]
    image = Image.open(imagePath)
    imageSize = image.size
    imageRatio = imageSize[1] / imageSize[0]
    if imageSize in standards:
        print(imagePath + " 不需要处理")
    else:
        print(imagePath + " 处理中")
        basename = os.path.splitext(imagePath)

        # 内鬼网裁剪时不会改变宽度，只会改变高度（gacha splash art例外，该图片的原始尺寸为 2048 × 1024）
        # 由宽高比例综合宽度信息，判断图像的用途
        if 320 in imageSize and imageRatio > 1.5:
            newImage = fill_with_blank(image, imageSize, 320, 1024)
        elif 256 in imageSize and imageRatio < 1:
            newImage = fill_with_blank(image, imageSize, 256, 256)
        else:
            print("将 " + imagePath + " 填充至 1:1")
            fillSize = max(imageSize)
            newImage = fill_with_blank(image, imageSize, fillSize, fillSize)

        os.rename(imagePath, basename[0] + "_backup.png")
        # noinspection PyUnboundLocalVariable
        newImage.save(imagePath)


if __name__ == "__main__":
    working_dir = os.path.dirname(__file__)

    images = sys.argv[1:] if len(sys.argv) >= 2 else find_images()

    for img in images:
        fill_image(img)

    globals().pop("img", None)
