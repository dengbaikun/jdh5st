<h1>京东h5st 4.4算法分析 js_security_v3_0.1.8.js js_security_v3_main_0.1.8.js</h1>
京东h5st 4.4算法分析 仅供学习

![这里请求获取商品的预约以及其他信息需要h5st](img/9c1d21c6078d4de1bcfd55b6192d8fa3.png)
这里请求获取商品的预约以及其他信息需要h5st （stock.js）
现在看下h5st如何获取
![在这里插入图片描述](img/ddf67729c0214d0ea58eac856068d273.png)
此处会vm加载一个js文件 js_security_v3_main_0.1.8.js 获取h5st的所有算法在里面

下面讲解几个关键位置
![在这里插入图片描述](img/b94ba79f338f497794d60f543c210966.png)
这里是获取_fingerprint 随机生成码  这里要把算法逆向一下  这里不是任意随机生成（本人亲测了，只能把算法给逆向出来）
![在这里插入图片描述](img/faec5f99c73b4d878e4c627bebaea0e5.png)

这里的算法是获取 _fingerprint 用于获取algo 获取token 以及匿名js 方法 用于计算sign值
![在这里插入图片描述](img/fe24c1a51c264648b10ae2726bb3f256.png)
这里就是环境参数生成值然后请求algo
![在这里插入图片描述](img/d118a496277548dfb099441c0640efd7.png)
![在这里插入图片描述](img/8968014cd9bc4659b59d7b9dadb1d57f.png)
h5st
![在这里插入图片描述](img/20389c3c87974d519d3b61365e8f24df.png)
这里是环境参数加密
![在这里插入图片描述](img/5ace5c4c38d540239884c64148363581.png)
![在这里插入图片描述](img/5c7555af52a94e0486bbbe7376e02509.png)
这里的key生成就是我们刚刚获取algo函数

![在这里插入图片描述](img/170fd191a2014fb48da46c2e31863acf.png)
结果图
![在这里插入图片描述](img/2cfc69b728cf49b9a3d13362cbc72188.png)
请给我一个⭐ 感谢大家 fp做了优化版 方便大家理解 也可以想我那样把逆向扣写所需要的代码
会进行答疑



(jd_h5st.py)  python式 主文件入口 
python version 3.8
pip install -r requirements.txt
需求安装nodejs环境 18v-20v npm install crypto-js --save


下面是有个小伙提出 能否实现金豆签到 是可以的 下面是成功逆向了结果图 仅供学习 后面会放代码
https://jdbeantask-pro.pf.jd.com/
![在这里插入图片描述](img/jd金豆签到.png)
验证文件版本是 js_security_v3_0.1.7.js  大家对h5st这个已经成功了逆向了  可以自己实现一下金豆 如果成功基本上没有问题了 有问题可以提出来

增加了_defaultToken.js __genDefaultKey.js 代码跟3.18一样的  请留意js317文件 里面的参数变量可能会变 就是数组值


<h1>金豆签到4.4算法分析 js_security_v3_0.1.7.js </h1>

下面是gentk 和genkey 算法逆向
![在这里插入图片描述](js317/img/20240415133705.png)
![在这里插入图片描述](js317/img/20240415133725.png)
![在这里插入图片描述](js317/img/20240415133847.png)
![在这里插入图片描述](js317/img/20240415143449.png)
![在这里插入图片描述](js317/img/20240415143538.png)
![在这里插入图片描述](js317/img/20240415155640.png)
![在这里插入图片描述](js317/img/20240415162515.png)
![在这里插入图片描述](js317/img/20240415162524.png)
![在这里插入图片描述](js317/img/20240416102844.png)
![在这里插入图片描述](js317/img/20240416102857.png)
![在这里插入图片描述](js317/img/h5st.png)
![在这里插入图片描述](js317/img/jd金豆签到.png)


