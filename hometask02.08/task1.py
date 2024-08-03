from concurrent.futures import ProcessPoolExecutor
import os


def word_numbers(file: str):
    dc: dict = dict()
    with open(file, 'r') as f:
        data = f.read()
    count_word = len(data.split())
    dc[file] = count_word
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
    print(result)
