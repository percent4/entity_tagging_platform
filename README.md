# entity_tagging_platform
A simple and useful platform for entity tagging using tornado.

### 背景介绍
&emsp;&emsp;在平时的NLP任务中，我们经常用到命名实体识别（NER），常用的识别实体类型为人名、地名、组织机构名，但是我们往往也会有识别其它实体的需求，比如时间、品牌名等。在利用算法做实体识别的时候，我们一般采用序列标注算法，这就对标注的文本格式有一定的要求，因此，一个好的序列标注的平台必不可少，将会大大减少我们标注的工作量，有效提升算法的更新迭代速度。
&emsp;&emsp;本文将介绍笔者的一个工作：自制的序列标注平台。我们以时间识别为例。比如，在下面的文章中：

> 按计划，2019年8月10日，荣耀智慧屏将在华为开发者大会上正式亮相，在8月6日，荣耀官微表示该产品的预约量已破十万台，8月7日下午，荣耀总裁赵明又在微博上造势率先打出差异化牌，智慧屏没有开关机广告，并表态以后也不会有，消费者体验至上，营销一波接一波，可谓来势汹汹。

我们需要从该文章中标注出三个时间：`2019年8月10日`，`8月6日`，`8月7日下午`，并形成标注序列。
&emsp;&emsp;下面将详细介绍笔者的工作。

### 序列标注平台
&emsp;&emsp;由于开发时间仓促以及笔者能力有限，因此，序列标注平台的功能还没有很完善，希望笔者的工作能抛砖引玉。
&emsp;&emsp;项目的结构图如下：

![项目结构图](https://upload-images.jianshu.io/upload_images/9419034-60d6c880d8b6905b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

templates中存放静态资源，time_index.html为平台的操作界面，time_output为平台标注完实体后的文件保存路径，time_server.py是用tornado写的服务端路径控制代码，utils.py中是获取某个路径下的txt文件的最大数值的函数。

### 平台使用

&emsp;&emsp;运行上述time_server.py后，在浏览器端输入网址: [http://localhost:9005/query](http://localhost:9005/query) , 则会显示如下界面：

![序列标注平台界面](https://upload-images.jianshu.io/upload_images/9419034-21a062ef0f971d0a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&emsp;&emsp;在`输入语料框`中，我们输入语料：

> 8月8日是“全民健身日”，推出重磅微视频《我们要赢的，是自己》。

在时间这个输入框中，可以标注语料中的时间，同时双击同一行中的下拉列表，就能显示该标注时间在语料中的起始位置，有时候同样的标注时间会在语料中出现多次，那么我们在下拉列表中选择我们需要的标注的起始位置即可。
&emsp;&emsp;点击`添加时间`按钮，它会增加一行标注，允许我们在同一份预料中标注多个时间。我们的一个简单的标注例子如下：

![标注过程的例子](https://upload-images.jianshu.io/upload_images/9419034-17ccdd7f4a0f5a9c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&emsp;&emsp;点击`显示标注`，则会显示我们标注完后形成的序列标注信息，同时将该序列信息保存为txt文件，该txt文件位于time_output目录下。在网页上的序列标注信息如下：

![形成的标注序列](https://upload-images.jianshu.io/upload_images/9419034-a8bff6c25668d696.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

同时，我们也可以查看保存的txt文档信息，如下：

![保存的txt文件](https://upload-images.jianshu.io/upload_images/9419034-4dcfbe3f80cffda6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

&emsp;&emsp;点击`返回`按钮，它会允许我们进行下一次的标注。刚才展示的只是一个简单例子，稍微复杂的标注如下图：

![稍微复杂些的标注](https://upload-images.jianshu.io/upload_images/9419034-92373ff7022271ea.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

它形成的标注序列(部分)如下：

```
按	O
计	O
划	O
，	O
2	B-TIME
0	I-TIME
1	I-TIME
9	I-TIME
年	I-TIME
8	I-TIME
月	I-TIME
1	I-TIME
0	I-TIME
日	I-TIME
，	O
荣	O
耀	O
智	O
慧	O
屏	O
将	O
在	O
华	O
为	O
开	O
发	O
者	O
大	O
会	O
上	O
正	O
式	O
亮	O
相	O
，	O
在	O
8	B-TIME
月	I-TIME
6	I-TIME
日	I-TIME
，	O
荣	O
耀	O
官	O
微	O
表	O
示	O
该	O
产	O
品	O
......
```

### 总结

&emsp;&emsp;本平台仅作为序列标注算法的前期标注工具使用，并不涉及具体的算法。另外，后续该平台也会陆续开放出来，如果大家有好的建议，也可以留言～
&emsp;&emsp;本项目已上传只Github, 网址为： [https://github.com/percent4/entity_tagging_platform](https://github.com/percent4/entity_tagging_platform)

