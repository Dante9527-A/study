import json
import base64
import time
import hmac
import copy


class Jwt():
    def __init__(self):
        pass

    # 生成token的方法
    # payload：载荷，token所承载的数据
    # key：共享秘钥key
    # exe:token的有效期，以秒为单位
    @staticmethod
    def encode(payload, key, exp=300):
        # 1 初始化头
        # 1.1 用字典表示的header
        header = {'alg': 'HS256', 'typ': 'JWT'}
        # 1.2 将字典序列化为json串
        header_json = json.dumps(header,
                                 separators=(',', ':'),
                                 sort_keys=True)
        # print(header_json)
        # 1.3 将json串进行base64编码
        # header_json.encode()  字符串=>字节串
        header_bs = Jwt.b64encode(header_json.encode())
        print(header_bs)
        # 2 载荷（公有声明和私有声明）
        # 2.1 对实参做一个深拷贝，不希望在函数内部修改到实参的值
        payload_data = copy.deepcopy(payload)
        # 2.2 设置公有声明，token的有效期
        payload_data['exp'] = time.time() + int(exp)
        # 2.3 对载荷对象字段序列化为json串
        payload_json = json.dumps(payload_data,
                                  separators=(',', ':'),
                                  sort_keys=True)
        # 2.4 将json串做base64编码
        payload_bs = Jwt.b64encode(payload_json.encode())
        print(payload_bs)
        # 3 签名(消息认证码的算法)
        # 3.1 生成一个算法对象
        hm = hmac.new(key.encode(),
                      header_bs + b'.' + payload_bs,
                      digestmod='SHA256')
        # 3.2 调用算法对象的digest方法，得到消息认证码
        digest = hm.digest()
        # 3.3 将消息认证码也要base64编码
        hm_bs = Jwt.b64encode(digest)
        print(hm_bs)
        return header_bs + b'.' + payload_bs + b'.' + hm_bs

    @staticmethod
    def decode(token, key):
        # 拆分token为三部分
        header_bs, payload_bs, sign = token.split(b'.')
        # 重新计算消息认证码
        hm = hmac.new(key.encode(),
                      header_bs + b'.' + payload_bs,
                      digestmod='SHA256')
        # 调用算法对象的digest方法，得到消息认证码
        digest = hm.digest()
        # 将消息认证码也要base64编码
        sign2 = Jwt.b64encode(digest)
        # 1. 两个消息认证码不相同，验证失败
        if sign != sign2:
            raise
        # 2.将payload b64解码得到json串，再反序列化对象【字典】
        # 一定要注意：将去掉的=补回来
        payload_js = Jwt.b64decode(payload_bs)
        # 将json串反序列化为对象【字典】
        payload = json.loads(payload_js)
        exp = payload['exp']
        now = time.time()
        # token 已经过期了
        if now > exp:
            raise
        return payload



    @staticmethod
    def b64decode(b_s):
        rem = len(b_s) % 4
        if rem > 0:
            b_s += b'=' * (4 - rem)
        return base64.urlsafe_b64decode(b_s)

    @staticmethod
    def b64encode(j_s):
        return base64.urlsafe_b64encode(j_s).replace(b'=', b'')


if __name__ == '__main__':
    token = Jwt.encode({'username': 'aid2010'},  # 私有声明
                       '123456',  # 共享秘钥
                       2)
    print(token)
    time.sleep(3)
    payload = Jwt.decode(token,'123456')
    print(payload)
