# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/8/23 12:21


# 上传图片到七牛云
def util_upload_image_qiniu(icon_file, icon_path):
    access_key = "K8-aPB6c05h*****yV_9E3E1iJpVfA"
    secret_key = "mTo2c-nm2IAg-6M****7KZKQxUuu9r"

    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 要上传的空间 - 即创建的空间
    bucket_name = 'cd-python-example'

    # 上传后保存的文件名
    key = icon_file.name

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)

    # 先上传到本地再上传到七牛云
    localfile = os.path.join(MEDIA_ROOT, icon_path)
    ret, info = put_file(token, key, localfile)
    print(ret, info)

    # 不上传到本地只上传到七牛云
    # ret, info = put_data(token, key, icon_file.read())

    # 获取云存储后的文件名字和存储地址
    filename = ret.get("key")
    save_path = "http://qf96g9ppn.hb-bkt.clouddn.com/" + filename

    return save_path

