[TOC]

> ### **以下均以conda 4.10.3版本为例，anaconda安装包版本为Anaconda3-2021.11-MacOSX-x86_64 (1).pkg**

# **管理conda**

接下来均是以命令行模式进行介绍，Windows用户请打开“Anaconda Prompt”；macOS和Linux用户请打开“Terminal”（“终端”）进行操作。

## **1. 验证conda已被安装**

```shell
conda -V
```

或

```sh
conda --version
```

终端上将会以conda 版本号的形式显示当前安装conda的版本号。如：

~~~bash
conda 4.10.3
~~~

注意：

如果出现错误信息，则需核实是否出现以下情况：

1. 使用的用户是否是安装Anaconda时的账户。
2. 是否在`安装Anaconda之后重启了终端。`
3. 在下载的时候64位怎么也下载不下来，想着用32位凑合一下，在这里奉劝各位不要，不然会在全部装好之后出现以下报错。明明都装好了，测试的时候出现ModuleNotFoundError的报错，No module named ‘torch’

安装完成后去查看下环境变量，确认conda是否将变量添加进环境变量中，通过`sudo vi ~/.bash_profile`命令查看，成功添加效果如下

```bash
# Setting PATH for Python 3.6
# The original version is saved in .bash_profile.pysave
#PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
#export PATH

#alias pip="/Library/Frameworks/Python.framework/Versions/3.6/bin/pip3"
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/opt/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/opt/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

**原来安装Python添加的环境变量需要注释或者放到conda添加的下面，`否则后续在虚拟环境中pip命令使用的还是本机的pip命令`**

## **2. 更新conda至最新版本**

```shell
conda update conda
```

###   更新Anaconda到最新版

​          [注意：在更新Anaconda前需要先更新conda]

~~~
conda update anaconda 
~~~

执行命令后，conda将会对版本进行比较并列出可以升级的版本。同时，也会告知用户其他相关包也会升级到相应版本。

当较新的版本可以用于升级时，终端会显示Proceed ([y]/n)?，此时输入y即可进行升级。

## **3. 查看conda帮助信息**

```sh
conda -h
```

## **4.卸载conda**

① Linux 或 macOS

```sh
rm -rf ~/anaconda2
```

或

```sh
rm -rf ~/anaconda3
```

即删除Anaconda的安装目录。根据安装的Anaconda版本选择相应的卸载命令。

**② Windows**

~~控制面板 → 添加或删除程序 → 选择“Python X.X (Anaconda)” → 点击“删除程序”~~

~~注意：~~

~~Python X.X：即Python的版本，如：Python 3.6。~~

~~Windows 10的删除有所不同。~~

直接卸载会有配置文件，注册表等残留

- `conda install anaconda-clean`
- `anaconda-clean --yes`
- 进入安装目录执行 `Uninstall_Anaconda3.exe`

# **管理环境**

接下来均是以命令行模式进行介绍，Windows用户请打开“Anaconda Prompt”；macOS和Linux用户请打开“Terminal”（“终端”）进行操作。

## 1.创建新环境

### 安装虚拟环境到默认路径下

```sh
conda create -name <env_name> <package_names>
```

注意：

`<env_name>`即创建的环境名。建议以英文命名，且不加空格，名称两边不加尖括号“<>”。

`<package_names>`即安装在环境中的包名。名称两边不加尖括号“<>”。

小心`-`需要为英文，否则出现该报错

```sh
CondaValueError: The target prefix is the base prefix. Aborting.
```

```sh
conda create –n pytorch python=3.6  #错误！中文-
conda create -n pytorch python=3.6  #正确！英文-
```

如果要安装指定的版本号，则只需要在包名后面以=和版本号的形式执行。如：

```sh
conda create -name python2 python=2.7 #即创建一个名为“python2”的环境，环境中安装版本为2.7的python。
```

如果要在新创建的环境中创建多个包，则直接在`<package_names>`后以空格隔开，添加多个包名即可。如：

```sh
conda create -n python3 python=3.5 numpy pandas #即创建一个名为“python3”的环境，环境中安装版本为3.5的python，同时也安装了numpy和pandas。
```

–name同样可以替换为-n。

提示：默认情况下，新创建的环境将会被保存在/Users/<user_name>/anaconda3/env目录下，其中，`<user_name>`为当前用户的用户名。

### **安装虚拟环境到指定路径的命令如下：**

```sh
conda create --prefix=D:\python36\py36 python=3.6
```

上面的命令中， 路径D:\python36是先建好的文件夹，py36是需要安装的虚拟环境名称。请注意，安装完成后，虚拟环境的全称包含整个路径，为D:\python36\py36。激活指定路径下的虚拟环境的命令如下：

```sh
conda activate D:\python36\py36
```

## **2. 切换环境**

① Linux 或 macOS

```sh
source activate <env_name> #即将弃用，使用 conda activate <env_name>
conda activate <env_name>
```

② Windows

```sh
activate <env_name>
```

③ 提示

如果创建环境后安装Python时没有指定Python的版本，那么将会安装与Anaconda版本相同的Python版本，即如果安装Anaconda第2版，则会自动安装Python 2.x；如果安装Anaconda第3版，则会自动安装Python 3.x。

当成功切换环境之后，在该行行首将以`“(env_name)”`或`“[env_name]”`开头。其中，`“env_name”`为切换到的环境名。如：在macOS系统中执行`source active python2`，即切换至名为`“python2”`的环境，则行首将会以`(python2)`开头。

```sh
conda config --set auto_activate_base false  #关闭自动激活状态
conda config --set auto_activate_base true  #关闭自动激活状态
```

## **3. 退出环境至root**

① Linux 或 macOS

```sh
source deactivate #该方法conda 4.10.3版本提示即将弃用，需要使用 conda deactivate
conda deactivate
```

② Windows

```sh
deactivate
```

③ 提示

当执行退出当前环境，回到root环境命令后，原本行首以`“(env_name)”`或`“[env_name]”`开头的字符将不再显示。

## 4**. 显示已创建环境**

```sh
conda info -e
```

或

```sh
conda env list
```

例如：

```bash
#
base                  *  /opt/anaconda3
```

结果中星号“*”所在行即为当前所在环境。macOS系统中默认创建的环境名为“base”。

## 5.复制环境

> Conda是没有重命名环境的功能的, 要实现这个基本需求, 只能通过愚蠢的**克隆-删除**的过程。
> 切记不要直接mv移动环境的文件夹来重命名, 会导致一系列无法想象的错误的发生!

```sh
conda create –name <new_env_name> –clone <copied_env_name>
```

注意：

`<copied_env_name>`即为被复制/克隆环境名。环境名两边不加尖括号“<>”。

`<new_env_name>`即为复制之后新环境的名称。环境名两边不加尖括号“<>”。

如：

```sh
conda create –name py2 –clone python2 #即为克隆名为“python2”的环境，克隆后的新环境名为“py2”。
```

此时，环境中将同时存在“python2”和“py2”环境，且两个环境的配置相同。

## 6.删除环境

```sh
conda remove –-name <env_name> -–all
```

注意：`<env_name>`为被删除环境的名称。环境名两边不加尖括号“<>”。

如：

```sh
conda remove –-name python3 --all
```

如果提示：

```bash
CondaEnvironmentError: cannot remove current environment. deactivate and run conda remove again
```

请判断当前是否在要删除的虚拟环境下，如果已经退出，执行删除命令仍然报上述错误，可以尝试下列命令：

```sh
 conda env remove -n python3
