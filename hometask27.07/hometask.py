from dataclasses import dataclass


#  1-masala
@dataclass
class ListClass:
    ls_num: list

    def sort_ls(self) -> list:
        """Tartiblash funksiyasi"""
        return sorted(self.ls_num)

    def add_func(self):
        nums_ls = self.sort_ls()
        last_indx = len(nums_ls) - 1
        num = nums_ls[0]
        i = 1
        while isinstance(num, int):
            print(num == nums_ls[i])
            if num == nums_ls[i]:
                print(nums_ls.pop(i))
                nums_ls.insert(last_indx, '_')
            else:
                num = nums_ls[i]
                i += 1

        return nums_ls


# 3-masala
def find_one(ls: list[int]) -> int:
    for i in ls:
        if ls.count(i) == 1:
            return i


# 4-masala
def find_nums(ls: list[int]) -> int:
    for i in range(max(ls)):
        if i not in ls:
            return i


# 5-masala
def like_users(ls: list) -> str:
    if len(ls) == 0:
        return "Bu hech kimga yoqmadi."
    elif len(ls) == 1:
        return f"Bu {ls[0]}ga yoqdi."
    elif len(ls) == 2:
        return f"Bu {ls[0]} va {ls[1]}ga yoqdi."
    elif len(ls) == 3:
        return f"Bu {ls[0]}, {ls[1]} va {ls[2]}larga yoqdi."
    else:
        return f"Bu {ls[0]}, {ls[1]} va yana {len(ls)-2} kishiga yoqdi."


def tester():
    u = ['Abdulla', 'Nemat', 'Sherzod', 'Shamsuddin']
    print(like_users(u))


tester()
