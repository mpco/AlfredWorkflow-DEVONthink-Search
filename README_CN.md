# DEVONthink Search

强大的 DEVONthink 搜索工具。

分为两个版本：

- DEVONthink Search, 适用于 DEVONthink Personal。
    - [点击下载](https://github.com/mpco/AlfredWorkflow-DEVONthink-Search/releases/download/3.0/DEVONthink.Search.alfredworkflow)
    - 搜索准确度一般，因为是利用生成的 Spotlight Index 进行搜索。
    - 需要开启数据库属性中的 `Create Spotlight Index` （默认开启）。
    - 仅支持下文中的 `dnt + 关键词` 搜索方式。
- DEVONthink Pro Search, 适用于 DEVONthink Pro / Pro Office。
    - [点击下载](https://github.com/mpco/AlfredWorkflow-DEVONthink-Search/releases)
    - 搜索结果与 DEVONthink 中搜索结果一致，按照关键词匹配得分排列。
    - 无需开启数据库属性中的 `Create Spotlight Index`。
    - 搜索结果中显示的信息更丰富。

![对比](https://user-images.githubusercontent.com/3690653/48790858-3f872c00-ed2b-11e8-8ae6-683ce19cc597.png)

**说明：**

- DEVONthink Search 搜索结果的子文本（subtext）为下载该文件的 URL 或相应的 Spotlight Index 文件路径。
- DEVONthink Pro Search 搜索结果的子文本（subtext）为该文件在 DEVONthink 中所在的数据库+文件夹路径。按下 `⌘Command` 则显示为标签信息。

## 用法

- 输入 `dnt + 关键词` 在所有数据库中进行搜索。
- 输入 `dnd` 选择需要搜索的数据库
    - 按 `回车` 确认，接着输入 `关键词` 以进行搜索。
    - 按 `⌘Command + 回车` 列出该数据库中的所有标签（Tag）。选择某个标签，然后按下回车键，可列出所有附有该标签的文档。
- 输入 `dnm + 标签1, 标签2, ……`，列出所有数据库中同时附有这些标签的文档。多个标签以英文逗号分隔。**注意：标签必须是准确完整的，如标签“aBcD”，不能输入“aBc”，不能输入“abcd”。**

显示文档列表后，

* 按下 `回车` ，用 DEVONthink 打开所选文件。
* 按下 `⌘Command + 回车` 用外部程序（系统默认）打开所选文件。
* 按下 `⌥Option + 回车` 在 DEVONthink 窗口中显示所选文件。

![按下回车后效果](https://user-images.githubusercontent.com/3690653/48790940-73625180-ed2b-11e8-89dc-6bf4f6b9e72a.png)

## 配置

**仅适用于 DEVONthink Pro Search**

### `ignoredDbUuidList`：屏蔽某些数据库

使用 `dnt` 和 `dnm` 在所有数据库中进行搜索，但是我们可能需要屏蔽某些数据库。例如，我建立了一个**存档**数据库以保存一些文件，但平时一般不需要打开或查看。在 Alfred Workflow 环境变量 `ignoredDbUuidList` 中加入以**英文逗号**分隔的多个数据库 UUID 即可屏蔽这些数据库。设置后，依旧可以通过 `dnd` 指定在被屏蔽的数据库中进行搜索。

具体步骤：

1. 打开 DEVONthink，在窗口界面左侧右键点击某个数据库，选择 `Copy Database Link`，获得类似于 `x-devonthink-item://1FC1A542-D8CA-4807-B806-8617966870B5` 的链接。
2. 链接中的 `1FC1A542-D8CA-4807-B806-8617966870B5` 部分就是该数据库的 UUID。
3. 如果仅屏蔽一个数据库，直接填入 UUID 即可。如果多个，则以英文逗号分隔后填入，如 `1DA1A542-D8CA-4897-B806-8627964878B5,52893041-45C2-459E-9423-C1986E783417`。

![设置](https://user-images.githubusercontent.com/3690653/48790986-9987f180-ed2b-11e8-8f64-846d96fd26b9.png)

### `filterOutGroup`：在搜索结果中滤除文件夹和标签

如果你想在 `dnt` 的搜索结果中滤除文件夹和表情，可以设置 `filterOutGroup` 为 `yes`。


## 存在的问题

在 DEVONthink 中搜索，关键词中的 CJK 文字（中国、日本、韩国）需要在其前面加上`~`。如搜索`你abc我他`，需改为`~你abc~我他`。在 DEVONthink Pro Search 中，已使用正则表达式 `/(\p{Unified_Ideograph}+)/ug` 匹配中文字符以自动添加`~`。

但是该正则表达式无法匹配日韩文字。如果你遇到日韩文字搜索问题，可自行研究解决。