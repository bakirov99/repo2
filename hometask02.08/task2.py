from concurrent.futures import ProcessPoolExecutor
import os


def word_numbers(file: str):
    dc: dict = dict()
    count_number: int = 0
    with open(file, 'r') as f:
        data = f.read()
    for item in data.split():
        try:
            item = int(item)
        except ValueError:
            pass
        else:
            count_number += 1
    dc[file] = count_number
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
