Multiple_vendors_RCE.py是我自己写的一个批量漏洞检测脚本，主要检测多个产商安全产品的命令执行漏洞

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
Fofa搜索语句
```
body="/webui/images/default/default/alert_close.jpg"
```

脚本使用方法

```
pocsuite -r ./Multiple_vendors_RCE.py -u ip
pocsuite -r ./Multiple_vendors_RCE.py -f url_file
```
------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------
Education_cloud_platform_upload.py是我自己写的一个批量漏洞检测脚本，主要检测某教育视频云平台前台某接口文件上传漏洞
```
Fofa搜索语句
```
body="Copyright © 2005-2018 广州市奥威亚电子科技有限公司"

body="/Upload/DomainInfo/MaxAVALogo.png"
```

脚本使用方法

```
pocsuite -r ./Education_cloud_platform_upload.py -u ip

pocsuite -r ./Education_cloud_platform_upload -f url_file
```
