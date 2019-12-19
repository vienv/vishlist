from configparser import ConfigParser
#from mysql.connector import MySQLConnection, Error

def read_db_config(filename='db.ini', section='mysql1'):
    parser = ConfigParser()
    parser.read(filename)
    return dict(parser.items(section)) if parser.has_section(section) else False

class VListModel():
    def __init__(self, id_obj):
        self.db_config = read_db_config()
        self.id = id_obj

    @property
    def data(self):
        try:
            db = MySQLConnection(**self._db_config)
            cursor = db.cursor()
            #выбор наименования обьекта по id
            cursor.execute('SELECT name, price, link, comment FROM table WHERE id=%s', (self.id,))
            self._name, self._price, self._link, self._comment = cursor.fetchall()[0]
        except Error as error:
            print(error)
        finally:
            conn.close()
        return self._name, self._price, self._link, self._comment

    @data.setter
    def data(self, in_data):
        try:
            self._name, self._price, self._link, self._comment = in_data
            db = MySQLConnection(**self._db_config)
            cursor = db.cursor()
            #Запись данных в базу
            cursor.execute('UPDATE table SET name=%s, price=%s, link=%s, comment=%s FROM table WHERE id=%s', \
                (self._name, self._price, self._link, self._comment, self.id))
            db.commit()
        except Error as error:
            print(error)
        finally:
            conn.close()