```

## 分享环境

```sh
conda env export > environment.yaml
```

将当前环境下的 package 信息存入名为 environment 的 YAML 文件中

## 导入环境

```sh
conda env create -f environment.yaml
```

用分享的 YAML 文件来创建一摸一样的运行环境

## 自动开启/关闭环境

```sh
conda activate   #默认激活base环境
conda activate xxx  #激活xxx环境
conda deactivate #关闭当前环境
conda config --set auto_activate_base false  #关闭自动激活状态
conda config --set auto_activate_base true  #关闭自动激活状态
```

# **管理包**

## 1. 查找可供安装的包版本

① 精确查找

```sh
conda search –full-name <package_full_name>
```

注意：

`–full-name`为精确查找的参数。

`<package_full_name>`是被查找包的全名。包名两边不加尖括号“<>”。

例如：

```sh
conda search –full-name python # 即查找全名为“python”的包有哪些版本可供安装。
```

② 模糊查找

```sh
conda search <text>
```

注意：`<text>`是查找含有此字段的包名。此字段两边不加尖括号“<>”。

例如：

```sh
conda search py # 即查找含有“py”字段的包，有哪些版本可供安装。
```

## 2. 获取当前环境中已安装的包信息

```sh
conda list
```

执行上述命令后将在终端显示当前环境已安装包的包名及其版本号。

## **3.查看指定环境下的包：**

```sh
conda list -n  <env_name>
```

## 3. 安装包

### 在指定环境中安装包

```sh
conda install –name <env_name> <package_name>
```

注意：

`<env_name>`即将包安装的指定环境名。环境名两边不加尖括号“<>”。

`<package_name>`即要安装的包名。包名两边不加尖括号“<>”。

例如：

```sh
conda install –name python2 pandas # 即在名为“python2”的环境中安装pandas包。
```

### 在当前环境中安装包

```sh
conda install <package_name>
```

注意：

`<package_name>`即要安装的包名。包名两边不加尖括号“<>”。

执行命令后在当前环境中安装包。

例如：

```sh
conda install pandas # 即在当前环境中安装pandas包。
```

### 清除Conda索引缓存*清理没有使用过的包*

~~~
conda clean -p
~~~

### PackagesNotFoundError: The following packages are not available from current channels的解决办法

#### 解决方法一：将[conda](https://so.csdn.net/so/search?q=conda&spm=1001.2101.3001.7020)-forge添加到搜索路径上

首先，当出现这种报错时，应该首先尝试使用以下命令将conda-forge channel添加到你的channel列表中

```sh
conda config --append channels conda-forge
```

它告诉conda在搜索软件包时也要在conda-forge channel上查看。

然后你就可以尝试利用如下命令再次安装

```sh
conda install 包名
```

原因在于：channel可以看成是托管python包的服务器，当无法通过标准channel获得python包时，社区驱动的conda-forge通常是一个很好的地点。大部分问题都可以利用这条语句解决。

#### 方法二：利用报错提示，进入annaconda网站利用命令解决

当添加上述语句仍然出现错误，安装某个python包时（并不特别对于某个特定包，各种包有时都会出现这种情况 。会出现当前channel不可用，并报错：

```sh
PackagesNotFoundError: The following packages are not available from current channels:
```

报错的完整显示：

```
Collecting package metadata (current_repodata.json): ...working... done
Solving environment: ...working... failed with initial frozen solve. Retrying with flexible solve.
Collecting package metadata (repodata.json): ...working... done
Solving environment: ...working... failed with initial frozen solve. Retrying with flexible solve.


