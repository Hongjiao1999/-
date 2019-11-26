def init(S, T, K):
    # 初始化S盒、T盒
    for i in range(256):
        S.append(i)
        T.append(K[i % len(K)])


def swap(S, T):
    # 更新S盒
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j], S[i]


def create_stream(S, plaintext, keystream):
    # 生成密钥流
    i = 0
    j = 0
    for x in range(len(plaintext)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        keystream.append(S[t])


def encrypt(plaintext, keystream, cipher):
    # 加密生成密文
    for i in range(len(plaintext)):
        t = (keystream[i] ^ ord(plaintext[i])) # 取明文字符的ASCII码
        t = hex(t)
        cipher.append(t[2:])


def decrypt(cipher, keystream, decrypt_plaintext):
    # 解密
    for i in range(len(cipher)):
        t = int("0x" + cipher[i], 16)
        # 用16进制数ASCII码转换成对应字符
        decrypt_plaintext.append(chr(keystream[i] ^ t))


def main():
    key = input("请输入密钥:")
    key.split(" ")
    key = [ord(key[i]) for i in range(len(key))]
    plaintext = input("请输入要加密的明文:")
    s = []
    t = []
    # S盒、T盒
    key_stream = []
    cipher = []
    decrypt_plaintext = []
    init(s, t, key)
    swap(s, t)
    create_stream(s, plaintext, key_stream)
    encrypt(plaintext, key_stream, cipher)
    print(8 * "*" + "  Encryption  " + 8 * "*")
    # print("置乱后的s盒：")
    # print(s)
    print("密钥流：")
    print(key_stream)
    print("Cipher:")
    # print(cipher)
    print("".join(cipher))  # 加密后输出密文
    decrypt(cipher, key_stream, decrypt_plaintext)  # 解密后输出明文
    print("\n" + 8 * "*" + "  Decryption  " + 8 * "*")
    print("明文：")
    print("".join(decrypt_plaintext))


if __name__ == '__main__':
    main()









