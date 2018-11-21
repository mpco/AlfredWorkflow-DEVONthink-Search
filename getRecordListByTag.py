#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import json
import subprocess

selectedTag = os.getenv('selectedTag', "")

getInfoAS = """
'tell application "DEVONthink Pro"
    set theList to lookup records with tags {"%s"} with any
    set theResult to ""
    repeat with theItem in theList
        set theName to name of theItem
        set theUUID to uuid of theItem
        set thePath to path of theItem
        set theInfo to theName & "||" & theUUID & "||" & thePath
        set theResult to theResult & "!@#!@#" & theInfo
    end repeat
end tell'
""" % selectedTag
result = {"items": []}

proc = subprocess.Popen("osascript -e " + getInfoAS.strip(),
                        stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()

infoList = out.split("!@#!@#")[1:]
# print(infoList)

for itemInfoStr in infoList:
    itemInfoList = itemInfoStr.split("||")
    itemName = itemInfoList[0]
    itemUUID = itemInfoList[1]
    itemPath = itemInfoList[2]
    result["items"].append({
        "title": itemName,
        "subtitle": "Open with DEVONthink",
        "arg": itemUUID,
        "mods": {
            "cmd": {"valid": True, "arg": itemPath, "subtitle": "Open with External Editor"},
            "alt": {"valid": True, "arg": itemUUID, "subtitle": "Reveal in DEVONthink"}
        }
    })

print(json.dumps(result))
