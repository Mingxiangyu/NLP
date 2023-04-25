[TOC]

# Python相关

查看Python安装位置

```python3
which python
```

查看Python的版本

```python3
python -V
```

# PIP相关

## pip数据源管理

```sh
#显示目前pip的数据源有哪些
pip config list
pip config list --[user|global] # 列出用户|全局的设置
pip config get global.index-url # 得到这key对应的value 如：https://mirrors.aliyun.com/pypi/simple/

# 添加
pip config set key value
#添加数据源：例如, 添加USTC中科大的源：
pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple
#添加全局使用该数据源
pip config set global.trusted-host https://mirrors.ustc.edu.cn/pypi/web/simple

# 删除
pip config unset key
# 例如
conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

#搜索
pip search flask  #搜素flask安装包

# 升级pip
pip install pip -U
```

## 更换pip源

> 国内的pip源

```bash
http://mirrors.aliyun.com/pypi/simple/ #阿里云
https://pypi.mirrors.ustc.edu.cn/simple/ #中国科技大学
http://pypi.douban.com/simple/  #豆瓣(douban) 
https://pypi.tuna.tsinghua.edu.cn/simple/ #清华大学 
http://pypi.mirrors.ustc.edu.cn/simple/ #中国科学技术大学 
```

## （临时配置）使用方法很简单，直接 -i 加 url 即可！如下：

```sh
pip install web.py -i http://pypi.douban.com/simple
```

如果有如下报错：

![img](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/1005188-20160824100208198-524213286.png)

请使用命令：

```sh
pip install web.py -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```

## 配置成默认源

需要创建或修改配置文件（一般都是创建），

linux的文件在`~/.pip/pip.conf`，

windows在`%HOMEPATH%\pip\pip.ini`，

修改内容为：

```bash
[global]
index-url = http://pypi.douban.com/simple
[install]
trusted-host=pypi.douban.com
```

或者

 ```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
 ```

这样在使用pip来安装时，会默认调用该镜像。

也可以使用读入文件进行安装：

```python
#!/usr/bin/python
  
import os
  
package = raw_input("Please input the package which you want to install!\n")
command = "pip install %s -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn" % package
os.system(command)
```

## 修复pip

```python3
python -m ensurepip # 修复pip
python -m pip install --upgrade pip  # 更新pip
```

**问题：**采用pip install pillow安装pillow，并提示成功安装，但是`from PIL import Image`提示如下错误

> **ModuleNotFoundError: No module named 'PIL'**

**解决：**先卸载，后重装。

```python3
pip uninstall pillow 
pip install pillow  
```

## pip安装包管理

```sh
pip list #列出当前缓存的包
pip purge #清除缓存
pip remove #删除对应的缓存
pip help #帮助
pip install xxx #安装xxx包
pip install ... --no-cache-dir #跳过缓存
pip uninstall xxx #删除xxx包
pip show xxx #展示指定的已安装的xxx包
pip check xxx #检查xxx包的依赖是否合适
```

查看Python安装位置

```python3
which pip
```

如果pip安装时出现问题并且看不到报错，可以尝试以下命令（debug形式运行install）

```python
pip install -vvv <package_name>   #package_name为你想安装的包名称，不带<>
```

## 清除缓存

### linux缓存所在文件夹

```bash
cd ~/.cache/pip
sudo rm -rf * #清除所有缓存
```

### win缓存默认所在文件夹

```bash
C:\Users\<user_name>\AppData\Local\pip\cache
```

## 用pip生成当前环境下的requirements文件

##### 当前使用全局环境模块导出

```bash
pip freeze > requirements.txt
```

- 问题

在 `conda` 沙箱环境中使用 `pip freeze > requirements.txt` 命令导出已安装的模块，其中部分模块显示了 `@ file:///...`，而不是具体的版本号，

此时，如果我们直接在其他机器上边使用 pip install -r requirements.txt 安装模块时，就会遇到如下错误：

```bash
ERROR: Could not install packages due to an EnvironmentError: [Errno 2] No such
file or directory: 'C:\\ci\\cffi_1600699250966\\work'
```

