'use strict';

function run(argv) {
    // read environment variables
    ObjC.import('stdlib')
    let env = $.NSProcessInfo.processInfo.environment;
    env = ObjC.unwrap(env)

    let selectedDbUUID
    let filterOutGroup

    if ("selectedDbUUID" in env) { selectedDbUUID = $.getenv('selectedDbUUID') }
    if ("filterOutGroup" in env) { filterOutGroup = $.getenv('filterOutGroup').toLowerCase() }
    if ("ignoredDbUuidList" in env) {
        let ignoredDbUuidList = [];
        let tempList = $.getenv('ignoredDbUuidList').split(",");
        for (let i = 0; i < tempList.length; i++) {
            ignoredDbUuidList.push(tempList[i].replace(/^\s+|\s+$/g, ''))
        }
    }

    let DNt = Application("DEVONthink 3");
    let allDB = DNt.databases

    // if selectedDbUUID exists, only search in selected db.
    if (typeof selectedDbUUID !== 'undefined') {
        allDB = { "0": DNt.getDatabaseWithUuid(selectedDbUUID) }
    }
    let allResult = []


    for (let dbIndex in allDB) {
        let theDbUUID = allDB[dbIndex].uuid()


        // if selectedDbUUID not exists and theDbUUID in ignoredDbUuidList, ignore the db
        if ((typeof selectedDbUUID == 'undefined') && (typeof ignoredDbUuidList !== 'undefined') && ignoredDbUuidList.includes(theDbUUID)) {
            continue
        }

        let smartGroupList = allDB[dbIndex].smartGroups()
        for (let sgIndex in smartGroupList) {
            let item = {
                title: smartGroupList[sgIndex].name(),
                subtitle: allDB[dbIndex].name(),
                arg: smartGroupList[sgIndex].uuid()
            }
            allResult.push(item)
        }
    }

    if (allResult.length == 0) {
        return JSON.stringify({ "items": [{ "title": "No SmartGroup..." }] });
    }

    return JSON.stringify({ "items": allResult });
}