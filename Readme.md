Multiple-vendors-RCE.py是我自己写的一个批量漏洞检测脚本，主要检测多个产商安全产品的命令执行漏洞

受影响的产商

```
H3C-下一代防火墙
安恒信息-明御安全网关
MAiPU-安全网关
D_Link-下一代防火墙
HUAWEI-公司产品
迈普通信技术股份有限公司安全网关
博达通信-下一代防火墙
任天行网络安全管理系统\安全审计系统
安博通应用网关
烽火网络安全审计
瑞斯康达科技发展股份有限公司安全路由器
任子行网络安全审计系统
绿盟安全审计系统
深圳市鑫塔科技有限公司第二代防火墙
```

脚本使用方法

```
pocsuite -r ./Multiple-vendors-RCE.py -u ip
pocsuite -r ./Multiple-vendors-RCE.py -f url_file
```

