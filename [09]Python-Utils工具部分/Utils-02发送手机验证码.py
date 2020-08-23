# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/8/23 12:18




def util_send_code(mobile):

    url = "https://api.netease.im/sms/sendcode.action"

    data = { "mobile": mobile }

    AppKey = "e34962a656267b26e750d286b2f682f9"
    AppSecret = "5f9092ea4ef9"
    # Nonce: 随机数,128字符
    Nonce = hashlib.new("sha512", str(time()).encode("utf-8")).hexdigest()
    # CurTime: 当前UTC时间戳,从1970年1月1日0点0分0秒开始到现在的秒数(String)
    CurTime = str(int(time()))
    print(CurTime, type(CurTime))
    # CheckSum: SHA1(AppSecret + Nonce + CurTime),三个参数拼接的字符串,进行SHA1哈希计算,转化成16进制字符(String,小写)
    content = AppSecret + Nonce + CurTime
    CheckSum = hashlib.sha1(content.encode("utf-8")).hexdigest()

    headers = {
        "AppKey": AppKey,
        "Nonce": Nonce,
        "CurTime": CurTime,
        "CheckSum": CheckSum,
        # "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    }

    response = requests.post(url, data, headers=headers)  # 响应json数据

    # str_result = response.text  # 获取响应的字符串数据
    # json_result = json.loads(str_result)  # 字符串数据转换成json数据
    json_result = response.json()  # 获取响应的json数据
    print(json_result)
    return json_result



