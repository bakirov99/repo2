from threading import Thread, current_thread
import requests

dolor = 0


def dolor_rate():
    global dolor
    print(f"current thread: {current_thread().ident}")
    resp = requests.get(url="https://cbu.uz/uz/arkhiv-kursov-valyut/json")
    data = resp.json()
    dolor = data[0]['Rate']
    print(f"stopped thread {current_thread().ident}\nresult: {dolor}")


if __name__ == '__main__':
    threads: list = list()
    for _ in range(4):
        thread = Thread(target=dolor_rate)
        threads.append(thread)
        thread.start()
        thread.join()
    print(dolor)
