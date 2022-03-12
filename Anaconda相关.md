# **管理conda**

接下来均是以命令行模式进行介绍，Windows用户请打开“Anaconda Prompt”；macOS和Linux用户请打开“Terminal”（“终端”）进行操作。

## **1. 验证conda已被安装**

```shell
conda -V
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

**3. 查看conda帮助信息**

conda –help

或

conda -h

\4. 卸载conda

① Linux 或 macOS

rm -rf ~/anaconda2

或

rm -rf ~/anaconda3

即删除Anaconda的安装目录。根据安装的Anaconda版本选择相应的卸载命令。

**② Windows**

控制面板 → 添加或删除程序 → 选择“Python X.X (Anaconda)” → 点击“删除程序”

注意：

Python X.X：即Python的版本，如：Python 3.6。

Windows 10的删除有所不同。

**五、管理环境**

\0. 写在前面

接下来均是以命令行模式进行介绍，Windows用户请打开“Anaconda Prompt”；macOS和Linux用户请打开“Terminal”（“终端”）进行操作。

\1. 创建新环境

conda create –name <env_name> <package_names>

注意：

<env_name>即创建的环境名。建议以英文命名，且不加空格，名称两边不加尖括号“<>”。

<package_names>即安装在环境中的包名。名称两边不加尖括号“<>”。

如果要安装指定的版本号，则只需要在包名后面以=和版本号的形式执行。如：conda create –name python2 python=2.7，即创建一个名为“python2”的环境，环境中安装版本为2.7的python。

如果要在新创建的环境中创建多个包，则直接在<package_names>后以空格隔开，添加多个包名即可。如：conda create -n python3 python=3.5 numpy pandas，即创建一个名为“python3”的环境，环境中安装版本为3.5的python，同时也安装了numpy和pandas。

–name同样可以替换为-n。

提示：默认情况下，新创建的环境将会被保存在/Users/<user_name>/anaconda3/env目录下，其中，<user_name>为当前用户的用户名。

**2. 切换环境**

① Linux 或 macOS

source activate <env_name>

② Windows

activate <env_name>

③ 提示

如果创建环境后安装Python时没有指定Python的版本，那么将会安装与Anaconda版本相同的Python版本，即如果安装Anaconda第2版，则会自动安装Python 2.x；如果安装Anaconda第3版，则会自动安装Python 3.x。

当成功切换环境之后，在该行行首将以“(env_name)”或“[env_name]”开头。其中，“env_name”为切换到的环境名。如：在macOS系统中执行source active python2，即切换至名为“python2”的环境，则行首将会以(python2)开头。

**3. 退出环境至root**

① Linux 或 macOS

source deactivate

② Windows

deactivate

③ 提示

当执行退出当前环境，回到root环境命令后，原本行首以“(env_name)”或“[env_name]”开头的字符将不再显示。

4**. 显示已创建环境**

conda info –envs

或

conda info -e

或

conda env list

例如：

结果中星号“*”所在行即为当前所在环境。macOS系统中默认创建的环境名为“base”。

\5. 复制环境

conda create –name <new_env_name> –clone <copied_env_name>

注意：

<copied_env_name>即为被复制/克隆环境名。环境名两边不加尖括号“<>”。

<new_env_name>即为复制之后新环境的名称。环境名两边不加尖括号“<>”。

如：conda create –name py2 –clone python2，即为克隆名为“python2”的环境，克隆后的新环境名为“py2”。此时，环境中将同时存在“python2”和“py2”环境，且两个环境的配置相同。

\6. 删除环境

conda remove –name <env_name> –all

注意：<env_name>为被删除环境的名称。环境名两边不加尖括号“<>”。

**六、管理包**

\1. 查找可供安装的包版本

① 精确查找

conda search –full-name <package_full_name>

注意：

–full-name为精确查找的参数。

<package_full_name>是被查找包的全名。包名两边不加尖括号“<>”。

例如：conda search –full-name python即查找全名为“python”的包有哪些版本可供安装。

② 模糊查找

conda search <text>

注意：<text>是查找含有此字段的包名。此字段两边不加尖括号“<>”。

例如：conda search py即查找含有“py”字段的包，有哪些版本可供安装。

\2. 获取当前环境中已安装的包信息

conda list

执行上述命令后将在终端显示当前环境已安装包的包名及其版本号。

\3. 安装包

① 在指定环境中安装包

conda install –name <env_name> <package_name>

注意：

<env_name>即将包安装的指定环境名。环境名两边不加尖括号“<>”。

<package_name>即要安装的包名。包名两边不加尖括号“<>”。

例如：conda install –name python2 pandas即在名为“python2”的环境中安装pandas包。

② 在当前环境中安装包

conda install <package_name>

注意：

<package_name>即要安装的包名。包名两边不加尖括号“<>”。

执行命令后在当前环境中安装包。

例如：conda install pandas即在当前环境中安装pandas包。

③ 使用pip安装包

→ 使用场景

当使用conda install无法进行安装时，可以使用pip进行安装。例如：see包。

→ 命令

pip install <package_name>

注意：<package_name>为指定安装包的名称。包名两边不加尖括号“<>”。

如：pip install see即安装see包。

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

\4. 卸载包

① 卸载指定环境中的包

conda remove –name <env_name> <package_name>

注意：

<env_name>即卸载包所在指定环境的名称。环境名两边不加尖括号“<>”。

<package_name>即要卸载包的名称。包名两边不加尖括号“<>”。

例如：conda remove –name python2 pandas即卸载名为“python2”中的pandas包。

② 卸载当前环境中的包

conda remove <package_name>

注意：

<package_name>即要卸载包的名称。包名两边不加尖括号“<>”。

执行命令后即在当前环境中卸载指定包。

例如：conda remove pandas即在当前环境中卸载pandas包。

\5. 更新包

① 更新所有包

conda update –all

或

conda upgrade –all

建议：在安装Anaconda之后执行上述命令更新Anaconda中的所有包至最新版本，便于使用。

② 更新指定包

conda update <package_name>

或

conda upgrade <package_name>

注意：

<package_name>为指定更新的包名。包名两边不加尖括号“<>”。

更新多个指定包，则包名以空格隔开，向后排列。如：conda update pandas numpy matplotlib即更新pandas、numpy、matplotlib包。