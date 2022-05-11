#!/usr/bin/env python3

import sys
import signal
import requests
import os
from api import rootdir, readConfig, png2Webp, exploreDir

outdir = os.path.join(rootdir, "resources_custom", "Version2", "wish", "character")


def getPng(name, short):
    headers = {"user-agent": "curl/7.83.0"}
    url = "https://genshin.honeyhunterworld.com/img/char/{}_gacha_card.png".format(short)
    target = os.path.join(outdir, "{}.png".format(name))

    try:
        with open(target, "wb") as f:
            f.write(requests.get(url, headers=headers).content)

        print("获取：{}".format(url))
    except:
        print("获取失败：{}".format(url), file=sys.stderr)

    return target


def quit(errcode=0):
    sys.exit(errcode)


if "__main__" == __name__:
    names = readConfig(os.path.join(rootdir, "names.yml"))
    argc = len(sys.argv)

    if not os.path.exists(outdir):
        try:
            os.makedirs(outdir)
        except Exception as e:
            print("错误：{}".format(e), file=sys.stderr)
            quit(-1)

    if argc > 2:
        png2Webp(getPng(*sys.argv[1:3]))
    elif 1 == argc:
        for name, short in dict.items(names["characters"]):
            png2Webp(getPng(name, short))
    else:
        # XXX print usage ?
        print("参数错误", file=sys.stderr)
        quit(-1)

    try:
        exploreDir(outdir).wait()
    except Exception as e:
        print("非致命错误：{}".format(e), file=sys.stderr)
