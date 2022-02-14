## get-gacha-image.py

```shell
python3 get-gacha-image.py [角色中文名 角色标识名] …
```

角色标识名即内鬼网网址上的角色名称，例如 ht<span>tps://genshin</span>.honeyhunterworld.com/db/char/<ins>**qiqi**</ins>/?lang=CHS

当没有输入时，会从 `names.yml` 当中获取所有可用的链接

## fill_image.py

```shell
python3 fill_image.py -/path/to/image1.png -path/to/image2.png …
```

如果不传入任何参数，则默认扫描当前文件夹下的所有文件（包含子文件夹）
