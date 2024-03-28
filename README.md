# SimilarCharacter
对常用的6700个汉字进行音、形比较，输出一个相近字的列表。

Character文件是汉字总列表

Dict存放了四角码、相似音和结构字典

WriteNum是爬取和输出笔画数字典的爬虫

writenumDict是笔画数字典

Symbol_Structure是爬取结构代码的爬虫

JudgeSimilarity根据字形和音加权计算相似度输出相近字，是主函数

TransChar2Img将汉字转化为图片并保存

ProcessWithCV2将汉字图片进行对比，近似度超过阈值则写入文件

————————————————————————附件——————————————

四角编码字典7000字是标准四角码，为4位

四角编码字典70000字是带有辅码，为5位

结构字典中，1为左右结构，2为上下结构，3为左中右结构，4为上中下结构，5为全包围结构

笔画数字典为汉字的总笔画数。

注：部分文件可能中文有编码问题，使用gbk编码打开即可的，VSCode可以重新保存为utf-8编码格式。

![Alt](https://repobeats.axiom.co/api/embed/6a31e97dcb300359a3e776117d64ec101f95b07d.svg "Repobeats analytics image")
