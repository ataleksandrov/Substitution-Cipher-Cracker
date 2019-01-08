def encrypt(key_dict, text):
    return ''.join([key_dict.get(c, c) for c in text])

def decrypt(key_dict, text):
    return encrypt({v:k for k,v in key_dict.items()} ,text)