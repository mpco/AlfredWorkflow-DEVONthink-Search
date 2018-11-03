#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

metaFilePath = sys.argv[1]
if metaFilePath[-4:] in [".dt2", "dtp2"]:
    with open(metaFilePath, 'rb') as f:
        r = f.read()
    rList = r.split("DTst")

    # 各个标签信息的位置会随着被索引文件的类型不同而变化
    for labelStr in rList:
        if labelStr[:4] == "FILE":
            path = labelStr[12:]
            break
    print(path)
