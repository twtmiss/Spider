 #coding: utf-8
print("大法")
http://login.gwifi.com.cn/cmps/admin.php/api/login/
?gw_address=10.21.0.2
&gw_port=8060
&gw_id=GWIFI-qingdaogongxueyuan02
&ip=10.21.180.163
&mac=18:4F:32:F3:DA:5F
&url=http%3A//www.baidu.com%3Fua%3DMozilla  #http://www.baidu.com?ua=Mozilla
&apmac=00:0b:ab:f6:a5:f4&ssid=

{"auth_state":1,
"gw_id":"GWIFI-qingdaogongxueyuan02",
"access_type":"0",
"authStaType":"0",
"station_sn":"000babf6a5f4",
"client_mac":"18:4F:32:F3:DA:5F",
"online_time":12791,
"logout_reason":8,
"contact_phone":"400-038-5858",
"suggest_phone":"400-038-5858",
"station_cloud":"login.gwifi.com.cn",
"orgId":"877"}'

get_json=json.loads(urllib.request.urlopen("http://10.21.0.2:8060/wifidog/get_auth_state?ip=10.21.180.163").read())['data']


var loginAction  = function(params){
		var btn = $("#first_button");
		var round = Math.round(Math.random()*1000);
		var form = $("#frmLogin");
		$.ajax({
            url: "/cmps/admin.php/api/loginaction?round="+round,
            data: form.serialize(),
            type: "post",
            async: false,
            dataType: "json",
            success: function (data) {
                if (data.status === 1) {
                	if(data.data.reasoncode == "44"){
    					params = getWechatParams(data);
    					//showSelectMessage(params);
    					wechatAuth(params.okParams);
    				}else{
    					window.location.href = data.info;
    				}
                } else {
                    btn.removeAttr('disabled');
                    doFailedLogin(data,"frmLogin");
    				return false;
                }
            }
        });
	}