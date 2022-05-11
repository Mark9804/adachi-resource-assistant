# adachi-resource-assistant

## 准备

```shell
git clone https://github.com/Mark9804/adachi-resource-assistant.git
cd ./adachi-resource-assistant/
python3 -m venv ./.venv/
source ./.venv/bin/activate
pip3 install -r ./requirements.txt
```

## 使用

## 生成角色卡池图片

根据角色信息或者配置文件生成角色卡池图片。

```shell
python3 ./get_gacha_image.py 刻晴 keqing
python3 ./get_gacha_image.py
```

第二个参数来源于 [Honey Impact](https://genshin.honeyhunterworld.com/?lang=CN) 的角色页面链接，如 `https://genshin.honeyhunterworld.com/db/char/keqing/?lang=CHS` 中的 `keqing` 。不给出参数时，则从 [names.yml](names.yml) 当中获取所有可用的角色。

## 填充素材图片

根据素材图片自身信息进行填充。

```shell
python3 ./fill_image.py /path/to/image.png
python3 ./fill_image.py /path/*.png
python3 ./fill_image.py
```

参数列表为文件列表，不给出参数时，则递归扫描当前目录中的所有 `.png` 文件。

## 许可

[MIT License](LICENSE) 。
