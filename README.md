# adachi-resource-assistant

## Start

```shell
git clone https://github.com/Mark9804/adachi-resource-assistant.git
cd ./adachi-resource-assistant/
python3 -m venv ./.venv/
source ./.venv/bin/activate
pip3 install -r ./requirements.txt
```

## Usage

## 抓取角色图片

```shell
python3 ./get_gacha_image.py 刻晴 keqing
python3 ./get_gacha_image.py
```

第二个参数来源于[内鬼网](https://genshin.honeyhunterworld.com/?lang=CHS)的人物页面链接，例如 `https://genshin.honeyhunterworld.com/db/char/keqing/?lang=CHS` 中的 `keqing` 。不给出参数时，则从 `names.yml` 当中获取所有可用的角色。

## 切图

```shell
python3 ./fill_image.py /path/to/image.png
python3 ./fill_image.py
```

不给出参数时，则递归扫描当前目录。
