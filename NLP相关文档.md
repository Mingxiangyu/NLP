# [Colab使用教程](https://my.oschina.net/u/4339899/blog/3434699)

最近在学习NLP，但是学习[深度学习](https://cuijiahua.com/blog/tag/深度学习/)算法，需要有 **GPU**，也就是显卡。

而显卡，需要是 NVIDIA 的显卡，也就是我们俗称的 N 卡。

虽然人人都喊「 AMD yes，AMD 真香」，但在深度学习领域，目前来看只能对 A 卡说 No。

因为，主流的推理框架，都需要在 NVIDIA 推出的 CUDA 运算平台上进行，使用上这也是最方便的。

所以，如果你没有 N 卡，比如你用 Mac 本或者 A 卡电脑，那么你只能使用 **CPU 版本的深度学习框架**。

深度学习使用 GPU 运算很快，用 CPU 巨慢无比。

如果只是进行算法的效果测试，那姑且可以用 CPU 试一试，不过很多算法就算测试，可能也需要跑上十几分钟。

如果要进行算法的训练，那必须用 GPU，用 CPU 跑训练会跑到怀疑人生，几个月不断电都未必训练好算法。

至于·=「Torch not complied with CUDA enabled」这个问题：

- 如果你有 GPU ，那么就是你没有配置好开发环境。
- 如果你没有 GPU，那么你就只能修改代码，使用 cpu 跑算法。

修改代码为 cpu 版，这个对新手可能有点难度，不同深度学习框架修改方法也不同。

好在有百度，直接搜索关键词「pytorch修改代码为cpu」，其他框架同理，教程非常多。

自己没有 GPU，但是我就想用！可以！引出文本的**重点**，教你如何「白嫖 GPU」。

以下为总结出Colaboratory的使用教程。

> 1. Google Colaboratory是谷歌提供的基于linux系统的免费云平台并支持免费的 GPU，内部已经集成了深度学习所需要的库，比如Tensorflow（目前Version：2.2.0rc3）和Keras（目前Version: 2.3.1）等，一般情况下无需我们再做配置，直接上传自己代码就能用了。
>
> 2. Colab 是Google的且服务器在国外
>
>    如果不能使用Google，推荐使用Kaggle（国内也能访问）👉 [免费的深度学习GPU环境Colab和Kaggle搭配使用](https://www.cnblogs.com/zgqcn/p/13475630.html#kaggle)
>    如果可以上Google，那就继续往下看学习Colab用法！如何进入Colab

>  推荐大家使用 Google云端硬盘上传文件然后加载到自己的Colab里。

## Colab的基本配置

1. **登录 [Google Drive](https://drive.google.com/)**,注册个`Google账号-->Google搜索“Google 云端硬盘”-->个人 转至Google云端硬盘`，然后你就可以看到以下界面啦：

2. **在 Google Drive 上创建文件夹，我创建的是名字为 app 的文件夹**

   ![s](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/1538832-20190714224844251-1534150405.png)

3. **创建新的 Colab 笔记（Notebook），通过 右键点击 > More > Colaboratory 步骤创建一个新的笔记**

   ![ss](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/1538832-20190714225153623-189155043.png)



![20200501123641432](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/20200501123641432.png)

大家可以`新建属于自己的Colab和文件夹`，新建的Colab的默认名称为Untitled，代码运行就在这里面操作，后面也以这个为例讲解。

不过现在莫要着急嘛，咱先把自己的工程代码上传到个人的文件夹中，这里我的叫test（我上传到test里的文件夹叫yolo3-keras，后面的栗子会用到）。

步骤为：`双击test文件夹-->进去后右键-->上传文件/上传文件夹-->根据需要上传自己的代码文件或文件夹`，上传时间长短视网络情况而定。完成这一步之后，我们就可以开始快乐的操作Colab啦~

## Colab如何操作？

在**步骤二**的基础上，我们双击自己建立的Colab，进去之后它长这样：

![img](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0ZsYWdfaW5n,size_16,color_FFFFFF,t_70.png)

具体一些区域的功能已经在图上注释了，大家可以先了解下。首先是先入门hello world，如下所示，在代码框里输入print("hello world!")，然后点击左边的运行按钮就可以

![img](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0ZsYWdfaW5n,size_16,color_FFFFFF,t_70-20220311113155289.png)

上方为入门Colab的使用，接下来是设置加速器为GPU加速

### 使用GPU

以下两种方式都可以：

1. "修改"->"笔记本设置"->"硬件加速器"选择GPU
2. "代码执行程序"->"更改运行时类型"->"硬件加速器"选择GPU

![image-20220311113541370](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/image-20220311113541370.png)

![img](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/459651-20190220093759669-715713462.png)

然后运行以下代码确认GPU是否正常运行

```python
import tensorflow as tf
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
  raise SystemError('GPU device not found')
else: 
  print(device_name)
```

运行正常可以看到如下结果：

![img](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/1410231-20190818230121013-917198933.png)

否则看到如下结果：

![img](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/6bb31b60b0606798eb1df8a2a312c063177.png)

或者使用命令:

~~~shell
!nvidia-smi
~~~

可以看到以下结果：

![img](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/1410231-20190818231722902-460103915.png)

否则看到如下结果：

![img](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/77574856ca06fc9a771dcd1dddbef5504b9.png)

PS：如果你有其他会话正在运行，可能会看到这样的提示:
![img](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/36b38caf0d03210e0dde46157ad1c787041.png)

### 切换文件夹

不能用Linux下常用的`cd`命令，要用如下命令:

 1.加载盘

```python
from google.colab import drive
drive.mount('/content/drive/')
```

![fs](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/1538832-20190714230932384-1359631752.png)

 2.切换到你要跑的目录下面

~~~python 
# 指定当前的工作文件夹
import os 
# 此处为google drive中的文件路径,drive为之前指定的工作根目录，要加上
os.chdir("/content/drive/My Drive/your_path")
~~~

### 安装Pytorch以及torchvision

Colab 一般情况下已经自带了pytorch环境了。若没有可以进行相应的安装：

```python
!pip install torch torchvision  # 在Colab中执行操作语句时，感叹号不能漏
```



## 装载Google云盘文件

![image-20220311114930181](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/image-20220311114930181.png)

装载完成之后的界面如下： 

![img](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0ZsYWdfaW5n,size_16,color_FFFFFF,t_70-20220311171446877.png)

## 解决Colab长时间无操作就掉线的问题

使用中会发现，当我们在训练模型的时候，如果长时间不操作Colab后他就会自动断线，这就很头疼了，我们也不能傻傻一直盯着它跑吧。莫慌，你可以通过以下简单的操作来解决：

> [# How to prevent Google Colab from disconnecting ?](https://medium.com/@shivamrawat_756/how-to-prevent-google-colab-from-disconnecting-717b88a128c0)

首先在Colab界面打开控制台（快捷键Ctrl+Shift+I），然后复制以下代码（这段代码的功能是设置每隔60000ms也就是1min自动点击一下Colab的“连接”操作，这样就不至于长时间误操作而导致自动断开连接啦，当然这只是个例子，方法不唯一，大家也可以调整下自己的间隔时间）：

```shell
function ClickConnect(){
    console.log("Working");
    document.querySelector("colab-toolbar-button#connect").click()
}
setInterval(ClickConnect, 60000)
```

把上面这段代码添加到下图所示的位置 ，然后敲一下回车键即可

![img](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0ZsYWdfaW5n,size_16,color_FFFFFF,t_70-20220311171313588.png)