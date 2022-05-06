# win11家庭版-3050TI显卡安装CUDA11.3

### CUDA ToolKit 安装

#### 查看自己电脑的显卡驱动版本

注意电脑显卡不是NVIDIA的忽略这一步，非NVIDIA显卡不能安装CUDA。

![image-20220505165803829](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505165803829.png)

#### 显卡驱动支持的CUDA版本查看

> CUDA的版本是跟显卡型号有关还是驱动有关？
>
> 一般是驱动版本决定了能用的CUDA版本的上限，比如新版的显卡驱动可以支持老的CUDA runtime。但是老的显卡可能无法更新到最新的显卡驱动，比如Fermi显卡只能装到391驱动，因此只能用到CUDA9.1。除此之外，显卡硬件与CUDA compute capability相关，当然编译时也可以指定streaming multiprocessor。新的架构支持更多特性就是了。

这里CUDA11.6是支持的最高版本的CUDA，可以向下兼容，**但是注意不能安装高于这个版本的CUDA哦**，且可以安装多个版本的CUDA，可以通过更改`环境变量`来更改为你需要用到的CUDA版本

![image-20220505170334200](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505170334200.png)

查[官方文档(https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)

![image-20220505170451906](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505170451906.png)

### cuda toolkit下载

[CUDAtoolkit下载地址(https://developer.nvidia.com/cuda-toolkit-archive)](https://developer.nvidia.com/cuda-toolkit-archive)选择相应版本号

根据我要装的**pytorch支持的cuda版本**、并且**cuda版本要在我自己电脑的驱动版本之下**，选择安装cuda11.3

> pytorch安装
>
> [当前pytorch安装](https://pytorch.org/get-started/locally/)
> [以往pytorch安装](https://pytorch.org/get-started/previous-versions/)

![image-20220505170728997](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505170728997.png)

选择符合自己机器的系统下载（`建议选local，local相当于离线安装，相对稳定，network相当于下载器在线下载`）

![image-20220505171729944](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505171729944.png)

### cuda toolkit安装

![image-20220505171757844](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505171757844.png)

双击打开该exe后为下图界面

![image-20220505171944774](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505171944774.png)

图中路径仅为`该exe文件解压路径`，不是最后安装路径，安装完成后程序自行删除，所以最后的**`程序安装路径`一定不要在这个`解压路径`**下，否则会出现异常问题。

程序自解压后进入安装界面

![image-20220505172351311](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505172351311.png)

![image-20220505172412908](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505172412908.png)

如果是第一次安装CUDA则选择`精简安装`，否则建议`自定义安装`，**自定义安装选项的时候，CUDA是核心组件必须安装**

![image-20220505172654489](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505172654489.png)

安装路径可以自行选择，系统默认是在系统盘C盘，为了方便日后管理，可以安装到非系统盘的其他盘 ，不过要**`记住选择的路径`**，后续环境变量和`CUDnn`都需要用上该路径

![image-20220505172915277](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505172915277.png)

下一步后出现没有支持的VS，需要勾选后进行安装，

![img](https://img-blog.csdnimg.cn/067cd8b8b37246d3b2ba631bdac3c8fd.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6LCi5qGl5YWJ,size_20,color_FFFFFF,t_70,g_se,x_16)

我应为之前安装过11.6CUDA，11.3的VS无法安装，出现下图中提示，正常情况可以安装完成

![image-20220505173327499](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505173327499.png)

下一步后就ok

![image-20220505173720434](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505173720434.png)

打开路径 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\extras\CUPTI\lib64，查看有没有`cupti64_2021.1.1.dll`

有这个就说明CUPT1已成功

![image-20220505191008863](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505191008863.png)

### cuda toolkit设置

查看系统变量中是否添加了路径，如果没有需要自己添加

![image-20220505174025151](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505174025151.png)

用命令行检查下

``` sh
nvcc --version 或 nvcc -V #查看当前cuda版本
set cuda #查看cuda系统变量
```

![image-20220505174743911](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505174743911.png)

## CUDNN的安装

### cuDNN下载

cuDNN地址如下，不过要注意的是，需要注册一个账号才可以进入到下载界面。大家可以放心注册的。

注册成功后的下载界面

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210525004015691.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg0ODYxNA==,size_16,color_FFFFFF,t_70)



可以使用下面网址，查看适配的 cuDNN

[https://developer.nvidia.com/rdp/cudnn-archive](https://developer.nvidia.cn/rdp/cudnn-archive)

[这里(https://developer.nvidia.cn/rdp/cudnn-archive)](https://developer.nvidia.cn/rdp/cudnn-archive)
选择相应版本的cuDNN

![image-20220505184157032](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505184157032.png)

### cuDNN安装

cuDNN安装叫配置更为准确，我们先把下载的 cuDNN 解压缩，会得到下面的文件：

- cuDNN 解压缩后的文件

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210525110329269.png)

下载后发现其实cudnn不是一个exe文件，而是一个压缩包，解压后，有三个文件夹，把三个文件夹拷贝到`cuda的安装目录`下。

CUDA 的安装路径在前面截图中有，或者打开电脑的环境变量查看，默认的安装路径如下：

``` 
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.3
```

后面那个`v11.3`是你自己的版本号CUDA 安装目录文件：

- CUDA 安装目录文件：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210525111005422.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg0ODYxNA==,size_16,color_FFFFFF,t_70)

拷贝时看到，CUDA 的安装目录中，有和 cuDNN 解压缩后的同名文件夹，这里注意，不需要担心，直接复制即可。cuDNN 解压缩后的同名文件夹中的配置文件会添加到 CUDA安装目录中的同名文件夹中。

- 拷贝成功后的文件

  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210525111342257.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg0ODYxNA==,size_16,color_FFFFFF,t_70)

现在大家应该可以理解，cuDNN 其实就是 CUDA 的一个补丁而已，专为深度学习运算进行优化的。然后再添加环境变量

### cuDNN设置

1. 往系统环境变量中的 path 添加如下路径（根据自己的路径进行修改）

```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.3\bin

C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.3\include

C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.3\lib

C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.3\libnvvp
```

2. 验证安装是否成功

   配置完成后，我们可以验证是否配置成功，主要使用CUDA内置的deviceQuery.exe 和 bandwithTest.exe，如果运行后`Result = PASS`则表示CUDA及CUDNN成功安装：
   首先win+R启动cmd，cd到`CUDA安装目录`下的 …\extras\demo_suite,然后分别执行bandwidthTest.exe和deviceQuery.exe,应该得到下图:

   ![image-20220505185310376](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505185310376.png)

![image-20220505191328815](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505191328815.png)

## 疑难问题

- 如果在任务管理器还是看不到 CUDA

> 按Win+I打开系统设置，依次进入系统、显示、图形设置（在页面底部）
> 发现硬件加速 GPU 计划被开启，把它关掉，然后重启即可。

![image-20220505183844730](C:\Users\zhouhuilin\AppData\Roaming\Typora\typora-user-images\image-20220505183844730.png)

## 参考博客

[【CUDA】cuda安装 （windows版） ](https://blog.csdn.net/weixin_43848614/article/details/117221384) https://blog.csdn.net/weixin_43848614/article/details/117221384

