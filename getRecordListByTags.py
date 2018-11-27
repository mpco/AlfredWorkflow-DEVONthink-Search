#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import os
import json
import os
import sys
import subprocess

if sys.argv[1] == "inputTags":
    if not sys.argv[2].strip():
        sys.exit()
    tagList = sys.argv[2].split(",")
    tagList = [tagItem.strip() for tagItem in tagList]
    tagStr = "\",\"".join(tagList)
    ignoredDbUuidList = os.getenv('ignoredDbUuidList', "").split(",")
    ignoredDbUuidList = [dbUuid.strip() for dbUuid in ignoredDbUuidList]
    ignoredDbUuidListStr = "\",\"".join(ignoredDbUuidList)
    getInfoAppleScript = """'tell application "DEVONthink Pro"
    set allDb to every database
    set allResult to ""
    set ignoredDbUuidList to {"%s"}
    set newAllDb to {}
    repeat with theDb in allDb
        if ignoredDbUuidList does not contain (get uuid of theDb) then
            copy theDb to end of newAllDb
        end if
    end repeat
    repeat with theDb in newAllDb
        set theList to lookup records with tags {"%s"} in theDb
        set theResult to ""
        repeat with theItem in theList
            set theName to name of theItem
            set theUUID to uuid of theItem
            set thePath to path of theItem
            set theTagList to tags of theItem
            set saveTID to text item delimiters of AppleScript
            set text item delimiters of AppleScript to ",,,"
            set theTags to theTagList as text
            set text item delimiters of AppleScript to saveTID
            set theDbName to (name of database of theItem)
            set theDbLocation to location of theItem
            set theInfo to theName & "||" & theUUID & "||" & thePath & "||" & theTags & "||" & theDbName & "||" & theDbLocation
            set theResult to theResult & "!@#!@#" & theInfo
        end repeat
        set allResult to allResult & theResult
    end repeat
end tell'""" % (ignoredDbUuidListStr, tagStr)
elif sys.argv[1] == "selectedTag":
    selectedTag = os.getenv('selectedTag', "")
    tagStr = selectedTag
    selectedDbUuid = os.getenv('selectedDbUUID', "")
    getInfoAppleScript = """'tell application "DEVONthink Pro"
    set theDB to (get database with uuid "%s")
    set theList to lookup records with tags {"%s"} in theDB
    set theResult to ""
    repeat with theItem in theList
        set theName to name of theItem
        set theUUID to uuid of theItem
        set thePath to path of theItem
        set theTagList to tags of theItem
        set saveTID to text item delimiters of AppleScript
        set text item delimiters of AppleScript to ",,,"
        set theTags to theTagList as text
        set text item delimiters of AppleScript to saveTID
        set theDbName to (name of database of theItem)
        set theDbLocation to location of theItem
        set theInfo to theName & "||" & theUUID & "||" & thePath & "||" & theTags & "||" & theDbName & "||" & theDbLocation
        set theResult to theResult & "!@#!@#" & theInfo
    end repeat
end tell'""" % (selectedDbUuid, tagStr)
else:
    sys.exit(1)

result = {"items": []}

proc = subprocess.Popen("osascript -e " + getInfoAppleScript.strip(),
                        stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()

if not out:
    print(json.dumps({"items": [{"title": "No record with the tags"}]}))
    sys.exit()

# print(out)

infoList = out.strip().split("!@#!@#")[1:]

for itemInfoStr in infoList:
    itemInfoList = itemInfoStr.split("||")
    itemName = itemInfoList[0]
    itemUUID = itemInfoList[1]
    itemPath = itemInfoList[2]
    itemTagListStr = itemInfoList[3]
    itemTagList = itemTagListStr.split(",,,")
    itemDbName = itemInfoList[4]
    itemDbLocation = itemInfoList[5]
    if len(itemDbLocation) > 1:
        # remove the last /
        itemDbLocation = itemDbLocation[:-1].replace("/", " > ")
    else:
        itemDbLocation = ""
    result["items"].append({
        "title": itemName,
        "subtitle": "📂 " + itemDbName + " " + itemDbLocation,
        "arg": itemUUID,
        "icon": {"type": "fileicon", "path": itemPath},
        "mods": {
            "cmd": {"valid": True, "arg": itemPath, "subtitle": "🏷 " + ", ".join(itemTagList)},
            "alt": {"valid": True, "arg": itemUUID, "subtitle": "Reveal in DEVONthink"}
        }
    })

print(json.dumps(result))
