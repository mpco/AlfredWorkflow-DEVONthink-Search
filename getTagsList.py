#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import json

selectedDbUUID = os.getenv('selectedDbUUID', "")

# todo: if not selectedDbUUID，显示所有 tags
# 多个 tag 匹配

dtTagsFilePath = os.path.expanduser(
    "~/Library/Caches/Metadata/DEVONthink Pro 2/Lookup/{}.dtTags".format(selectedDbUUID))

result = {"items": []}
if dtTagsFilePath[-6:] == "dtTags":
    with open(dtTagsFilePath, 'rb') as f:
        r = f.read()
    rList = r.split("DTstTAGS")

    for tagStr in rList[1:]:
        tag = tagStr[8:]
        result["items"].append({
            "title": tag,
            "subtitle": "Enter to list all files with this tag",
            # "arg": tag,
            "variables": {"selectedTag": tag}
        })

sys.stdout.write(json.dumps(result))
