[TOC]

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

注意：如果出现错误信息，则需核实是否出现以下情况：

使用的用户是否是安装Anaconda时的账户。

是否在`安装Anaconda之后重启了终端。`

## **2. 更新conda至最新版本**

```shell
conda update conda
```

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

控制面板 → 添加或删除程序 → 选择“Python X.X (Anaconda)” → 点击“删除程序”

注意：

Python X.X：即Python的版本，如：Python 3.6。

Windows 10的删除有所不同。

# **管理环境**

接下来均是以命令行模式进行介绍，Windows用户请打开“Anaconda Prompt”；macOS和Linux用户请打开“Terminal”（“终端”）进行操作。

## 1.创建新环境

```sh
conda create –name <env_name> <package_names>
```

注意：

`<env_name>`即创建的环境名。建议以英文命名，且不加空格，名称两边不加尖括号“<>”。

`<package_names>`即安装在环境中的包名。名称两边不加尖括号“<>”。

如果要安装指定的版本号，则只需要在包名后面以=和版本号的形式执行。如：

```sh
conda create –name python2 python=2.7 #即创建一个名为“python2”的环境，环境中安装版本为2.7的python。
```

如果要在新创建的环境中创建多个包，则直接在`<package_names>`后以空格隔开，添加多个包名即可。如：

```sh
conda create -n python3 python=3.5 numpy pandas #即创建一个名为“python3”的环境，环境中安装版本为3.5的python，同时也安装了numpy和pandas。
```

–name同样可以替换为-n。

提示：默认情况下，新创建的环境将会被保存在/Users/<user_name>/anaconda3/env目录下，其中，`<user_name>`为当前用户的用户名。

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
conda remove –name <env_name> –all
```

注意：`<env_name>`为被删除环境的名称。环境名两边不加尖括号“<>”。

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

① 在指定环境中安装包

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

② 在当前环境中安装包

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

③ 使用pip安装包

→ 使用场景

当使用conda install无法进行安装时，可以使用pip进行安装。例如：see包。

→ 命令

```sh
pip install <package_name>
```

注意：<package_name>为指定安装包的名称。包名两边不加尖括号“<>”。

如：`pip install see`即安装see包。

→ 注意

pip只是包管理器，无法对环境进行管理。因此如果想在指定环境中使用pip进行安装包，则需要先切换到指定环境中，再使用pip命令安装包。

pip无法更新python，因为pip并不将python视为包。

pip可以安装一些conda无法安装的包；conda也可以安装一些pip无法安装的包。因此当使用一种命令无法安装包时，可以尝试用另一种命令。

④ 从[http://Anaconda.org](https://links.jianshu.com/go?to=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%3A%2F%2FAnaconda.org)安装包

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
conda remove –name python2 pandas #即卸载名为“python2”中的pandas包。
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

## 6.配置TUNA国内镜像

1） 在命令行下，输入：

```sh
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/ 
```

或

```sh
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/conda
```

 设置搜索时显示通道地址

```sh
conda config --set show_channel_urls yes
```

> 如果添加源之后，conda install 仍然出现下载速度慢的情况，这个时候可以直接将`.condarc`文件 里面的-default一行删去

> 如果发现更新后的版本反而更旧，是因为国内下载站没有及时更新官方最新版本，若需要官方最新版本的话就直接删除~/.condarc文件即可

查看是否添加上了源

```python3
conda config --show
```

查看已使用哪些镜像源

```python3
conda config --get channels
```

逐一删除镜像源

```text
conda config --remove channels 国内镜像源
```

> 例如：删除中科大源
> conda config --remove channels [Index of /anaconda/pkgs/free/](https://link.zhihu.com/?target=https%3A//mirrors.ustc.edu.cn/anaconda/pkgs/free/)
> conda config --remove channels [Index of /anaconda/pkgs/main/](https://link.zhihu.com/?target=https%3A//mirrors.ustc.edu.cn/anaconda/pkgs/main/)

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

## 不通过网络，直接通过本地包进行安装

这里需要说明一下，我这边是**在目的机器上也安装了Anaconda，同时创建了一个虚拟环境，切换到虚拟环境之后，再执行下面的语句**，需要自己根据实际情况稍微变通。

```sh
pip install --no-index --find-links=<pack_path> -r requirements.txt
```

