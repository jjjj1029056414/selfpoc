脚本使用方法

```
pocsuite -r ./Multiple-vendors-RCE.py -u ip
pocsuite -r ./Multiple-vendors-RCE.py -f url_file
```



Multiple-vendors-RCE.py检测多个产商安全产品的命令执行漏洞

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
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
Education_cloud_platform_upload.py主要检测某教育视频云平台前台某接口文件上传漏洞
```
Fofa搜索语句
```
body="Copyright © 2005-2018 广州市奥威亚电子科技有限公司"

body="/Upload/DomainInfo/MaxAVALogo.png"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
superdata-upload.py主要检测速达软件全系产品的任意文件上传漏洞

Fofa搜索语句
```
app="速达软件-公司产品"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
dahua-DSS-struts2-045.py检测大华DSS的s2-45漏洞

Fofa搜索语句
```
body="/portal/include/script/dahuaDefined/headCommon.js?type=index"&&title="DSS"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
yunbaoan-fashjson.py检测云宝安-云匣子fastjson命令执行

Fofa搜索语句
```
app="云安宝-云匣子"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
RG-UAC-RCE.py检测锐捷RG-UAC应用网关-前台RCE漏洞

Fofa搜索语句
```
app="Ruijie-RG-UAC"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
yongyouu8-cloud-upload.py检测用友U8-Cloud upload任意文件上传漏洞
能检测出来洞，但上传需要登录身份认证

Fofa搜索语句
```
app="用友-U8-Cloud"&& country="CN"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
haoshitong-fileread.py检测好视通视频会议任意文件读取漏洞
Fofa搜索语句
```
app="好视通-视频会议"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
yongyouNC-upload.py检测用友NC任意文件上传漏洞
Fofa搜索语句
```
app="用友-NC-Cloud"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
yushi-isc-logreport-rce.py检测浙江宇视 isc LogReport.php 远程命令执行漏洞
Fofa搜索语句
```
body="Alarm" && country="CN" && body="白牌定制"
```

----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
huawei-Auth-Http-fileread.py检测华为Auth-HTTP服务器任意文件读取漏洞

Fofa搜索语句
```
server="Huawei Auth-Http Server 1.0"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
JieLink_zhineng_sql.py检测某智能终端操作平台前台通用SQL注入漏洞

Fofa搜索语句
```
title="JieLink+智能终端操作平台"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
yongyou-ufida-nc-unauthorized.py检测某友UFIDA NC系统某接口未授权访问漏洞
Fofa搜索语句
```
app="用友-UFIDA-NC"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
tongdaOA-Authenticatio-bypass.py检测通达OA header身份认证绕过漏洞
Fofa搜索语句
```
title="office Anywhere" && product="TDXK-通达OA"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
fanwei-yunqiaoe-bridge-sql.py检测泛微云桥 e-Bridge SQL注入漏洞
Fofa搜索语句
```
app="泛微-云桥e-Bridge"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
iDocview-fileread.py检测iDocview某接口任意文件读取漏洞
Fofa搜索语句
```
title="I Doc View"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
zhedaente-upload.py检测浙大恩特客户资源管理系统CustomerAction.entphone;.js文件上传漏洞
Fofa搜索语句
```
title="欢迎使用浙大恩特客户资源管理系统"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
wangshen-SecGate3600-information-leakage.py检测网神SecGate3600防火墙敏感信息泄露漏洞
Fofa搜索语句
```
"sec_gate_image/button_normal.gif"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
milesight-vpn-fileread.py检测milesight vpn 任意文件读取漏洞
Fofa搜索语句
```
body="glyphicon-remove" && body="$randdt;" && country="CN"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
livebos-crm-scriptvariable-rce.py检测livebos crm scriptvariable.jsp 远程命令执行漏洞
Fofa搜索语句
```
body="/react/browser/loginBackground.png"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
idocview-doc-upload-fileread.py检测iDocview doc/upload接口存在任意文件读取漏洞
Fofa搜索语句
```
title="I Doc View" && country="CN"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
yongyouu8-CRM-fileread.py检测某友CRM系统某接口存在任意文件读取漏洞
Hunter搜索语句
```
app.name="用友 CRM"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
TurboMail-view-fileread.py检测TurboMail viewfile 文件读取漏洞
Fofa搜索语句
```
body="maintlogin.jsp" && body="/mailmain?type=logout"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
yisaitong-fileread.py检测亿赛通电子文档安全管理系统某接口存在任意文件读取漏洞
Fofa搜索语句
```
"CDGServer3/index.jsp" && country="CN"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
datang-dianxinAC-information-leakage.py检测大唐电信AC集中管理平台敏感信息泄漏漏洞
Fofa搜索语句
```
app="大唐电信AC集中管理平台" && fid="gmqJFLGz7L/7TdQxUJFBXQ=="
```
