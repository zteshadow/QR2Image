# QR2Image
扫描二维码获取图片, 微信小程序的客户端和服务端

## 1. http服务器on Google Cloud Platform

**1.在Debian服务器上面Flask绑定80端口, 提示"permission denied"**
解决: 不能绑定80端口, 可以使用8080端口, 然后再配置redirect

sudo /sbin/iptables -A PREROUTING -t nat -p tcp --dport 80 -j REDIRECT --to-port 8080

再把443端口也重定向到8080端口:
sudo /sbin/iptables -A PREROUTING -t nat -p tcp --dport 443 -j REDIRECT --to-port 8080

**2.'connection refused'**

app.run添加host='0.0.0.0'参数


##2. Flask搭建HTTPS服务器

**1.安装pyOpenSSL失败**

需要升级pip: 

python -m pip install --upgrade pip

需要安装开发环境: 

sudo apt-get install build-essential

sudo apt-get install python3-dev

参考: http://www.jianshu.com/p/109cc43b564a

##3.服务器证书无效


**1. 用自带证书**

开始的时候使用pyOpenSSL自带的安全证书: ssl_context='adhoc'会有"服务器证书无效"的提示, 于是决定自己配置证书

参考:参考: http://www.jianshu.com/p/109cc43b564a

**2. 自己配置证书**

注意要填写自己的域名, 否则"证书与域名匹配"这一项验证不通过, CN: www.meandlife.net, 然而还是无法通过腾讯的验证, 考虑找免费的认证.

参考: http://www.jianshu.com/p/109cc43b564a


**3. 找免费的证书**

Let's Encrypt 

参考:https://foofish.net/https-free-for-lets-encrypt.html

免费证书也无法通过腾讯的认证

**4. 用腾讯的SSL证书**

需要实名认证, 注意在验证域名的归属性上有2种方法, 一种是写文件, 另外一种是手动解析的方式, 手动给服务器添加一条TXT解析规则, 比较方便.








