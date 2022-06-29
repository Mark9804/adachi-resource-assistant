from PIL import Image, ImageFilter
import subprocess
import os
import sys
from platform import system
import yaml

__all__ = ["rootdir", "readConfig", "png2Webp", "exploreDir", "findImages", "fillImage"]

rootdir = os.path.dirname(os.path.realpath(__file__))


def readConfig(path):
    try:
        with open(path, "r") as f:
            return yaml.full_load(f)
    except:
        raise


def png2Webp(path):
    basename, filename, dirname = (
        os.path.splitext(path)[0],
        os.path.basename(path),
        os.path.dirname(path),
    )
    target = "{}.webp".format(basename)
    targetPath = os.path.join(dirname, target)

    try:
        Image.open(path).filter(ImageFilter.GaussianBlur(radius=0.05)).save(targetPath, "webp", quality=95)
        os.remove(path)
        print("转换：{}".format(targetPath))
    except:
        print("转换失败：{}".format(targetPath), file=sys.stderr)


def exploreDir(path):
    osName = system()

    if "Windows" == osName:
        cmdline = "explorer '{}'".format(path)
    elif "Darwin" == osName:
        cmdline = "open {}".format(path)
    elif "Linux" == osName:
        cmdline = "xdg-open '{}'".format(path) if "DISPLAY" in os.environ else "ls -lh '{}'".format(path)
    else:
        raise Exception("无法在 {} 系统上打开文件浏览器".format(osName))

    try:
        process = subprocess.Popen(cmdline, shell=True)
    except:
        raise

    return process


def findImages(workdir, extension=".png"):
    images = []

    for root, _, files in os.walk(workdir, topdown=True):
        for file in files:
            if file.endswith(extension):
                images.append(os.path.join(root, file))

    return images


def fillImageWithBlank(image, size=[256, 256], square=False):
    try:
        width, height = [max(image.size) for _ in range(2)] if square else size
        pos = int((width - image.size[0]) / 2), int((height - image.size[1]) / 2 if square else 1)
        imageNew = Image.new("RGBA", (width, height), (255, 255, 255, 0))
        imageNew.paste(image.copy(), pos)
    except:
        raise

    return imageNew


def fillImage(path):
    standards = [(320, 1024), (256, 256)]

    try:
        image = Image.open(path)
    except Exception as e:
        print("错误：{}".format(e))
        return

    imageRatio = image.size[1] / image.size[0]
    basename = os.path.splitext(path)[0]

    if image.size in standards:
        print("跳过：{}".format(path))
        return

    try:
        os.rename(path, "{}_backup.png".format(basename))

        # 由宽高比例综合宽度信息，判断图像的用途，
        # 内鬼网裁剪时不会改变宽度，只会改变高度，
        # gacha splash art 例外，该图片的原始尺寸为 2048 × 1024
        if 320 in image.size and imageRatio > 1.5:
            fillImageWithBlank(image, standards[0]).save(path)
        elif 256 in image.size:
            fillImageWithBlank(image, standards[1]).save(path)
        else:
            fillImageWithBlank(image, square=True).save(path)

        print("填充：{}".format(path))
    except:
        print("填充失败：{}".format(e), file=sys.stderr)
