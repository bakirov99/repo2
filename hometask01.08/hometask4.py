from threading import Thread, current_thread
import requests
import json

result = ""


def dummy():
    global result
    print(f"current thread: {current_thread().ident}")
    resp = requests.get(url='https://dummyjson.com/posts')
    result = resp.json()
    print(f"Stopped: {current_thread().ident}")


if __name__ == '__main__':
    threads: list = list()
    for i in range(4):
        thread = Thread(target=dummy)
        threads.append(thread)
        thread.start()
        thread.join()
        with open(f"file{i+1}.json", "w") as file:
            json.dump(result, file, indent=4)


