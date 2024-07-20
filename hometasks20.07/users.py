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

    def make_product(self):
        """Products uchun namedtuple yaratish funksiyasi"""
        ls_product: list = list()
        field_names = 'id title price rating'
        Product = namedtuple('Product', field_names=field_names)
        for item in self.download():
            try:
                product = Product(id=item['id'], title=item['title'], price=item['price'], rating=item['rating'])
            except:
                raise KeyError("Mos kalit qiymatlari topilmadi. url berishda xatolikka yo'l qo'yilgan ko'rinadi")
            else:
                ls_product.append(product)
        return ls_product

    def make_comment(self):
        """Comments uchun namedtuple yaratish funksiyasi"""
        ls_comment: list = list()
        field_names = 'id post_id user_id body'
        Comment = namedtuple('Comment', field_names=field_names)
        for item in self.download():
            try:
                comment = Comment(id=item['id'], post_id=item['postId'], user_id=item['user']['id'], body=item['body'])
            except:
                raise KeyError("Mos kalit qiymatlari topilmadi. url berishda xatolikka yo'l qo'yilgan ko'rinadi")
            else:
                ls_comment.append(comment)
        return ls_comment


def tested():
    for_user = DummyRequest(url='https://dummyjson.com/users')
    for_post = DummyRequest(url='https://dummyjson.com/posts')
    for_product = DummyRequest(url='https://dummyjson.com/products')
    for_comment = DummyRequest(url='https://dummyjson.com/comments')
    for i in for_comment.make_comment():
        print(i)


if __name__ == '__main__':
    tested()
