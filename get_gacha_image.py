import sys
import requests
from lib.APIs import *


def get_png(characterName, imagePrefix):
    fileUrl = (
        "https://genshin.honeyhunterworld.com/img/char/"
        + imagePrefix
        + "_gacha_card.png"
    )
    imagePath = os.path.join(save_path, characterName + ".png")
    print("获取：{}".format(fileUrl))
    # FIXME handle exception
    rawBytes = requests.get(fileUrl, headers=headers)
    # FIXME handle exception
    with open(imagePath, "wb") as f:
        f.write(rawBytes.content)
    return imagePath


def get_webp(characterName, imagePrefix):
    png_to_webp(get_png(characterName, imagePrefix))


if __name__ == "__main__":
    wd = os.path.dirname(__file__)
    names_path = os.path.join(wd, "names.yml")
    names = read_config(names_path)
    save_path = os.path.join(wd, "resources_custom", "Version2", "wish", "character")
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
    }
    argc = len(sys.argv)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    if argc > 2:
        get_webp(*sys.argv[1:3])
    elif 1 == argc:
        for name, prefix in dict.items(names["characters"]):
            get_webp(name, prefix)
    else:
        print("参数错误看说明文档")

    try:
        open_in_explorer(save_path).wait()
    except Exception as e:
        print("可以忽略的错误：{}".format(e))
