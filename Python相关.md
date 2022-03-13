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

使用方法很简单，直接 -i 加 url 即可！如下：

```sh
pip install web.py -i http://pypi.douban.com/simple
```

如果有如下报错：

![img](https://gitee.com/ming-xiangyu/Imageshack/raw/master/img/1005188-20160824100208198-524213286.png)

请使用命令：

```sh
pip install web.py -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```

