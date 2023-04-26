def pkcs7_pad(data, blocksize):
    if len(data) == blocksize:
        return data
    count_to_add = blocksize - len(data)
    byte_to_add = chr(count_to_add)
    return data + count_to_add * bytes(byte_to_add.encode('ascii'))

if __name__ == "__main__":
    print(pkcs7_pad(b"YELLOW SUBMARINE", 16))

    

