# 更换pip源

> 国内的pip源

阿里云

```text
 http://mirrors.aliyun.com/pypi/simple/
```

中国科技大学

```sh
https://pypi.mirrors.ustc.edu.cn/simple/
```

豆瓣(douban) 

```sh
http://pypi.douban.com/simple/ 
```

清华大学 

```sh
https://pypi.tuna.tsinghua.edu.cn/simple/
```

中国科学技术大学 

```sh
http://pypi.mirrors.ustc.edu.cn/simple/
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

这样在使用pip来安装时，会默认调用该镜像。

也可以使用读入文件进行安装：

```python
#!/usr/bin/python
  
import os
  
package = raw_input("Please input the package which you want to install!\n")
command = "pip install %s -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn" % package
os.system(command)
```

# Python相关

查看Python安装位置

```python3
where python
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
easy_install Pillow 
```

## pip安装包管理

```sh
pip list #列出当前缓存的包
pip purge #清除缓存
pip remove #删除对应的缓存
pip help #帮助
pip install xxx #安装xxx包
pip uninstall xxx #删除xxx包
pip show xxx #展示指定的已安装的xxx包
pip check xxx #检查xxx包的依赖是否合适
```

