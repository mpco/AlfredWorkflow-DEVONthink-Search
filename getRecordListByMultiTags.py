#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import os
import json
import sys
import subprocess

tagList = sys.argv[1].split(",")
tagList = [tagStr.strip() for tagStr in tagList]

getInfoAS = """
'tell application "DEVONthink Pro"
    set theList to lookup records with tags {"%s"}
    set theResult to ""
    repeat with theItem in theList
        set theName to name of theItem
        set theUUID to uuid of theItem
        set thePath to path of theItem
        set theInfo to theName & "||" & theUUID & "||" & thePath
        set theResult to theResult & "!@#!@#" & theInfo
    end repeat
end tell'
""" % "\",\"".join(tagList)
result = {"items": []}

proc = subprocess.Popen("osascript -e " + getInfoAS.strip(),
                        stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()

if not out:
    print(json.dumps({"items": [{"title": "No record with the tags"}]}))
    sys.exit()

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
        "icon": {"type": "fileicon", "path": itemPath},
        "mods": {
            "cmd": {"valid": True, "arg": itemPath, "subtitle": "Open with External Editor"},
            "alt": {"valid": True, "arg": itemUUID, "subtitle": "Reveal in DEVONthink"}
        }
    })

print(json.dumps(result))
