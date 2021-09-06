from PIL import Image


def solve():
    with Image.open('after_flag.png') as after_flag:
        with Image.new('RGB', (after_flag.width, after_flag.height)) as flag:
            data = [(r % 2 * 255, r % 2 * 255, r % 2 * 255) for (r, g, b) in after_flag.getdata()]
            flag.putdata(data)
            # nitic_ctf{high_contrast}
            flag.show()


if __name__ == '__main__':
    solve()
