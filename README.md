# P 站非会员查看人气作品  

这个项目来源于我的一篇文章 [缺手机壁纸？来看看：也来看看](https://zhuanlan.zhihu.com/p/27466844) 下面的一条评论  

![](https://github.com/chenjiandongx/pixiv/blob/master/images/pixiv_5.png)  

其实一开始我是不知道 P 站是什么  

![](https://github.com/chenjiandongx/pixiv/blob/master/images/pixiv_6.jpg)  

某度了一下，原来是日本一个插画网站，但是这个网站看人气作品是要会员的。  

![](https://github.com/chenjiandongx/pixiv/blob/master/images/pixiv_2.png)  

然后我就又有个大胆的想法了，把插图的的连接和 star 数爬取下来，然后进行排序，这样就可以看到人气高的作品了。  

![](https://github.com/chenjiandongx/pixiv/blob/master/images/pixiv_7.jpg)  

第一次爬取网站内容，发现没有插图内容，应该是要保持登录状态才行。为此我注册了个账号，目的是为了获取 cookies。F12 获取 cookies  

![](https://github.com/chenjiandongx/pixiv/blob/master/images/pixiv_1.png)  

将 cookies 保存在项目下的 cookies.txt 文件里。在代码中组装 cookies 内容  
```python
def cookies(self):
    with open("cookies.txt", 'r') as f:
        _cookies = {}
        for row in f.read().split(';'):
            k, v = row.strip().split('=', 1)
            _cookies[k] = v
        return _cookie
```

测试一下，爬取 'summer' 关键词前 500 页信息。  

```python
urls = get_urls("summer", 500)
```   

效果如下

![](https://github.com/chenjiandongx/pixiv/blob/master/images/pixiv_3.png)  

点击排第一的连接  

![](https://github.com/chenjiandongx/pixiv/blob/master/images/pixiv_4.png)  

诚不欺我，确实高人气  
不过这个单线程版本（pixiv.py）爬取太多页的话速度有点慢，所以又写了个多线程版本的（pixiv_.py），速度蹭蹭就上去了。 

> 技术本身是无罪的。   —— 原快播CEO王欣  

当然还是希望有能力的同学支持下这个网站，充个会员。但是，我！就！不！  
