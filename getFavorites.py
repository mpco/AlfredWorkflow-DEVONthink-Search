#!/usr/bin/python
# -*- coding: UTF-8 -*-

import plistlib
import os
import json

filePath = os.path.expanduser("~/Library/Application Support/DEVONthink 3/Favorites.plist")

if os.path.exists(filePath):
    result = {"items": []}
    plObjList = plistlib.readPlist(filePath)
    for plobj in plObjList:
        if "UUID" in plobj:
            result["items"].append({
                "title": plobj["Name"],
                # "subtitle": "",
                "arg": plobj["UUID"]})
        else:
            pass
            # when favourite item is a db, plobj has keys: alias, date, path
            # alias can be read by 'plobj["Alias"].data'
    print(json.dumps(result))
else:
    print('{"items": [{"title": "No Favorite Item","subtitle": "(*´･д･)?"}]}')
