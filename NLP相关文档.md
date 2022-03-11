# [Colab使用教程](https://my.oschina.net/u/4339899/blog/3434699)

> Google Colaboratory是谷歌提供的基于linux系统的免费云平台，内部已经集成了深度学习所需要的库，比如Tensorflow（目前Version：2.2.0rc3）和Keras（目前Version: 2.3.1）等，一般情况下无需我们再做配置，直接上传自己代码就能用了。

## 如何进入Colab

> 推荐大家使用 Google云端硬盘上传文件然后加载到自己的Colab里。

首先你得注册个`Google账号-->Google搜索“Google 云端硬盘”-->个人 转至Google云端硬盘`，然后你就可以看到以下界面啦：

![20200501123641432](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/20200501123641432.png)

大家可以`新建属于自己的Colab和文件夹`，新建的Colab的默认名称为Untitled，代码运行就在这里面操作，后面也以这个为例讲解。

不过现在莫要着急嘛，咱先把自己的工程代码上传到个人的文件夹中，这里我的叫test（我上传到test里的文件夹叫yolo3-keras，后面的栗子会用到）。

步骤为：`双击test文件夹-->进去后右键-->上传文件/上传文件夹-->根据需要上传自己的代码文件或文件夹`，上传时间长短视网络情况而定。完成这一步之后，我们就可以开始快乐的操作Colab啦~

## Colab如何操作？

> 在**步骤二**的基础上，我们双击自己建立的Colab，进去之后它长这样：

![img](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0ZsYWdfaW5n,size_16,color_FFFFFF,t_70.png)

具体一些区域的功能已经在图上注释了，大家可以先了解下。首先当然是先入门hello world啦~如下所示，在代码框里输入print("hello world!")，然后点击左边的运行按钮就可以啦~~

![img](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0ZsYWdfaW5n,size_16,color_FFFFFF,t_70-20220311113155289.png)

上方为入门Colab的使用，接下来是设置加速器为GPU加速

### 使用GPU

以下两种方式都可以：

1. "修改"->"笔记本设置"->"硬件加速器"选择GPU
2. "代码执行程序"->"更改运行时类型"->"硬件加速器"选择GPU

![image-20220311113541370](../../Library/Application Support/typora-user-images/image-20220311113541370.png)

