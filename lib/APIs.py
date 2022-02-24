from PIL import Image, ImageFilter
import subprocess
import os
from platform import system
import yaml


def read_config(namesPath):
    with open(namesPath, 'r') as settings:
        return yaml.full_load(settings)


def png_to_webp(pngPath):
    baseName = os.path.splitext(pngPath)[0]
    fileName = os.path.basename(pngPath)
    print("正在转换 " + fileName + "到webp…")
    savePath = baseName + ".webp"
    image = Image.open(pngPath).filter(ImageFilter.GaussianBlur(radius=0.05))
    image.save(savePath, "webp", quality=95)
    os.remove(pngPath)


def open_in_explorer(path):
    userSystem = system()
    if userSystem == 'Windows':
        subprocess.Popen('explorer "' + path + '"', shell=False)
    elif userSystem == 'Darwin':
        subprocess.Popen(["open", path])
    elif userSystem == 'Linux':
        # noinspection PyBroadException
        try:
            subprocess.Popen('nautilus "' + path + '"', shell=False)
        except:
            pass


def find_images(workingDir, extension=".png"):
    pendingImages = []
    for root, dirs, files in os.walk(workingDir, topdown=True):
        for file in files:
            if file.endswith(extension):
                pendingImages.append(os.path.join(root, file))

    return pendingImages


def fill_with_blank(original, originalSize, width, height, fillType="normal"):
    newImage = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    pastebin = original.copy()
    pastePosition = (int((width - originalSize[0]) / 2), height - originalSize[1]) if fillType == "normal" else (
        int((width - originalSize[0]) / 2), int((height - originalSize[1]) / 2))
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
        elif 256 in imageSize:
            newImage = fill_with_blank(image, imageSize, 256, 256)
        else:
            print("将 " + imagePath + " 填充至 1:1")
            fillSize = max(imageSize)
            newImage = fill_with_blank(image, imageSize, fillSize, fillSize, fillType="fit-square")

        os.rename(imagePath, basename[0] + "_backup.png")
        # noinspection PyUnboundLocalVariable
        newImage.save(imagePath)
