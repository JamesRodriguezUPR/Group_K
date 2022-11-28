from psycopg2.errors import UniqueViolation
from config.dbconfig import pg_config
import psycopg2


class UsersDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (pg_config['Database'],
                                                                            pg_config['User'],
                                                                            pg_config['Password'],
                                                                            pg_config['Port'],
                                                                            pg_config['Host'])
        self.conn = psycopg2.connect(connection_url)



    def getAllUser(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self,user_email, user_password, first_name, last_name):
        cursor = self.conn.cursor()
        try:
            query = "INSERT INTO users(user_email, user_password, first_name, last_name) VALUES (lower(%s), %s, %s, %s);"
            cursor.execute(query, (user_email, user_password, first_name, last_name,))
            self.conn.commit()
            return True
        except UniqueViolation as e:
            return False

    def get_user_password(self, user_email):
        cursor = self.conn.cursor()
        try:
            query = "Select user_password from users where user_email=lower(%s);"
            cursor.execute(query, (user_email,))
            result = cursor.fetchone()[0]
            return result
        except UniqueViolation as e:
            return None

    def get_user(self, user_email):
        cursor = self.conn.cursor()
        query = "select user_email, first_name, last_name from users where user_email = %s;"
        cursor.execute(query, (user_email,))
        result = cursor.fetchone()
        return result

