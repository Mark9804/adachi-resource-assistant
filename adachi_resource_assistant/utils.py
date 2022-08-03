import subprocess
import os
import sys
from subprocess import Popen
from typing import Union
from PIL import Image, ImageFilter
from platform import system

__all__ = ["exploreDir", "findImages", "fillImage", "png2Webp"]


def png2Webp(path: str) -> None:
    """
    :param path: png 文件路径
    :return: None
    """
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
    except Exception:
        print("转换失败：{}".format(targetPath), file=sys.stderr)


def exploreDir(path: str) -> object:
    """
    :param path: 目录路径
    :return: 用于浏览目录的进程
    """
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
    except Exception:
        raise

    return process


def findImages(workdir: str, extension: str = ".png") -> list:
    """
    :param workdir: 寻找图片文件的工作目录
    :param extension: 后缀名
    :return: 图片文件列表
    """
    images = []

    for root, _, files in os.walk(workdir, topdown=True):
        for file in files:
            if file.endswith(extension):
                images.append(os.path.join(root, file))

    return images


def fillImageWithBlank(image: object, size=[256, 256], square: bool = False) -> object:
    """
    :param image: Image 对象
    :param size: 长宽像素
    :param square: 是正方形
    :return: Image 对象
    """
    try:
        width, height = [max(image.size) for _ in range(2)] if square else size
        pos = int((width - image.size[0]) / 2), int((height - image.size[1]) / 2 if square else 1)
        imageNew = Image.new("RGBA", (width, height), (255, 255, 255, 0))
        imageNew.paste(image.copy(), pos)
    except Exception:
        raise

    return imageNew


def fillImage(path: str) -> None:
    """
    :param path: 图片路径
    :return: None
    """
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
    except Exception as e:
        print("填充失败：{}".format(e), file=sys.stderr)
