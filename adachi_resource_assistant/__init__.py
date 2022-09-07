from adachi_resource_assistant.names import characters
from adachi_resource_assistant.utils import exploreDir, findImages, fillImageFile, png2Webp

__version__ = "3.0.2"
__all__ = ["fillImageFile", "getGachaImage"]


def deprecationWarnings():
    import warnings
    from functools import partial

    text = (
        "弃用警告（ Deprecation Warning ）\n"
        "弃用：\n"
        "弃用：从原神 3.1 版本开始此模块已经弃用，功能已经整合到 Adachi-BOT ，使用说明详见《资源文件制作指引》。\n"
        "弃用：\n"
        "弃用：This module has been deprecated since Genshin Impact 3.1 version, and the function has been integrated into Adachi-BOT. For details, please refer to《资源文件制作指引》.\n"
        "弃用：\n"
        "弃用：Adachi-BOT ：          https://github.com/Arondight/Adachi-BOT\n"
        "弃用：《资源文件制作指引》： https://github.com/Arondight/Adachi-BOT/blob/master/docs/%E8%B5%84%E6%BA%90%E6%96%87%E4%BB%B6%E5%88%B6%E4%BD%9C%E6%8C%87%E5%BC%95.md#%E5%85%B6%E4%BB%96%E8%B5%84%E6%BA%90%E6%96%87%E4%BB%B6\n"
        "弃用：\n"
    )

    warnings.simplefilter("default")
    warnings.warn(text, DeprecationWarning)


def fillImage():
    import os
    import sys

    deprecationWarnings()

    argc = len(sys.argv)
    images = sys.argv[1:] if argc > 1 else findImages(os.getcwd(), extension=".png")

    for image in images:
        fillImageFile(image)


def getGachaImage():
    import os
    import sys
    import requests

    deprecationWarnings()

    outdir = os.path.join(os.getcwd(), "resources_custom", "Version2", "wish", "character")

    def getPng(name: str, short: str) -> str:
        headers = {"user-agent": "curl/7.83.0"}
        url = "https://genshin.honeyhunterworld.com/img/{}_gacha_card.png".format(short)
        target = os.path.join(outdir, "{}.png".format(name))

        try:
            with open(target, "wb") as f:
                f.write(requests.get(url, headers=headers).content)

            print("获取：{}".format(url))
        except Exception:
            print("获取失败：{}".format(url), file=sys.stderr)

        return target

    def bye(errcode: int = 0) -> None:
        sys.exit(errcode)

    argc = len(sys.argv)

    if not os.path.exists(outdir):
        try:
            os.makedirs(outdir)
        except Exception as e:
            print("错误：{}".format(e), file=sys.stderr)
            bye(-1)

    if argc > 2:
        png2Webp(getPng(*sys.argv[1:3]))
    elif 1 == argc:
        for name, short in dict.items(characters):
            png2Webp(getPng(name, short))
    else:
        # XXX print usage ?
        print("参数错误", file=sys.stderr)
        bye(-1)

    try:
        exploreDir(outdir).wait()
    except Exception as e:
        print("非致命错误：{}".format(e), file=sys.stderr)
