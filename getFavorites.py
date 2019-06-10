#!/usr/bin/python
# -*- coding: UTF-8 -*-

import plistlib
import os
import json

filePath = os.path.expanduser("~/Library/Application Support/DEVONthink Pro 2/Favorites.plist")

if os.path.exists(filePath):
    result = {"items": []}
    plObjList = plistlib.readPlist(filePath)
    for plobj in plObjList:
        result["items"].append({
            "title": plobj["Name"],
            # "subtitle": "",
            "arg": plobj["UUID"]})
    print(json.dumps(result))
else:
    print('{"items": [{"title": "No Favorite Item","subtitle": "(*´･д･)?"}]}')