PackagesNotFoundError: The following packages are not available from current channels:

  - igraph

Current channels:

  - https://repo.anaconda.com/pkgs/main/win-64
  - https://repo.anaconda.com/pkgs/main/noarch
  - https://repo.anaconda.com/pkgs/r/win-64
  - https://repo.anaconda.com/pkgs/r/noarch
  - https://repo.anaconda.com/pkgs/msys2/win-64
  - https://repo.anaconda.com/pkgs/msys2/noarch

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.
```

解决办法其实人家在报错中已经说了：

```bash
To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.
```

你需要去 https://anaconda.org 这个网址，在上方的搜索条上搜索你要安装这个包的其他channel，下边展示一下如何找igraph的其他channel
首先进入上述网址，你可以在上方看到搜索条：

![大多数公共软件包都可以不登陆直接搜索](https://img-blog.csdnimg.cn/20201113095745194.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTU1MjU2Mg==,size_16,color_FFFFFF,t_70#pic_center)

我这里搜索igraph，会出现所有包名中包含“igraph”字段的包：

![点击想要的加粗绿色包名就可以查找详细信息](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTU1MjU2Mg==,size_16,color_FFFFFF,t_70-20220314122513860.png)

接着在你的命令行窗口或Anaconda Prompt窗口对应的路径下运行页面中提供的任意一条命令即可。

![运行任意一条命令](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTU1MjU2Mg==,size_16,color_FFFFFF,t_70-20220314122534639.png)

#### 方法三：进入annaconda网站利用包的安装包安装

如果上述这些命令经过一一尝试都无效，那只有下载该python包对应的本地“***.bz2”本地文件，然后利用annaconda进行本地安装，需要点击上图的file，下载本机环境下对应的安装包：

![点击你所需要的安装包名，网页会自动下载](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTU1MjU2Mg==,size_16,color_FFFFFF,t_70-20220314122648557.png)



把下载好的“python-igraph-0.8.3-py38h0d6bca7_2.tar.bz2”这个安装包放到anaconda存放包的目录下，如:

```sh
D/anaconda3/pkgs/~
```

然后执行命令：

```sh
  conda install --use-local  python-igraph-0.8.3-py38h0d6bca7_2.tar.bz2
