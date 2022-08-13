from adachi_resource_assistant.names import characters
from adachi_resource_assistant.utils import exploreDir, findImages, fillImage, png2Webp

__version__ = "3.0"
__all__ = ["fillImage", "getGachaImage"]


def fillImage():
    import os
    import sys

    argc = len(sys.argv)
    images = sys.argv[1:] if argc > 1 else findImages(os.getcwd(), extension=".png")

    for image in images:
        fillImage(image)


def getGachaImage():
    import os
    import sys
    import requests

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
