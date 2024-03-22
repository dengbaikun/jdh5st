import hashlib
import hmac

function_registry = {}


def register_function(name):
    def decorator(func):
        function_registry[name] = func
        return func

    return decorator


def digest(mode, *args, **kwargs):
    if mode not in function_registry:
        raise ValueError("mode failed")
    return function_registry[mode](*args, **kwargs)


class Digester:
    MD5 = 1
    SHA1 = 2
    SHA256 = 3
    SHA364 = 4
    SHA512 = 5
    HMAC = 7
    SM3 = 8

    @staticmethod
    @register_function(MD5)
    def md5(data):
        md5_hash = hashlib.md5()
        md5_hash.update(data.encode('utf-8'))
        return md5_hash.hexdigest()

    @staticmethod
    @register_function(MD5)
    def md5Digest(data):
        md5_hash = hashlib.md5()
        md5_hash.update(data.encode('utf-8'))
        return md5_hash.digest()

    @staticmethod
    @register_function(SHA1)
    def sha1(data):
        sha1_hash = hashlib.sha1()
        sha1_hash.update(data.encode('utf-8'))
        return sha1_hash.hexdigest()

    @staticmethod
    @register_function(SHA256)
    def sha256(data):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(data.encode('utf-8'))
        return sha256_hash.hexdigest()

    @staticmethod
    @register_function(SHA512)
    def sha512(data):
        sha512_hash = hashlib.sha512()
        sha512_hash.update(data.encode('utf-8'))
        return sha512_hash.hexdigest()

    @staticmethod
    @register_function(SHA364)
    def sha384(data):
        sha384_hash = hashlib.sha384()
        sha384_hash.update(data.encode('utf-8'))
        return sha384_hash.hexdigest()

    @staticmethod
    @register_function(HMAC)
    def hmac(data, secret_key, hash_function=None):
        # 选择一个哈希函数（在此示例中使用SHA-256）
        hash_function = hash_function if hash_function else hashlib.sha256

        # 使用秘密密钥和哈希函数创建HMAC对象
        hmac_obj = hmac.new(secret_key, data, hash_function)

        # 计算HMAC摘要
        hmac_digest = hmac_obj.digest()
        # 你也可以获取摘要的十六进制表示
        hmac_hexdigest = hmac_obj.hexdigest()
        return hmac_hexdigest



if __name__ == '__main__':
    data = '{"skuId":10096186210939,"cat":"9987,653,655","area":"19_1666_36267_36272","shopId":"10449763","venderId":10679769,"paramJson":"{\\"platform2\\":\\"1\\",\\"colType\\":0,\\"specialAttrStr\\":\\"p0pp1pppppppp1ppppppppppppppp\\",\\"skuMarkStr\\":\\"00\\"}","num":1,"bbTraffic":"","canvasType":1}'
    # 示例用法
    md5_hash = Digester.md5(data)
    sha1_hash = Digester.sha1(data)
    sha256_hash = Digester.sha256(data)
    sha512_hash = Digester.sha512(data)
    sha384_hash = Digester.sha384(data)
    sm3_hash = Digester.sm3(data)

    print("MD5 散列值:", md5_hash)
    print("SHA-1 散列值:", sha1_hash)
    print("SHA-256 散列值:", sha256_hash)
    print("SHA-512 散列值:", sha512_hash)
    print("SHA-384 散列值:", sha384_hash)
    print("SM3 散列值:", sm3_hash)
    # 你的秘密密钥
    secret_key = b'password'

    # 要进行身份验证的数据
    data = 'test中文'.encode()
    print("HMAC 编码:", Digester.hmac(data, secret_key, hashlib.md5))
