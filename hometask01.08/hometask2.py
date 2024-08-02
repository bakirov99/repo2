from threading import Thread, current_thread
from random import randint, choice

token = ""


def token_generate():
    global token
    ls = []
    for i in range(48, 58):
        ls.append(i)
    for i in range(65, 90):
        ls.append(i)
    for i in range(97, 122):
        ls.append(i)
    char = chr(choice(ls))
    token += char


if __name__ == '__main__':
    threads = []
    for _ in range(16):
        thread = Thread(target=token_generate)
        threads.append(thread)
        thread.start()
        thread.join()
    print(token)

