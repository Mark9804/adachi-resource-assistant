# adachi-resource-assistant

## 说明

A resource assistant for [Adachi-BOT](https://github.com/Arondight/Adachi-BOT).

## 安装

```shell
pip3 install -U adachi_resource_assistant
```

## 使用

### 生成角色卡池图片

根据角色信息或者配置文件生成角色卡池图片。

```shell
adachi_resource_get_gacha_image 刻晴 keqing
adachi_resource_get_gacha_image
```

第二个参数来源于 [Honey Impact](https://genshin.honeyhunterworld.com/?lang=CN) 的角色页面链接，如 `https://genshin.honeyhunterworld.com/db/char/keqing/?lang=CHS` 中的 `keqing` 。不给出参数则获取所有可用的角色。

### 填充素材图片

根据素材图片自身信息进行填充。

```shell
adachi_resource_fill_image /path/to/image.png
adachi_resource_fill_image /path/*.png
adachi_resource_fill_image
```

参数列表为文件列表，不给出参数时，则递归扫描当前目录中的所有 `.png` 文件。

## 许可

[MIT License](https://github.com/Mark9804/adachi-resource-assistant/blob/main/LICENSE) 。
