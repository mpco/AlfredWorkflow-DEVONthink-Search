#!/usr/bin/python
# -*- coding: UTF-8 -*-

# todo: if not selectedDbUUID，显示所有 tags
# 多个 tag 匹配

import os
import json
import ast
import shlex
import subprocess

def runForCertainDB(selectedDbUUID):
    cmdScript = "osascript -e 'tell application \"DEVONthink 3\" to get name of tag group of (get database with uuid \"{}\")' -s s".format(selectedDbUUID)
    cmdList = shlex.split(cmdScript)
    cmdResult = subprocess.check_output(cmdList)
    tagList = ast.literal_eval(
        "[" + cmdResult[1:-2].decode("UTF8") + "]")

    result = []
    for tag in tagList:
        result.append({
            "title": tag,
            "subtitle": "Press Enter to list all files with this tag",
            # "arg": tag,
            "variables": {"selectedTag": tag, "selectedDbUUID": selectedDbUUID}
        })
    return result


selectedDbUUID = os.getenv('selectedDbUUID', "")
result = {"items": []}

if selectedDbUUID == '':
    getAllUUIDs = """'set dbUUIDs to {}
    tell application "DEVONthink 3"
        set allDb to every database
        repeat with theDb in allDb
            set end of dbUUIDs to (get uuid of theDb)
        end repeat
    end tell
    get dbUUIDs'"""
    proc = subprocess.Popen("osascript -e " + getAllUUIDs.strip(),
                            stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    DbUUIDs = out.decode('utf-8').strip().split(', ')
    for db_uuid in DbUUIDs:
        dbresult = runForCertainDB(db_uuid)
        result['items'].extend(dbresult)

else:
    dbresult = runForCertainDB(selectedDbUUID)
    result['items'].extend(dbresult)


if result['items']:
    print(json.dumps(result))
else:
    # when result list is empty
    print('{"items": [{"title": "None Tag","subtitle": "(*´･д･)?"}]}')
