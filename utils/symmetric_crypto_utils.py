from Crypto.Cipher import AES, DES, DES3
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from utils.timer import Timer
from utils.codec_utils import CODEC, BASE64, HEX


class SymmetricCrypto:

    # @staticmethod
    # def encrypt_aes(key, plaintext):
    #     cipher = AES.new(key, AES.MODE_EAX)
    #     nonce = cipher.nonce
    #     ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    #     return nonce, ciphertext, tag
    #
    # @staticmethod
    # def decrypt_aes(key, nonce, ciphertext, tag):
    #     cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    #     plaintext = cipher.decrypt(ciphertext)
    #     try:
    #         cipher.verify(tag)
    #         return plaintext
    #     except ValueError:
    #         raise ValueError("Authentication failed")
    @staticmethod
    @Timer("encrypt_aes")
    def encrypt_aes(key, plaintext, mode=AES.MODE_ECB, encode_mode=CODEC, iv=None):
        cipher = AES.new(key, mode, iv) if iv else AES.new(key, mode)
        encrypted_data = cipher.encrypt(pad(plaintext, AES.block_size))
        return encode_mode.encode(encrypted_data)

    @staticmethod
    @Timer("decrypt_aes")
    def decrypt_aes(key, ciphertext, mode=AES.MODE_ECB, encode_mode=CODEC, iv=None):
        cipher = AES.new(key, mode, iv) if iv else AES.new(key, mode)
        padded_data = encode_mode.decode(ciphertext)
        padded_data = cipher.decrypt(padded_data)
        plaintext = unpad(padded_data, AES.block_size)
        return plaintext

    @staticmethod
    @Timer("encrypt_des")
    def encrypt_des(key, plaintext, mode=DES.MODE_ECB, encode_mode=CODEC, iv=None):
        cipher = DES.new(key, mode, iv) if iv else DES.new(key, mode)
        encrypted_data = cipher.encrypt(pad(plaintext, DES.block_size))
        return encode_mode.encode(encrypted_data)

    @staticmethod
    @Timer("decrypt_des")
    def decrypt_des(key, ciphertext, mode=DES.MODE_ECB, encode_mode=CODEC, iv=None):
        cipher = DES.new(key, mode, iv) if iv else DES.new(key, mode)
        padded_data = encode_mode.decode(ciphertext)
        padded_data = cipher.decrypt(padded_data)
        plaintext = unpad(padded_data, DES.block_size)
        return plaintext

    @staticmethod
    @Timer("encrypt_3des")
    def encrypt_3des(key, plaintext, mode=DES3.MODE_ECB, encode_mode=CODEC, iv=None):
        cipher = DES3.new(key, mode, iv) if iv else DES3.new(key, mode)
        encrypted_data = cipher.encrypt(pad(plaintext, DES3.block_size))
        return encode_mode.encode(encrypted_data)

    @staticmethod
    @Timer("decrypt_3des")
    def decrypt_3des(key, ciphertext, mode=DES3.MODE_ECB, encode_mode=CODEC, iv=None):
        cipher = DES3.new(key, mode, iv) if iv else DES3.new(key, mode)
        padded_data = encode_mode.decode(ciphertext)
        padded_data = cipher.decrypt(padded_data)
        plaintext = unpad(padded_data, DES3.block_size)
        return plaintext


if __name__ == "__main__":
    # 示例用法
    key = b'adfg1234asdfqwe2'
    plaintext = b'huyang'
    ciphertext = SymmetricCrypto.encrypt_aes(key, plaintext, AES.MODE_ECB, BASE64)
    print("AES加密后的数据:", ciphertext)
    plaintext = SymmetricCrypto.decrypt_aes(key, ciphertext, AES.MODE_ECB, BASE64)
    print("AES解密后的数据:", plaintext)
    iv = b'0000000000000000'
    ciphertext = SymmetricCrypto.encrypt_aes(key, plaintext, AES.MODE_CBC, BASE64,iv)
    print("iv AES加密后的数据:", ciphertext)
    plaintext = SymmetricCrypto.decrypt_aes(key, ciphertext, AES.MODE_CBC, BASE64,iv)
    print("iv AES解密后的数据:", plaintext)
    key = b"8bytekey"
    ciphertext = SymmetricCrypto.encrypt_des(key, plaintext, DES.MODE_ECB, BASE64)
    print("DES加密后的数据:", ciphertext)
    plaintext = SymmetricCrypto.decrypt_des(key, ciphertext, DES.MODE_ECB, BASE64)
    print("DES解密后的数据:", plaintext)

    key = b'adfg1234asdfqwe2'
    ciphertext = SymmetricCrypto.encrypt_3des(key, plaintext, DES3.MODE_ECB, BASE64)
    print("3DES加密后的数据:", ciphertext)
    plaintext = SymmetricCrypto.decrypt_3des(key, ciphertext, DES3.MODE_ECB, BASE64)
    print("3DES解密后的数据:", plaintext)
