import os
import socket
import threading
import random
import traceback
import string

FLAG = os.getenv("FLAG", (
    "Not the flag you're searching for, Keep looking close, there's plenty more. "
    "INTIGRITI{4a9f2b823dc8d09fd732d741954ccce2} A clue I might be, but not the key, The flag is hidden, not in me!!!"
))

MAX_LENGTH = 160


def otp(p, k):
    k_r = (k * ((len(p) // len(k)) + 1))[:len(p)]
    return bytes([p ^ k for p, k in zip(p, k_r)])


def check_cat_box(ciphertext, cat_state):
    c = bytearray(ciphertext)
    if cat_state == 1:
        for i in range(len(c)):
            c[i] = ((c[i] << 1) & 0xFF) ^ 0xAC
    else:
        for i in range(len(c)):
            c[i] = ((c[i] >> 1) | (c[i] << 7)) & 0xFF
            c[i] ^= 0xCA
    return bytes(c)


def handle_client(client_socket):
    try:
        # Set socket timeout to prevent hanging
        client_socket.settimeout(60)

        KEY = ''.join(random.choices(
            string.ascii_letters + string.digits, k=160)).encode()

        message = (
            "Welcome to Schrödinger's Pad!\n"
            "Due to its quantum, cat-like nature, this cryptosystem can re-use the same key\n"
            "Thankfully, that means you'll never be able to uncover this secret message :')\n\n"
        )
        client_socket.send(message.encode())

        client_socket.send(
            f"Encrypted (cat state=ERROR! 'cat not in box'): {otp(FLAG.encode(), KEY).hex()}\n".encode(
            )
        )

        client_socket.send(b"\nAnyway, why don't you try it for yourself?\n")

        plaintext = client_socket.recv(1024).strip()
        print(plaintext)

        if len(plaintext) > MAX_LENGTH:
            client_socket.send(
                f"Plaintext too long! Max allowed length is {MAX_LENGTH} characters.\n".encode(
                )
            )
            return

        cat_state = random.choice([0, 1])
        ciphertext = otp(plaintext, KEY)
        c_ciphertext = check_cat_box(ciphertext, cat_state)
        cat_state_str = "alive" if cat_state == 1 else "dead"

        client_socket.send(
            f"Encrypted (cat state={cat_state_str}): {c_ciphertext.hex()}\n".encode(
            )
        )

    except socket.timeout:
        client_socket.send(b"Error: Connection timed out.\n")
    except BrokenPipeError:
        print("Client disconnected abruptly.")
    except Exception as e:
        print(f"Server Error: {e}")
        traceback.print_exc()
    finally:
        client_socket.close()


def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("0.0.0.0", 1337))

        # Increase backlog size for more concurrent connections
        server.listen(100)
        print("Server started on port 1337")

        while True:
            try:
                client_socket, addr = server.accept()
                print(f"Accepted connection from {addr}")

                # Create a daemon thread to handle each client
                client_handler = threading.Thread(
                    target=handle_client, args=(client_socket,))
                # Daemon thread will exit automatically when main thread ends
                client_handler.daemon = True
                client_handler.start()

            except Exception as e:
                print(f"Error accepting connection: {e}")
                traceback.print_exc()

    except Exception as e:
        print(f"Critical server error: {e}")
    finally:
        server.close()
        print("[*] Server shutdown")


if __name__ == "__main__":
    start_server()