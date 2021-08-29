from PIL import Image


def solve():
    data = []
    with Image.open('chall.png') as img:
        for r, g, b in list(img.getdata()):
            data.append(r)
            data.append(g)
            data.append(b)

    for flag_len in range(10, 100):
        flag = 0
        bits_len = flag_len * 8 - 1
        for i in range(bits_len):
            bit = data[i] & 1
            for j in range(i + bits_len, len(data), bits_len):
                bit = bit & (data[j] & 1)
            flag += (bit << i)
        flag = flag.to_bytes(flag_len, 'big').decode()
        if flag.startswith('CakeCTF{'):
            return flag


if __name__ == '__main__':
    print(solve())
