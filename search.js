'use strict';
function run(argv) {
    // read environment variables
    ObjC.import('stdlib')
    var env = $.NSProcessInfo.processInfo.environment;
    env = ObjC.unwrap(env)
    if ("selectedDbUUID" in env) { var selectedDbUUID = $.getenv('selectedDbUUID') }
    if ("filterOutGroup" in env) { var filterOutGroup = $.getenv('filterOutGroup').toLowerCase() }
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
    // const cjkRegex = /(\p{Unified_Ideograph}+)/ug
    const cjkRegex = /([\u4e00-\u9fff]+)/g
    const query = argv[0].replace(/^\s+|\s+$/g, '').replace(cjkRegex, "~$1");
    var DNt = Application("DEVONthink Pro");
    var allDB = DNt.databases
    // if selectedDbUUID exists, only search in selected db.
    if (typeof selectedDbUUID !== 'undefined') {
        allDB = { "0": DNt.getDatabaseWithUuid(selectedDbUUID) }
    }
    var allResult = []
    for (var db in allDB) {
        var theDbUUID = allDB[db].uuid()

        // if selectedDbUUID not exists and theDbUUID in ignoredDbUuidList, ignore the db
        if ((typeof selectedDbUUID == 'undefined') && (typeof ignoredDbUuidList !== 'undefined') && ignoredDbUuidList.includes(theDbUUID)) {
            continue
        }
        // search in record corresponding to the database
        var theDbRecord = DNt.getRecordWithUuid(theDbUUID)
        var resultList = DNt.search(query, { in: theDbRecord })
        for (var key in resultList) {
            var record = resultList[key]
            var item = {}
            var itemName = record.name()
            var itemScore = record.score()
            var itemTags = record.tags()
            var itemPath = record.path()
            var itemLocation = record.location()
            var itemUUID = record.uuid()

            // ignore group
            var titlePrefix = ""
            if (record.type() == 'group') {
                if (filterOutGroup == "yes") { continue }

                titlePrefix = "[Group] "
                if (itemLocation == "/Tags/") {
                    titlePrefix = "[Tag] "
                }
            }

            if (itemLocation.length > 1) {
                itemLocation = itemLocation.slice(0, -1).replace(/\//g, " > ")
            } else {
                itemLocation = ""
            }
            item["type"] = "file"
            item["title"] = titlePrefix + itemName
            item["score"] = itemScore
            item["arg"] = itemUUID
            item["subtitle"] = "📂 " + record.database().name() + " " + itemLocation
            item["icon"] = { "type": "fileicon", "path": itemPath }

            var itemTagStr;
            if (itemTags.length > 0) {
                itemTagStr = itemTags.join(", ")
            } else {
                itemTagStr = "No Tag"
            }

            item["mods"] = {
                "cmd": { "valid": true, "arg": itemPath, "subtitle": "🏷 " + itemTagStr},
                "alt": { "valid": true, "arg": itemUUID, "subtitle": "Reveal in DEVONthink" }
            }
            allResult.push(item)
        }
    }

    // sorted by searching score
    allResult.sort(function(a, b) {
        return (a.score > b.score) ? -1 : (a.score < b.score) ? 1 : 0;
    });

    if (allResult.length == 0) {
        return JSON.stringify({ "items": [{"title": "No document..."}] });
    }

    return JSON.stringify({ "items": allResult });
}


String.prototype.padLeft = function(char, length) {
    return char.repeat(Math.max(0, length - this.length)) + this;
}
String.prototype.padRight = function(char, length) {
    return this + char.repeat(Math.max(0, length - this.length));
}