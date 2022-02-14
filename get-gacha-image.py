import yaml
import os
import urllib.request
import requests


def read_config(namesPath):
    with open(namesPath, 'r') as settings:
        return yaml.full_load(settings)


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

    for name, prefix in dict.items(names["characters"]):
        file_url = "https://genshin.honeyhunterworld.com/img/char/" + prefix + "_gacha_card.png"
        print(name, file_url)
        image_path = os.path.join(save_path, name + ".png")
        raw_bytes = requests.get(file_url, headers=headers)
        with open(image_path, "wb") as file:
            file.write(raw_bytes.content)