这是 pip 安装软件包的一种特殊语法（自19.1开始受支持）[PEP404](https://www.python.org/dev/peps/pep-0440/#direct-references)，
但是该此种路径取决于环境，`file:///URL` 仅在本地文件系统上可用，你不能将生成的 `requirements.txt` 文件提供给其他人使用

[解决](https://blog.csdn.net/qq_36078992/article/details/109435000)

当你遇到此类问题时，可以暂时考虑使用如下命令生成 `requirements.txt` 文件

```bash
pip list --format=freeze > requirements.txt
```

> 使用上述命令导出的文件中，会包含如下几个包：`distribute`，`pip`，`setuptools`，`wheel`，建议手动删除！

##### [当前项目使用模块导出](https://blog.csdn.net/Xuanze_xx/article/details/107948638)

使用pipreqs，这种方法会自动检测项目中调用的库，然后写进requirements.txt

```bash
#安装pipreqs
pip install pipreqs

#终端输入以下命令
pipreqs ./
```

- 问题1

当项目所在文件夹中已有requirement.txt时，会提示

```sh
WARNING: requirements.txt already exists, use --force to overwrite it
```

解决办法：这时需要将输入命令改为以下，即可更新已经存在的requirement.txt文件了。

```sh
pipreqs --force ./
```

- 问题2

有可能会出现如下所示的报错

```bash
UnicodeDecodeError: 'gbk' codec can't decode byte exae in position 168: illegal multibyte sequence
```

解决办法：输入一下命令即可成功

```sh
pipreqs ./ --encoding=utf-8
```



## 用pip安装当前环境下的requirements文件

```sh
pip install -r requirements.txt
```

# dockerFile

构建dockerfile

~~~dockerfile
FROM python:3.6
ENV PATH /usr/local/bin:$PATH
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
CMD python3 ab.py
~~~

dockerFile说明
~~~shell
FROM　　基础镜像，当前新镜像是基于哪个镜像的
MAINTAINER　　镜像维护者的姓名和邮箱地址
RUN　　容器构建时需要运行的命令
EXPOSE　　当前容器对外暴露出的端口
WORKDIR　　指定在创建容器后，终端默认登录进来的工作目录，一个落脚点
ENV　　用来在构建镜像过程中设置环境变量
ADD　　将宿主机目录下的文件拷贝进镜像且ADD命令会自动处理URL和解压tar压缩包
COPY　　类似ADD，拷贝文件和目录到镜像中。将从构建上下文目录中<源路径>的文件/目录复制到新的一层的镜像内的<目标路径>位置
VOLUME　　容器数据卷，用于数据保存和持久化工作
CMD　　指定一个容器启动时要运行的命令。Dockerfile中可以有多个CMD指令，但只要最后一个生效，CMD会被docker run之后的参数替换
ENTRYPOINT　　指定一个容器启动时要运行的命令。ENTRYPOINT的目的和CMD一样，都是在指定容器启动程序及参数
ONBUILD　　当构建一个被继承的Dockerfile时运行命令，父镜像在被子继承后父镜像的onbuild被触发
~~~

## 破解五秒盾

~~~dockerfile
docker run -d --name=flaresolverr -p 8191:8191 -e LOG_LEVEL=info --restart unless-stopped ghcr.io/flaresolverr/flaresolverr:latest
~~~



# 常见问题

- 如果用pip提示找不到相关库，可以切换下用conda指令安装；

- 如果用某个源下载速度慢，即可多切换下不同的镜像源试试，比如有时候用清华源只有10k，换个豆瓣源有2M多；

- 如果提示连接超时，代理设置有问题的，可以检查下自己的vpn是否开启了全局，可改成PAC模式；

- 如果出现“conda Collecting package metadata (current_repodata.json): failed”，说明当前设置的镜像源可能失效，可直接通过下面指令依次执行后，再重新安装你需要的包：

- ```sh
  conda config --remove-key channels
  conda update conda
  conda update --all
  conda config --add channels conda-forge
  conda config --set channel_priority flexible
  ```

