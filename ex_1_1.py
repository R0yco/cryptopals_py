import codecs
def hex_to_base64(hex_string):
    return codecs.encode(codecs.decode(hex_string,'hex'),'base64') \
    .decode() \
    .replace("\n","")

