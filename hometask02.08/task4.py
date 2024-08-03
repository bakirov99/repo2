from concurrent.futures import ProcessPoolExecutor
import os


max_sentence = ""


def word_numbers(file: str):
    global max_sentence
    dc: dict = dict()
    with open(file, 'r') as f:
        data = f.read()
    for item in data.split('.'):
        if item > max_sentence:
            max_sentence = item
    dc[max_sentence] = len(max_sentence.split())
    return dc


def check_txt(file: str) -> bool:
    f = file.split('.')
    if f[-1] != 'txt':
        return False
    return True


if __name__ == '__main__':
    ls: list = [file for file in os.listdir() if check_txt(file)]
    with ProcessPoolExecutor(max_workers=len(ls)) as pool:
        result = list(pool.map(word_numbers, ls))

