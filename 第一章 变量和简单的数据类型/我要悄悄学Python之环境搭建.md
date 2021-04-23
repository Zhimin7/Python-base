# 前言

话说，工欲善其事，必先利其器。

今天有几个小伙伴们问我，怎么样安装Python环境，我本来以为大家都是可以正常安装的，但是却不会安装，或是其他的原因安装失败。所以，今天我特地写一篇文章来告诉大家，怎么样安装Python的环境。

# Python安装包获取

首先，在浏览器上输入：

```
https://www.python.org/
```

进入Python官网，页面如下所示：

![](https://routing-ospf.oss-cn-beijing.aliyuncs.com/image-20210228185032256.png)

鼠标滑至Downloads并点击windows，如下图所示：

![](https://routing-ospf.oss-cn-beijing.aliyuncs.com/image-20210228185227447.png)

点击进去之后，往下拉，选择3.8.5这个版本，这个版本目前来说是比较稳定的版本，因此推荐大家下载这个版本的Python安装包。

![](https://routing-ospf.oss-cn-beijing.aliyuncs.com/image-20210228185432701.png)

不过你们的下载速度可能非常慢，因此我也为你们准备好了安装包。在微信公众号回复【**Python安装包**】即可获取安装包。

# Python的安装

本文以python-3.8.5-amd64为例，演示以下python的安装过程，其他版本的安装过程大同小异。x86适用于32位机，如果是64位windows操作系统，建议安装后缀为-amd64的版本。

- 首先双击python-3.8.5-amd64.exe。

![](https://routing-ospf.oss-cn-beijing.aliyuncs.com/image-20210228190348033.png)

- 选择Customize installation

![](https://routing-ospf.oss-cn-beijing.aliyuncs.com/image-20210228190007412.png)

- 选择next

![](https://routing-ospf.oss-cn-beijing.aliyuncs.com/image-20210228190432805.png)

- 点击安装

等待一段时间，安装就会结束。

# 验证安装

安装完成之后，我们需要检查安装是否成功。

开始——搜索框中输入“cmd”——回车，启动命令提示符——输入python。

![](https://routing-ospf.oss-cn-beijing.aliyuncs.com/image-20210228190654063.png)

如果出现的结果和上图类似，则说明你的安装是成功。

# 安装失败如何处理

如果出现说，**Python不是内部命令**，那是因为第一步，你没有按照我的操作来执行，没有添加环境变量。

添加环境变量的步骤如下：

- 右键此电脑，并点击属性

  ![](https://routing-ospf.oss-cn-beijing.aliyuncs.com/image-20210228190943857.png)

- 点击高级系统设置

![](https://routing-ospf.oss-cn-beijing.aliyuncs.com/image-20210228191021106.png)

- 点击环境变量

![](https://routing-ospf.oss-cn-beijing.aliyuncs.com/image-20210228191058562.png)

- 在系统环境变量中找到path，点击进去选择新建并将Python的安装路径添加进去。

![](https://routing-ospf.oss-cn-beijing.aliyuncs.com/image-20210228191219209.png)

在这里一共要添加两个路径，一个是Python的安装路径；另一个是Python安装路径下的Scripts文件下的路径。

将上面两个路径添加进去即可。

接下来再回到命令行进行测试。

如果大家还是安装失败，可以直接私信我，我手把手教你。

# 最后

没有什么事情是可以一蹴而就的，生活如此，学习亦是如此！

因此，哪里会有什么三天速成，七天速成的说法呢？

唯有坚持，方能成功！

**啃书君说**：

文章的每一个字都是我用心敲出来的，只希望对得起每一位关注我的人。在文章末尾点【**赞**】，让我知道，你们也在为自己的学习拼搏和努力。

**路漫漫其修远兮，吾将上下而求索**。

我是**啃书君**，一个专注于学习的人，**你懂的越多，你不懂的越多**。更多精彩内容，我们下期再见！