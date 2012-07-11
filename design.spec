为了方便用户添加待翻译文章，我们需要将待翻译文章智能化处理成为方便翻译的格式。
格式有几个特征：
1、只有简单的几个 style
color
strong italic
font size
font family
link
解决：1)用 webkit 渲染后将多余 style 清除，合并 style，重新生成文档。
2)用现有工具清除。

2、有明显标记分段。先采用双回车即分段。
分段是为了给某一段加评注、评论。

3、先不考虑 theme 制定，统一使用 djangobook 的 theme (希望他们不会找我)
