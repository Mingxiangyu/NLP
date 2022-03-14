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

# 查看Python安装位置

```python3
where python
```

查看Python的版本

```python3
python -V
```

