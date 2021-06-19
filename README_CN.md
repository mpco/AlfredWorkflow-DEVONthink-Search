<h1 align="center">DEVONthink Search</h1>

强大的 DEVONthink 搜索工具，适用于 DEVONthink 3 的各个版本。

**注意：** DEVONthink 2.x 请使用 7.0 之前的版本，说明文档及代码请查看[相应分支](https://github.com/mpco/AlfredWorkflow-DEVONthink-Search/tree/DEVONthink2.x)。

[这里下载](https://github.com/mpco/AlfredWorkflow-DEVONthink-Search/releases)

## 用法

- 输入 `dnt + 关键词` 在 Alfred 中搜索所有数据库。搜索结果按照相关度得分排序，与 DEVONthink 中一致。
- 输入 `dnts + 关键词` 在 DEVONthink 的窗口中进行搜索。
    - 按 `回车` 在已经打开的窗口中搜索。
    - 按 `⌘Command + 回车` 在新建窗口中搜索。
- 输入 `dnd` 选择需要搜索的数据库
    - 按 `回车` 确认，接着输入 `关键词` 以进行搜索。
    - 按 `⌘Command + 回车` 列出该数据库中的所有标签（Tag）。选择某个标签，然后按下回车键，可列出所有附有该标签的文档。
    - 按 `⌥Option + 回车` 列出该数据库中的智能文件夹。
- 输入 `dnm + 标签1, 标签2, ……`，列出所有数据库中同时附有这些标签的文档。多个标签以英文逗号分隔。**注意：标签必须是准确完整的，如标签“aBcD”，不能输入“aBc”，不能输入“abcd”。**
- Workspace 相关动作:
    - 输入 `dnw` 列出所有 Workspace，按下`回车`加载所选项。
    - 输入 `dnwa + 名称` 将当前窗口布局保存为 Workspace 并命名。
- 输入 `dnf` 列出收藏。
- 输入 `dnsg` 列出所有打开数据库的智能文件夹。

显示结果列表后，

* 按下 `回车` 用外部程序（系统默认）打开所选文件。
* 按下 `⌘Command + 回车` 用 DEVONthink 打开所选文件。
* 按下 `⌥Option + 回车` 在 DEVONthink 窗口中显示所选文件。
* 按下 `⇧Shift + 回车` 复制所选文件的 Markdown 格式链接。
* 按下 `→` 或 `fn` 等，显示 Alfred 文件动作。可以在 Alfred 设置里 `Features → File Search → Actions` 中查看或修改按键。
* 按下 `Shift` 或 `⌘Command + Y` 可以预览（QuickLook）当前选中的文件。
* 按下 `⌘Command + C` 复制当前选中的文件在 DEVONthink 中的链接（x-devonthink-item://xxxx）。
* 直接拖拽列表中的文件，复制到你需要的地方。

![按下回车后效果](https://user-images.githubusercontent.com/3690653/48790940-73625180-ed2b-11e8-89dc-6bf4f6b9e72a.png)

## 配置

### `ignoredDbUuidList`：屏蔽某些数据库

使用 `dnt` 和 `dnm` 在所有数据库中进行搜索，但是我们可能需要屏蔽某些数据库。例如，我建立了一个**存档**数据库以保存一些文件，但平时一般不需要打开或查看。在 Alfred Workflow 环境变量 `ignoredDbUuidList` 中加入以**英文逗号**分隔的多个数据库 UUID 即可屏蔽这些数据库。设置后，依旧可以通过 `dnd` 指定在被屏蔽的数据库中进行搜索。

具体步骤：

1. 打开 DEVONthink，在窗口界面左侧右键点击某个数据库，选择 `Copy Database Link`，获得类似于 `x-devonthink-item://1FC1A542-D8CA-4807-B806-8617966870B5` 的链接。
2. 链接中的 `1FC1A542-D8CA-4807-B806-8617966870B5` 部分就是该数据库的 UUID。
3. 如果仅屏蔽一个数据库，直接填入 UUID 即可。如果多个，则以英文逗号分隔后填入，如 `1DA1A542-D8CA-4897-B806-8627964878B5,52893041-45C2-459E-9423-C1986E783417`。

<img src="https://user-images.githubusercontent.com/3690653/48790986-9987f180-ed2b-11e8-8f64-846d96fd26b9.png" width="450">

### `filterOutGroup`：在搜索结果中滤除文件夹和标签

如果你想在 `dnt` 的搜索结果中滤除文件夹和表情，可以设置 `filterOutGroup` 为 `yes`。

### macOS Mojave 上的权限问题

需确保 `系统偏好设置 → 安全性与隐私 → 隐私 → 自动化` 中，Alfred 拥有控制 DEVONthink 的权限。一般情况下，第一次运行该 Workflow 时，会弹窗申请该权限，授权即可。如果始终无法正常搜索，可检查该权限设置。

## 存在的问题
