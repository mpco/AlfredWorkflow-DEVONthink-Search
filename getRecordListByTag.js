'use strict';
function run(argv) {
    // read environment variables
    ObjC.import('stdlib')
    var env = $.NSProcessInfo.processInfo.environment;
    env = ObjC.unwrap(env)
    if ("selectedTag" in env) { var selectedTag = $.getenv('selectedTag') }
    if ("selectedDbUUID" in env) { var selectedDbUUID = $.getenv('selectedDbUUID') }
    if ("ignoredDbUuidList" in env) {
        var ignoredDbUuidList = [];
        var tempList = $.getenv('ignoredDbUuidList').split(",");
        for (var i = 0; i < tempList.length; i++) {
            ignoredDbUuidList.push(tempList[i].replace(/^\s+|\s+$/g, ''))
        }
    }

    // list all env var
    // for (var key in env) {
    //     console.log(key + " : " + ObjC.unwrap(env[key]))
    // }

    // get $query, strip space, convert '你abc我他' to '~你abc~我他'
    const cjkRegex = /(\p{Unified_Ideograph}+)/ug
    const query = argv[0].replace(/^\s+|\s+$/g, '').replace(cjkRegex, "~$1");
    var DNt = Application("DEVONthink Pro");
    var allDB = DNt.databases
    // if selectedTag exists, only search in selected db.
    if (typeof selectedTag !== 'undefined') {
        allDB = { "0": DNt.getDatabaseWithUuid(selectedTag) }
    }
    var allResult = []
    for (var db in allDB) {
        var theDbUUID = allDB[db].uuid()

        // if selectedTag not exists and theDbUUID in ignoredDbUuidList, ignore the db
        if ((typeof selectedTag == 'undefined') && (typeof ignoredDbUuidList !== 'undefined') && ignoredDbUuidList.includes(theDbUUID)) {
            continue
        }
        // search in record corresponding to the database
        var theDbRecord = DNt.getRecordWithUuid(theDbUUID)
        var resultList = DNt.lookupRecordsWithTags(query, { in: theDbRecord })
        for (var key in resultList) {
            var record = resultList[key]
            var item = {}
            //name     record.name()
            //score    record.score()
            //tags     record.tags()
            //dbName   record.database().name()
            //path     record.path()
            //location record.location()

            // ignore group
            if (record.type() == 'group') { continue }

            var locationInDb = record.location()
            if (locationInDb.length > 1) {
                locationInDb = locationInDb.slice(0, -1).replace(/\//g, " > ")
            } else {
                locationInDb = ""
            }
            item["type"] = "file"
            item["title"] = record.name()
            item["score"] = record.score()
            item["arg"] = record.uuid()
            item["subtitle"] = "📂 " + record.database().name() + " " + locationInDb
            item["icon"] = { "type": "fileicon", "path": record.path() }
            item["mods"] = {
                "cmd": { "valid": true, "arg": record.path(), "subtitle": "🏷 " + record.tags().join(", ") },
                "alt": { "valid": true, "arg": record.uuid(), "subtitle": "Reveal in DEVONthink" }
            }
            allResult.push(item)
        }
    }

    // sorted by searching score
    allResult.sort(function(a, b) {
        return (a.score > b.score) ? -1 : (a.score < b.score) ? 1 : 0;
    });

    return JSON.stringify({ "items": allResult });
}