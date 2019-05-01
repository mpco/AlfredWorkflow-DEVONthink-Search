'use strict';
function run() {
    var DNt = Application("DEVONthink 3");
    var allDB = DNt.databases
    var allResult = []
    for (var db in allDB) {
        var item = {}
        item["title"] = allDB[db].name()
        item["type"] = "file"
        //item["arg"] = allDB[db].uuid()
        item["subtitle"] = "Search in this database"
        item["variables"] = { "selectedDbUUID": allDB[db].uuid(), "selectedDbName": item["title"] }
        allResult.push(item)
    }

    return JSON.stringify({ "items": allResult });
}