from threading import Thread
import uuid

# 1- misol
result = 0
vowels = ['a', 'e', 'i', 'o', 'u']


def count_vowel(text: str, vowel: str) -> None:
    global result
    result += text.count(vowel)


if __name__ == '__main__':
    with open('about_me.txt', 'r') as file:
        text1 = file.read()
    text1 = text1.lower()
    thread1 = Thread(target=count_vowel, args=(text1, 'a'))
    thread2 = Thread(target=count_vowel, args=(text1, 'e'))
    thread3 = Thread(target=count_vowel, args=(text1, 'i'))
    thread4 = Thread(target=count_vowel, args=(text1, 'o'))
    thread5 = Thread(target=count_vowel, args=(text1, 'u'))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    print(result)
    ui = uuid.uuid4()
    print(ui)



