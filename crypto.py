import zlib


def get_hash_url(url):
    return hex(zlib.crc32(bytes(url, 'utf-8')))[2:]
