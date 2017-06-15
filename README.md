# QR2Image
扫描二维码获取图片, 微信小程序的客户端和服务端

## 1. http服务器on Google Cloud Platform

**1.在Debian服务器上面Flask绑定80端口, 提示"permission denied"**
解决: 不能绑定80端口, 可以使用8080端口, 然后再配置redirect

sudo iptables -A PREROUTING -t nat -p tcp --dport 80 -j REDIRECT --to-port 8080

**2.'connection refused'**

app.run添加host='0.0.0.0'参数