```

即可完成安装。（bz2前的包名根据你所需要的包而不同，“python-igraph-0.8.3-py38h0d6bca7_2.tar.bz2”是我所安装的igraph）

### 使用pip安装包

→ 使用场景

当使用conda install无法进行安装时，可以使用pip进行安装。例如：see包。

→ 命令

```sh
pip install <package_name>
```

注意1：<package_name>为指定安装包的名称。包名两边不加尖括号“<>”。

如：`pip install see`即安装see包。

注意2：

使用`pip`安装前请确认是否在虚拟环境中，否则安装的包将装在全局中

可以使用`which pip`命令查看pip是否是全局的pip命令，如果进入环境中，pip仍然为全局pip，可使用`python -m pip install <package>`命令进行虚拟环境内安装包

注意3：

pip只是包管理器，无法对环境进行管理。因此如果想在指定环境中使用pip进行安装包，则需要先切换到指定环境中，再使用pip命令安装包。

pip无法更新python，因为pip并不将python视为包。

pip可以安装一些conda无法安装的包；conda也可以安装一些pip无法安装的包。因此当使用一种命令无法安装包时，可以尝试用另一种命令。`卸载包时用安装包的命令下载，不要混用`，如用`pip`安装则用`pip`卸载

###  从[http://Anaconda.org](https://links.jianshu.com/go?to=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%3A%2F%2FAnaconda.org)安装包

→ 使用场景

当使用conda install无法进行安装时，可以考虑从[http://Anaconda.org](https://links.jianshu.com/go?to=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%3A%2F%2FAnaconda.org)中获取安装包的命令，并进行安装。

→ 注意

从[http://Anaconda.org](https://links.jianshu.com/go?to=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%3A%2F%2FAnaconda.org)安装包时，无需注册。

在当前环境中安装来自于[http://Anaconda.org](https://links.jianshu.com/go?to=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%3A%2F%2FAnaconda.org)的包时，需要通过输入要安装的包在[http://Anaconda.org](https://links.jianshu.com/go?to=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%3A%2F%2FAnaconda.org)中的路径作为获取途径（channel）。查询路径的方式如下：

在浏览器中输入：[http://anaconda.org](https://links.jianshu.com/go?to=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%3A%2F%2Fanaconda.org)，或直接点击[http://Anaconda.org](https://links.jianshu.com/go?to=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%3A%2F%2FAnaconda.org)

在新页面“Anaconda Cloud”的上方搜索框中输入要安装的包名，然后点击右边“放大镜”标志。

搜索结果中有数以千计的包可供选择，此时点击“Downloads”可根据下载量进行排序，最上面的为下载最多的包。（图中以搜索bottleneck包为例）

选择满足需求的包或下载量最多的包，点击包名。

复制“To install this package with conda run:”下方的命令，并粘贴在终端中执行。

完成安装。

## 4. 卸载包

① 卸载指定环境中的包

```sh
conda remove –name <env_name> <package_name>
```

注意：

`<env_name>`即卸载包所在指定环境的名称。环境名两边不加尖括号“<>”。

`<package_name>`即要卸载包的名称。包名两边不加尖括号“<>”。

例如：

```sh
conda remove –name python2 pandas #即卸载名为“python2”虚拟环境中的pandas包。
```

② 卸载当前环境中的包

```sh
conda remove <package_name>
```

注意：

`<package_name>`即要卸载包的名称。包名两边不加尖括号“<>”。

执行命令后即在当前环境中卸载指定包。

例如：

```sh
conda remove pandas # 即在当前环境中卸载pandas包。
```

## 5. 更新包

① 更新所有包

```sh
conda update –all
```

或

```sh
conda upgrade –all
```

> 建议：在安装Anaconda之后执行上述命令更新Anaconda中的所有包至最新版本，便于使用。在完全更新前必须确保网络给力不中断的前提下使用此命令，否则还是指定更新某个包。当然，为方便快捷激活、更新内置应用或包，Anaconda还支持GUI图形界面操作，安全起见，推荐使用

② 更新指定包

```sh
conda update <package_name>
```

或

```sh
conda upgrade <package_name>
```

注意：

`<package_name>`为指定更新的包名。包名两边不加尖括号“<>”。

更新多个指定包，则包名以空格隔开，向后排列。如：

```sh
conda update pandas numpy matplotlib #即更新pandas、numpy、matplotlib包。
```

## 清理（[conda](https://so.csdn.net/so/search?q=conda&spm=1001.2101.3001.7020)瘦身）

`conda clean`就可以轻松搞定！

第一步：通过`conda clean -p`来删除一些没用的包，这个命令会检查哪些包没有在包缓存中被硬依赖到其他地方，并删除它们。

第二步：通过`conda clean -t`可以删除conda保存下来的tar包。

```bash
conda clean -p      //删除没有用的包
conda clean -t      //删除tar包
conda clean -y --all //删除所有的安装包及cache
```

## 6.配置TUNA国内镜像

 在命令行下，输入： (后添加的通道优先级更高)

```sh
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/conda
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud//pytorch/
```

或直接把下面文字拷贝到 `~/.condarc`中 (越靠前的优先级越高)

```sh
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud//pytorch/
show_channel_urls: true
auto_activate_base: false  #关闭自动激活状态
```

 设置搜索时显示通道地址

```sh
conda config --set show_channel_urls yes
```

> 如果添加源之后，conda install 仍然出现下载速度慢的情况，这个时候可以直接将`.condarc`文件 里面的-default一行删去

> 如果发现更新后的版本反而更旧，是因为国内下载站没有及时更新官方最新版本，若需要官方最新版本的话就直接删除~/.condarc文件即可

### 查看是否添加上了源

```python3
conda config --show
```

### 查看已使用哪些镜像源

```python3
conda config --get channels
```

### 逐一删除镜像源

```text
conda config --remove channels 国内镜像源
```

> 例如：删除中科大源
> conda config --remove channels [Index of /anaconda/pkgs/free/](https://link.zhihu.com/?target=https%3A//mirrors.ustc.edu.cn/anaconda/pkgs/free/)
> conda config --remove channels [Index of /anaconda/pkgs/main/](https://link.zhihu.com/?target=https%3A//mirrors.ustc.edu.cn/anaconda/pkgs/main/)

## 修改默认虚拟环境安装位置

### 查看配置

```
conda config --show
```

`envs_dirs` 的第一项即为[虚拟环境](https://so.csdn.net/so/search?q=虚拟环境&spm=1001.2101.3001.7020)的默认位置-

### 修改配置

#### 添加 envs_dirs

```
conda config --add envs_dirs ~/.conda/envs
```

#### 删除 envs_dirs

如果需要删除配置虚拟环境安装路径，可以使用以下语句进行删除

```
conda config --remove envs_dirs ~/.conda/envs
```

除了使用 conda 指令修改 envs_dirs 配置外，还可以手动修改配置文件内容，实现配置修改，Windows 系统下 配置文件为 C:\Users\Username\.condarc，Linux 系统下为 ~/.condarc。可以直接编辑该 .condarc 文件，在其中添加配置：

> envs_dirs:
>
> ~/.conda/envs

# 迁移包

## 将Python环境里的包导出成txt文件

```sh
pip freeze > requirements.txt
```

## 根据requirements.txt里面的包和版本下载到本地保存

```sh
pip download -r requirements.txt -d <pack_path>
```

注意：

`<pack_path>`为指定的下载路径。包名两边不加尖括号“<>”。

提示：

如果使用默认pip源过慢，可指定国内源，如：

```sh
pip download -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt -d packs
```

## 不通过网络，直接通过本地包进行安装

这里需要说明一下，我这边是**在目的机器上也安装了Anaconda，同时创建了一个虚拟环境，切换到虚拟环境之后，再执行下面的语句**，需要自己根据实际情况稍微变通。

```sh
pip install --no-index --find-links=<pack_path> -r requirements.txt
```

注意：

`<pack_path>`为本地包路径。包名两边不加尖括号“<>”。

# 可能会碰到的问题

## 在执行`pip freeze > requirements.txt`时，碰到以下问题：

```bash
ERROR: Could not find a version that satisfies the requirement nvidia-ml-py==375.53.1 (from -r requirements.txt (line 61)) (from versions: 1.0, 2.285.1, 3.295.0, 4.304.2, 4.304.3, 4.304.4, 6.340.0, 7.346.0, 7.352.0, 10.418.84, 375.53)
ERROR: No matching distribution found for nvidia-ml-py==375.53.1 (from -r requirements.txt (line 61))
```

**原因：**
你需要的这个包太老了，导致网络上下载不了，所以需要重新安装一下这个包的最新版本
**解决方法：**
到https://pypi.org/project/，去搜索一下你需要的包，然后重新安装一下、

## 明明可以通过`pip install <package_names>`是正常的但是`pip download <package_names>`时却提示`No matching distribution found for <package_names>`

同时终端提示一下内容：

~~~shell
WARNING: The repository located at pypi.douban.com is not a trusted or secure host and is being ignored. If this repository is available via HTTPS we recommend you use HTTPS instead, otherwise you may silenc

e this warning and allow it anyway with '--trusted-host pypi.douban.com'.

ERROR: Could not find a version that satisfies the requirement  <package_names> (from versions: none)

ERROR: No matching distribution found for  <package_names>
~~~

**原因一：**

配置的`pip源`不是受信任的主机，所以在下载的时候忽略了该源

**解决办法：**

在执行命令后面添加 `--trusted-host <pip源地址>`就可以正常下载了，如：

```sh
pip dwonload pytest -d pack --trusted-host mirrors.aliyun.com
```

> ps ：--trusted-host pypi.douban.com 这是为了获得ssl证书的认证
>
> 常见pip镜像源（国内源）
> 	清华：https://pypi.tuna.tsinghua.edu.cn/simple
> 	阿里云：http://mirrors.aliyun.com/pypi/simple/
> 	中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
> 	华中理工大学：http://pypi.hustunique.com/
> 	山东理工大学：http://pypi.sdutlinux.org/
> 	豆瓣：http://pypi.douban.com/simple/

**原因二：**

没有提供符合条件的二进制包

**解决办法：**

使用非二进制包安装 --no-binary=:all: <package_name>

```
pip download --no-binary=:all: tornado==6.0 -d pkg/
```

**原因三：**

pip的版本过低，需要升级一下，可以执行以下命令进行尝试

**解决办法：**

更新pip版本

```
 python -m pip install --upgrade pip
