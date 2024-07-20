import requests
from collections import namedtuple


class DummyRequest:

    def __init__(self, url: str) -> None:
        self.url = url

    def download(self) -> list:
        ls_data: list
        data = requests.get(self.url)
        d = self.url.split('/')[-1]
        print(d)
        ls_data = data.json()[d]
        return ls_data

    def make_user(self) -> list:
        """Users uchun namedtuple yaratish funksiyasi"""
        ls_user: list = list()
        field_names = 'id username firstname lastname datebirth email phone'
        User = namedtuple('User', field_names=field_names)
        for item in self.download():
            try:
                user = User(id=item['id'], username=item['username'], firstname=item['firstName'],
                            lastname=item['lastName'], datebirth=item['birthDate'],
                            email=item['email'], phone=item['phone'])
            except:
                raise KeyError("Mos kalit qiymatlari topilmadi. url berishda xatolikka yo'l qo'yilgan ko'rinadi")
            else:
                ls_user.append(user)
        return ls_user

    def make_post(self):
        """Posts uchun namedtuple yaratish funksiyasi"""
        ls_post: list = list()
        field_names = 'id title body'
        Post = namedtuple('Post', field_names=field_names)
        for item in self.download():
            try:
                post = Post(id=item['id'], title=item['title'], body=item['body'])
            except:
                raise KeyError("Mos kalit qiymatlari topilmadi. url berishda xatolikka yo'l qo'yilgan ko'rinadi")
            else:
                ls_post.append(post)
        return ls_post


def tested():
    for_user = DummyRequest(url='https://dummyjson.com/users')
    for_post = DummyRequest(url='https://dummyjson.com/users')

    # for i in for_user.make_post():
    #     print(i)


if __name__ == '__main__':
    tested()
