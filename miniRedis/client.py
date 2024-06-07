import socket

def format_command(*args):
    """Formats a command in the Redis Serialization Protocol (RESP) format."""
    command = f"*{len(args)}\r\n"
    for arg in args:
        command += f"${len(arg)}\r\n{arg}\r\n"
    return command


def simple_client():
    host = '127.0.0.1'
    port = 31337
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        commands = [
            format_command('SET', 'key', 'value'),
            format_command('GET', 'key'),
            format_command('DELETE', 'key'),
            format_command('FLUSH')
        ]

        for command in commands:
            s.sendall(command.encode('utf-8'))
            data = s.recv(1024)
            print('Received', repr(data))


if __name__ == '__main__':
    simple_client()
