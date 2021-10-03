from pathlib import Path
import string

import cv2
import numpy as np


def pixelize(s):
    images = []
    for i in s:
        img = np.full((100, 85, 3), (255, 255, 255), dtype=np.uint8)
        cv2.putText(img, i, (0, 80), cv2.FONT_HERSHEY_PLAIN, 8, (0, 0, 0), 5, cv2.LINE_AA)

        cv2.putText(img, "P", (0, 90), cv2.FONT_HERSHEY_PLAIN, 7, (0, 0, 0), 5, cv2.LINE_AA)
        cv2.putText(img, "I", (0, 90), cv2.FONT_HERSHEY_PLAIN, 8, (0, 0, 0), 5, cv2.LINE_AA)
        cv2.putText(img, "X", (0, 90), cv2.FONT_HERSHEY_PLAIN, 9, (0, 0, 0), 5, cv2.LINE_AA)
        simg = cv2.resize(img, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_NEAREST)  # WTF :-o
        img = cv2.resize(simg, img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

        images.append(img)

    return images


def solve():
    characters = string.digits + string.ascii_lowercase + "{}_"
    images = pixelize(characters)

    flag = ''

    path = Path(__file__).parent / 'output.png'
    flag_img = cv2.imread(str(path))

    for i in range(0, 31 * 85, 85):
        img = flag_img[:, i:i+85, :]
        for j in range(0, len(characters)):
            if (img == images[j]).all():
                flag += characters[j]

    return flag


if __name__ == '__main__':
    print(solve())
