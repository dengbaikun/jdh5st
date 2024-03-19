import base64
from abc import ABCMeta, abstractmethod


class CODEC(metaclass=ABCMeta):

    # 构造方法
    @staticmethod
    @abstractmethod
    def decode(decode_data):
        return decode_data

    @staticmethod
    @abstractmethod
    def encode(encode_data):
        return encode_data


class HEX(CODEC):
    @staticmethod
    def decode(decode_data):
        return bytes.fromhex(decode_data)

    @staticmethod
    def encode(encode_data):
        if isinstance(encode_data, bytes):
            return ''.join(format(char, '02x') for char in encode_data)
        return ''.join(format(ord(char), '02x') for char in encode_data)


class BASE64(CODEC):
    @staticmethod
    def decode(decode_data):
        if isinstance(decode_data, str):
            return base64.b64decode(decode_data.encode('utf8'))
        return base64.b64decode(decode_data)

    @staticmethod
    def encode(encode_data):
        return base64.b64encode(encode_data).decode()


class BASE64_URLSAFE(CODEC):

    @staticmethod
    def decode(decode_data):
        if isinstance(decode_data, str):
            return base64.urlsafe_b64decode(decode_data.encode('utf8'))
        return base64.urlsafe_b64decode(decode_data)

    @staticmethod
    def encode(encode_data):
        return base64.urlsafe_b64encode(encode_data).decode()


if __name__ == '__main__':
    data = "Hello, World!"
    hex_data = HEX.encode(data)
    base64_data = BASE64.encode(data.encode())
    base64_urlsafe = BASE64_URLSAFE.encode(data.encode())
    print("十六进制 编码:", hex_data)
    print("Base64 编码:", base64_data)
    print("Base64_urlsafe 编码:", base64_urlsafe)
    print("十六进制 解码:", HEX.decode(hex_data))
    print("Base64 解码:", BASE64.decode(base64_data))
    print("Base64_urlsafe 解码:", BASE64_URLSAFE.decode(base64_urlsafe))
