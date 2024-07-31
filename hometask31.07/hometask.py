import psycopg2


class DB:

    def __init__(self):
        self.dbname = 'postgres'
        self.user = 'postgres'
        self.password = '1234'
        self.host = 'localhost'
        self.port = '5432'
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cur = self.conn.cursor()
        except:
            raise "Ma'lumotlar bazasiga ulanib bo'lmadi."

    def create_t(self, tbname: str) -> None:
        self.cur.execute(
            f"""CREATE TABLE IF NOT EXISTS {tbname}(
                        id SERIAL PRIMARY KEY, username TEXT UNIQUE NOT NULL,
                        firstname TEXT, lastname TEXT);""")

    def add_data(self, username: str, firstname='', lastname='') -> None:
        self.cur.execute(
            f"""INSERT INTO users(username, firstname, lastname) VALUES(%s, %s, %s);""",
            (username, firstname, lastname)
        )

    def delete_data(self, username: str):
        self.cur.execute(
            f"""DELETE FROM users WHERE username='{username}'"""
        )

    def update_data(self, username: str, firstname: str, lastname: str):
        self.cur.execute(
            f"""UPDATE users
            SET firstname='{firstname}', lastname='{lastname}'
            WHERE username='{username}'"""
        )


    def show_data(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()


with DB() as file:
    file.connect()
    file.create_t(tbname='users')
    # file.add_data(username='suxrob')
    # file.delete_data(username='alisher')
    file.update_data(username='suxrob', firstname='Suxrob', lastname="Qodirov")



