```

**原因四：**

检查下是否开启代理或者VPN，将其关闭再使用国内镜像进行尝试看看是否可以解决，我这边就是代理开启导致网络太慢而报错的。

**解决办法：**

关闭VPN



## pytorch下载不了

```sh
ERROR: Could not find a version that satisfies the requirement torch==1.1.0 (from -r requirements.txt (line 12)) (from versions: 0.1.2, 0.1.2.post1, 0.1.2.post2)
ERROR: No matching distribution found for torch==1.1.0 (from -r requirements.txt (line 12))
```

原因：
pytorch比较麻烦，通过清华源，或者pip源下载不到，需要到官网下载
解决方法：
[Pytorch官网下载最新版](https://pytorch.org/)
[Pytorch老版本下载页面](https://pytorch.org/get-started/previous-versions/)
例如，我想下载pytorch==1.1.0 windows版本，我就需要在[Pytorch老版本下载页面](https://pytorch.org/get-started/previous-versions/)这个页面里，找到pytorch 1.1.0，拉到windows这一块，这里需要根据你的CUDA版本选择，我的版本是CUDA 9.0，所以我会在https://download.pytorch.org/whl/cu90/torch_stable.html这个页面里面找到whl下载。

![在这里插入图片描述](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpY2hhbzA2Mjc=,size_16,color_FFFFFF,t_70.png)

![在这里插入图片描述](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpY2hhbzA2Mjc=,size_16,color_FFFFFF,t_70-20220313220916377.png)



## 另一台无网络的服务器没有网络，怎么创建的虚拟环境呢

1）下载好Anaconda，然后复制过去安装，用anaconda的base环境。

2）带一个无线网卡插上去，然后连接手机热点，用自己的流量跑



## 安装或卸载anaconda 后打不开cmd

打开注册表，Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Command Processor，删除 AutoRun 项



## 下载时Solving environment: failed with initial frozen solve. Retrying with flexible solve.PackagesNotFoundError

检查镜像源
虽然上述博客的解决方案没用，但是更新命令收下了。

更新conda到最新版本：`conda update -n base conda`
再查一下conda版本：`conda -V`
第二次更新conda到最新版本：`conda update -n base conda`
第二次很重要！！！
更新完后再查一下conda版本：`conda -V`
然后执行：`conda update --all`



## ModuleNotFoundError … No module named ‘torch’

检查版本是否正确，如64位下载64位Anaconda。我把之前的32为卸载了重新装了64位的就没有问题了。



### anaconda或conda不是内部命令

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190624104613684.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3poYXl1c2h1aQ==,size_16,color_FFFFFF,t_70)

添加上图环境变量即可

### 更改 Python 的 pip install 默认安装依赖路径

[更改 Python 的 pip install 默认安装依赖路径](https://blog.csdn.net/mukvintt/article/details/80908951) https://blog.csdn.net/mukvintt/article/details/80908951

### 改变conda虚拟环境的默认路径

[改变conda虚拟环境的默认路径](https://blog.csdn.net/qq_36455412/article/details/125347552) https://blog.csdn.net/qq_36455412/article/details/125347552

1)首先，找到用户目录下的.condarc文件（C:\Users\username）。

2)打开.condarc文件之后，添加或修改.condarc 中的 env_dirs 设置环境路径，按顺序第⼀个路径作为默认存储路径，搜索环境按先后顺序在各⽬录中查找。直接在.condarc添加：

```txt
envs_dirs:
  - D:\Anaconda3\envs #你想要存储的路径
```

