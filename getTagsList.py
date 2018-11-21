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


if not os.path.exists(dtTagsFilePath):
    sys.stdout.write(json.dumps({"items": [{"title": "Tags File for this database not exists"}]}))
    sys.exit()

result = {"items": []}
if dtTagsFilePath[-6:] == "dtTags":
    with open(dtTagsFilePath, 'rb') as f:
        r = f.read()
    if not r:
        sys.stdout.write(json.dumps({"items": [{"title": "No tag in the database"}]}))
        sys.exit()

    rList = r.split("DTstTAGS")

    for tagStr in rList[1:]:
        tag = tagStr[8:]
        result["items"].append({
            "title": tag,
            "subtitle": "Enter to list all files with this tag",
            # "arg": tag,
            "variables": {"selectedTag": tag, "selectedDbUUID": selectedDbUUID}
        })

sys.stdout.write(json.dumps(result))
