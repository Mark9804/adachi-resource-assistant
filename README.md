# adachi-resource-assistant

## 弃用警告（ Deprecation Warning ）

从原神 3.1 版本开始此模块已经弃用，功能已经整合到 [Adachi-BOT](https://github.com/Arondight/Adachi-BOT) ，使用说明详见[《资源文件制作指引》](https://github.com/Arondight/Adachi-BOT/blob/master/docs/%E8%B5%84%E6%BA%90%E6%96%87%E4%BB%B6%E5%88%B6%E4%BD%9C%E6%8C%87%E5%BC%95.md#%E5%85%B6%E4%BB%96%E8%B5%84%E6%BA%90%E6%96%87%E4%BB%B6)

This module has been deprecated since Genshin Impact 3.1 version, and the function has been integrated into [Adachi-BOT](https://github.com/Arondight/Adachi-BOT). For details, please refer to [《资源文件制作指引》](https://github.com/Arondight/Adachi-BOT/blob/master/docs/%E8%B5%84%E6%BA%90%E6%96%87%E4%BB%B6%E5%88%B6%E4%BD%9C%E6%8C%87%E5%BC%95.md#%E5%85%B6%E4%BB%96%E8%B5%84%E6%BA%90%E6%96%87%E4%BB%B6).

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
adachi_resource_get_gacha_image 刻晴 keqing_042
adachi_resource_get_gacha_image
```

第二个参数来源于 [Honey Impact](https://genshin.honeyhunterworld.com/?lang=CN) 的角色页面链接，如 `https://genshin.honeyhunterworld.com/keqing_042/?lang=CHS` 中的 `keqing_042` 。不给出参数则获取所有可用的角色。

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
