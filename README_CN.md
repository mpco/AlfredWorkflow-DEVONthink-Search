# DEVONthink Search

强大的 DEVONthink 搜索工具。

分为两个版本：

- DEVONthink Search, 适用于 DEVONthink Personal。
    - [点击下载]()
    - 搜索准确度一般，因为是利用生成的 Spotlight Index 进行搜索。
    - 需要开启数据库属性中的 `Create Spotlight Index` （默认开启）。
    - 不支持`dnd`指令与多个数据库。
- DEVONthink Pro Search, 适用于 DEVONthink Pro / Pro Office。
    - [点击下载]()
    - 搜索结果与 DEVONthink 中搜索结果一致，按照关键词匹配得分排列。（滤除搜索结果中的文件夹）
    - 无需开启数据库属性中的 `Create Spotlight Index`。
    - 搜索结果中显示的信息更丰富。

![对比](https://user-images.githubusercontent.com/3690653/48790858-3f872c00-ed2b-11e8-8ae6-683ce19cc597.png)

**说明：**

- DEVONthink Search 搜索结果的子文本（subtext）为下载该文件的 URL 或相应的 Spotlight Index 文件路径。
- DEVONthink Pro Search 搜索结果的子文本（subtext）为该文件在 DEVONthink 中所在的数据库+文件夹路径。按下 `⌘Command` 则显示为标签信息。


## 用法

- 输入 `dnt + 关键词` 在所有数据库中进行搜索。
- 输入 `dnd` 选择需要搜索的数据库，按回车确认，接着输入 `关键词` 以进行搜索。

搜索后，

* 按下 `回车` ，用 DEVONthink 打开所选文件。
* 按下 `⌘Command + 回车` 用外部程序（系统默认）打开所选文件。
* 按下 `⌥Option + 回车` 在 DEVONthink 窗口中显示所选文件。

![按下回车后效果](https://user-images.githubusercontent.com/3690653/48790940-73625180-ed2b-11e8-89dc-6bf4f6b9e72a.png)

## 配置

**仅适用于 DEVONthink Pro Search**

使用 `dnt` 默认在所有数据库中进行搜索，但是我们可能需要屏蔽某些数据库。例如，我建立了一个**存档**数据库以保存一些文件，但平时一般不需要打开或查看。在 Alfred Workflow 环境变量 `ignoredDbUuidList` 中加入以**英文逗号**分隔的多个数据库 UUID 即可屏蔽这些数据库。设置后，依旧可以通过 `dnd` 指定在被屏蔽的数据库中进行搜索。

具体步骤：

1. 打开 DEVONthink，在窗口界面右侧右键点击某个数据库，选择 `Copy Database Link`，获得类似于 `x-devonthink-item://1FC1A542-D8CA-4807-B806-8617966870B5` 的链接。
2. 链接中的 `1FC1A542-D8CA-4807-B806-8617966870B5` 部分就是该数据库的 UUID。
3. 如果仅屏蔽一个数据库，直接填入 UUID 即可。如果多个，则以英文逗号分隔后填入，如 `1DA1A542-D8CA-4897-B806-8627964878B5,52893041-45C2-459E-9423-C1986E783417`。

![设置](https://user-images.githubusercontent.com/3690653/48790986-9987f180-ed2b-11e8-8f64-846d96fd26b9.png)

## 存在的问题

在 DEVONthink 中搜索，关键词中的 CJK 文字（中国、日本、韩国）需要在其前面加上`~`。如搜索`你abc我他`，需改为`~你abc~我他`。在 DEVONthink Pro Search 中，已使用正则表达式 `/(\p{Unified_Ideograph}+)/ug` 匹配中文字符以自动添加`~`。

但是该正则表达式无法匹配日韩文字。如果你遇到日韩文字搜索问题，可自行研究解决。