
# DEVONthink Search

Powerful tool for seaching in DEVONthink, for DEVONthink 3.x.

For DEVONthink 2.x, you can use the versions of this workflow before V7.0. Switch to [Branch DEVONthink 2.x](https://github.com/mpco/AlfredWorkflow-DEVONthink-Search/tree/DEVONthink2.x) to access the README document and source code.

[Download](https://github.com/mpco/AlfredWorkflow-DEVONthink-Search/releases) [中文说明](https://github.com/mpco/AlfredWorkflow-DEVONthink-Search/blob/master/README_CN.md)

## Usage

- Type `dnt + keywords` to search in all opened databases in Alfred. 
- Type `dnts + keywords` to search in DEVONthink window.
- Type `dnd` to choose which datebase to search
    - Press `Enter`, then type in `keywords` to search in the chosen database. 
    - Press `⌘Command + Enter` to list all tags in the database, then choose a tag and press `Enter` to list all documents which have the tag.
- Type `dnm + tag1, tag2, ...` to list all documents which have these tags in all database. **Tags inputed must be exact. For example, Tag `aBcD` can't be inputed as `aBc` or `abcd`**
- Actions for Workspace:
    - Type `dnw` to list all workspaces, press `Enter` to load the selected workspace.
    - Type `dnwa + WorkspaceName` to save current workspace named `WorkspaceName`.

After documents were listed,

- Press `Enter` to open the selected file with external editor.
- Press `⌘Command + Enter` to open with DEVONthink.
- Press `⌥Option + Enter` to reveal result in DEVONthink.
- Press `→`, `fn`, etc. to show file actions of Alfred. The keys are set in `Features → File Search → Actions` of Alfred Preferences.
- Press `Shift` or `⌘Command + Y` to `QuickLook` the selected file.
- Press `⌘Command + C` to copy DEVONthink link (x-devonthink-item://xxxx) of the selected file.
- Drag & Drop file in the result list to wherever you want.

![Enter](https://user-images.githubusercontent.com/3690653/48790940-73625180-ed2b-11e8-89dc-6bf4f6b9e72a.png)

## Configuration

### `ignoredDbUuidList`: ignore databases

`dnt` and `dnm` search in **all** opened databases. You can ignore some databases by setting `ignoredDbUuidList` environment variable in Alfred workflow.

1. Copy database link in DEVONthink, which is similar to `x-devonthink-item://1FC1A542-D8CA-4807-B806-8617966870B5`.
2. The part `1FC1A542-D8CA-4807-B806-8617966870B5` is the database's UUID.
3. Fill in workflow configuration with UUIDs. You should separate multiple UUIDs with comma(,).

![Configuration](https://user-images.githubusercontent.com/3690653/48790986-9987f180-ed2b-11e8-8f64-846d96fd26b9.png)

### `filterOutGroup`: filter out group and tag in searching result

You can set environment variable `filterOutGroup` to `yes` if you want to filter out group and tag.

### Automation permission in macOS Mojave

Alfred will ask for Automation permission to control DEVONthink when you run the workflow for the first time. You should check up permission of Alfred controlling DEVONthink in `System Preferences → Security & Privacy → Privacy → Automation` if the workflow doesn't work.

## Known issues

CJK (Chinese, Japanese, and Korean) characters should be added `~` in the front when seaching in DEVONthink. For example, searching keywords `你abc我他` should be converted to `~你abc~我他`. It's added automatically in `DEVONthink Search` by using regular expression `/([\u4e00-\u9fff]+)/g` to matching Chinese characters.

The regular expression can't match Japanese or Korean characters. You can research more perfect regular expressions which match CJK and tell me.

## Todo

1. Support Favourite Groups.