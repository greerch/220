def encode(data, key):
    new = ""
    for i in range(len(data)):
        num = ord(data[i])
        shift = num + key
        new = new + chr(shift)
    return new

def encode_better(data, key):
    new = ""
    for i in range(len(data)):
        num = ord(data[i])
        module = i % len(key)
        shift = num + (ord(key[module]) - 97)
        new = new + chr(shift % 256)
    return new

