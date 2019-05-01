#!/usr/bin/python
# -*- coding: UTF-8 -*-
import ast
import json
import shlex
import subprocess

cmdScript = "osascript -e 'tell application \"DEVONthink 3\" to get workspaces' -s s"
cmdList = shlex.split(cmdScript)
cmdResult = subprocess.check_output(cmdList)
workspaceList = ast.literal_eval(
    "[" + cmdResult[1:-2].decode("UTF8") + "]")

result = {"items": []}
for item in workspaceList:
    temp = {
        "title": item,
        "subtitle": "",
        "arg": item
    }
    result['items'].append(temp)

if result['items']:
    print(json.dumps(result))
else:
    # when result list is empty
    print('{"items": [{"title": "None Workspace","subtitle": "(*´･д･)?"}]}')
