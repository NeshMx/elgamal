import libelgamal as eg

def main():
    msg = input('Introduce el mensaje: ')
    keys = eg.generate_keys()
    privKey = keys.get('privateKey')
    pubKey = keys.get('publicKey')
    msg_ciphr = eg.encrypt(pubKey, msg)
    print('El mensaje cifrado es: \n' +  msg_ciphr)
    msg_plain = eg.decrypt(privKey, msg_ciphr)
    print('El mensaje descifrado es: \n' + msg_plain)


if __name__ == '__main__':
    main()
