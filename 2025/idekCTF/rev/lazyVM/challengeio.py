import functools
import socket
import time


def retry(max_retries=3):
    def inner_decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args)
                except Exception:
                    retries += 1
                    time.sleep(1)
            return None

        return wrapper

    return inner_decorator


@retry(max_retries=5)
def send(payload):
    if isinstance(payload, str):
        payload = payload.encode("latin1")
    assert isinstance(payload, bytes)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    s.connect(("lazy-vm.chal.idek.team", 1337))
    s.recv(1024)
    s.recv(1024)
    s.send(payload + b"\n")
    result = s.recv(1024)
    s.close()
    return result.decode().strip()
