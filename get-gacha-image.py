import yaml
import os
import sys
import requests
from PIL import Image, ImageFilter


def read_config(namesPath):
    with open(namesPath, 'r') as settings:
        return yaml.full_load(settings)


def get_png(characterName, imagePrefix):
    fileUrl = "https://genshin.honeyhunterworld.com/img/char/" + imagePrefix + "_gacha_card.png"
    imagePath = os.path.join(save_path, characterName + ".png")
    print(characterName, fileUrl)
    rawBytes = requests.get(fileUrl, headers=headers)
    with open(imagePath, "wb") as f:
        file.write(rawBytes.content)


def png_to_webp(pngPath):
    baseName = os.path.splitext(pngPath)[0]
    fileName = os.path.basename(pngPath)
    print("正在转换 " + fileName + "到webp…")
    savePath = baseName + ".webp"
    image = Image.open(pngPath).filter(ImageFilter.GaussianBlur(radius=0.05))
    image.save(savePath, "webp", quality=95)
    os.remove(pngPath)


if __name__ == "__main__":
    wd = os.path.dirname(__file__)
    names_path = os.path.join(wd, "names.yml")
    names = read_config(names_path)
    save_path = os.path.join(wd, "resources_custom", "Version2", "wish", "character")

    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
    }

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    if len(sys.argv) >= 1:
        get_png(sys.argv[1], sys.argv[2])
    else:
        for name, prefix in dict.items(names["characters"]):
            get_png(name, prefix)

    for root, dirs, files in os.walk(save_path):
        for file in files:
            png_path = os.path.join(root, file)
            if png_path.endswith(".png"):
                png_to_webp(png_path)
