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
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
mingfei-list-sql.py检测铭飞CMS cmscontentlist接口SQL注入
Fofa搜索语句
```
body="铭飞MCMS" || body="/mdiy/formData/save.do" || body="static/plugins/ms/1.0.0/ms.js"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
hongfanOA-iorepsavexml-upload.py检测红帆OA iorepsavexml.aspx文件上传漏洞
Fofa搜索语句
```
app="红帆-ioffice" || app="红帆-HFOffice"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
fanweiOA-xml-fileread.py检测泛微OA xmlrpcServlet接口任意文件读取漏洞
Fofa搜索语句
```
app="泛微-OA（e-cology）"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
kerong-fileread.py检测科荣AIO任意文件读取漏洞
Fofa搜索语句
```
body="changeAccount('8000')"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
haikang-fileread.py检测海康威视-综合安防管理平台-files-文件读取漏洞
Fofa搜索语句
```
app="HIKVISION-综合安防管理平台"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
office-web-365-fileread.py检测Office Web 365 任意文件读取漏洞
Fofa搜索语句
```
body="请输入furl参数" || header="OfficeWeb365" || banner="OfficeWeb365"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
rwx-CRM-smsdatalist-sql.py检测任我行CRM系统SmsDataList接口SQL注入漏洞
Fofa搜索语句
```
"欢迎使用任我行CRM"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
trx-topsec-cookie-rce.py检测天融信TOPSEC安全管理系统远程命令执行漏洞
Fofa搜索语句
```
title="Web User Login" && body="/cgi/maincgi.cgi?Url=VerifyCode"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
trx-topsec-static_convert-rce.py检测天融信TOPSEC static_convert 远程命令执行漏洞
Fofa搜索语句
```
app="天融信-上网行为管理系统"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
nc-actionhandlerservlet-unserialization.py检测用友 NC actionhandlerservlet 反序列化漏洞
Fofa搜索语句
```
app="用友-UFIDA-NC"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
nginxwebui-runcmd-rce.py检测nginxWebUI runCmd前台远程命令执行漏洞
Fofa搜索语句
```
app="nginxWebUI" && country="CN"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
jinhe-getattout-sql.py检测金和OA GetAttOut接口SQL注入漏洞
Fofa搜索语句
```
app="金和网络-金和OA" || body="/jc6/platform/sys/login"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
jinhe-jc6-upload.py检测金和OA jc6/servlet/Upload接口任意文件上传漏洞
Fofa搜索语句
```
app="金和网络-金和OA"||body="/jc6/platform/sys/login"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
yearning-front-fileread.py检测Yearning front 任意文件读取漏洞
Fofa搜索语句
```
app="Yearning"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
zdek-crmbasicaction-upload.py检测浙大恩特客户资源管理系统CrmBasicAction.entcrm接口存在任意文件上传漏洞
Fofa搜索语句
```
title="欢迎使用浙大恩特客户资源管理系统"||app="浙大恩特客户资源管理系统"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
kerongAIO-utilservlet-rce.py检测科荣AIO UtilServlet任意命令执行漏洞
Fofa搜索语句
```
body="changeAccount('8000')"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
ifair-fileread.py检测企语iFair协同管理系统getuploadimage.jsp接口任意文件读取漏洞
Fofa搜索语句
```
app="服务社-企语iFair"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
springboot-apiblade-user-sql.py检测SpringBlade export-user SQL 注入漏洞
Fofa搜索语句
```
body="https://bladex.vip" && country="CN"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
beijin-ucenter-rce.py检测北京亚鸿世纪互联网信息安全综合管理系统 ucenter命令执行漏洞
Fofa搜索语句
```
app="Atlassian-Confluence"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
atlassian-confluence-rce.py检测Atlassian Confluence 远程命令执行漏洞
Fofa搜索语句
```
app="Atlassian-Confluence"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
hikvision-files-fileread.py检测Hikvision综合安防管理平台files;.css接口存在任意文件读取漏洞
Fofa搜索语句
```
body="/portal/skin/isee/redblack/"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
edusoho-fileread.py检测EduSoho任意文件读取漏洞
Fofa搜索语句
```
title="Powered By EduSoho" || body="Powered by <a href=\"http://www.edusoho.com/\" target=\"_blank\">EduSoho" || (body="Powered By EduSoho" && body="var app")
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
likeshop-upload.py检测Likeshop任意文件上传漏洞
Fofa搜索语句
```
title="Likeshop"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
wanhu-text-fileread.py检测万户OA text2Html 任意文件读取漏洞
Fofa搜索语句
```
app="万户网络-ezOFFICE"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
yongyouU8-old.jsp-sql.py检测用友GRP-U8 forgetPassword_old.jspSQL注入漏洞
Fofa搜索语句
```
app="用友-GRP-U8"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
yisaitong-policyajax-sql.py检测亿赛通电子文档安全管理系统-policyajaxSQL注入漏洞
Fofa搜索语句
```
body="CDGServer3" || title="电子文档安全管理系统" || cert="esafenet" || body="/help/getEditionInfo.jsp"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
bangguanjiaCRM-ajax-upload.py检测帮管家 CRM ajax_upload文件上传漏洞
Fofa搜索语句
```
app="帮管客-CRM"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
bangguanjiaCRM-ajax-upload-chat.py检测帮管家 CRM ajax_upload_chat文件上传漏洞
Fofa搜索语句
```
app="帮管客-CRM"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
zdek-followaction-sql.py检测浙大恩特客户资源管理系统-FollowAction接口存在SQL注入漏洞
Fofa搜索语句
```
title="欢迎使用浙大恩特客户资源管理系统" || body="script/Ent.base.js" || app="浙大恩特客户资源管理系统"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
yongyouU8-doupload.py检测用友U8-OA协同工作系统doUpload.jsp接口任意文件上传漏洞
Fofa搜索语句
```
title="用友U8-OA"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
jinhe-rssmodules-sql.py检测金和OA C6 RssModulesHttp.aspx存在SQL注入漏洞
Fofa搜索语句
```
app="金和网络-金和OA"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
feiyuxing-ruokl.py检测飞鱼星路由器 弱口令漏洞
Fofa搜索语句
```
body = "../img/R1/loginbg.jpg"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
dongsheng-getdatalist-sql.py检测东胜物流软件-GetDataList接口SQL注入漏洞
Fofa搜索语句
```
body="CompanysAdapter.aspx"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
dongsheng-saveuser-sql.py检测东胜物流软件-SaveUserQuerySetting接口SQL注入漏洞
Fofa搜索语句
```
body="CompanysAdapter.aspx"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
dongsheng-Tcodevoyno-sql.py检测东胜物流软件-TCodeVoynoAdapter.aspx接口SQL注入漏洞
Fofa搜索语句
```
body="CompanysAdapter.aspx"
```
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
feiqi-parsetree-sql.py检测飞企互联-FE企业运营管理平台-parsetree接口存在SQL注入漏洞
Fofa搜索语句
```
app="飞企互联-FE企业运营管理平台"
```
