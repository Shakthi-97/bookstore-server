import pymysql
import json

db_configs = json.load(open('utils.json'))
DB_NAME = db_configs['DB_NAME']
DB_HOST = db_configs['DB_HOST']
DB_USER = db_configs['DB_USER']
DB_PASSWORD = db_configs['DB_PASSWORD']


def create_connection():
    connection = pymysql.connect(host=DB_HOST, user=DB_USER, database=DB_NAME,
                                 password=DB_PASSWORD)
    return connection


def createBook(title, author, cost):
    connection = create_connection()

    try:
        cursor = connection.cursor()
        sql = '''INSERT INTO Books (title, author, cost) VALUES ('%s', '%s', '%s');''' % (
            title, author, cost)
        result = cursor.execute(sql)
        connection.commit()
        return result

    except Exception as e:
        print(e)

    finally:
        connection.close()


def updateBook(id, title, author, cost):
    connection = create_connection()

    try:
        cursor = connection.cursor()
        sql = '''UPDATE Books SET title ='%s', author ='%s', cost = '%s' WHERE id='%s';''' % (
            title, author, cost, id)
        result = cursor.execute(sql)
        connection.commit()
        return result

    except Exception as e:
        print(e)

    finally:
        connection.close()


def getAllBooks():
    connection = create_connection()

    try:
        cursor = connection.cursor()
        sql = '''select * from Books;'''
        cursor.execute(sql)
        results = cursor.fetchall()

        # this will extract row headers
        row_headers = [x[0] for x in cursor.description]

        json_data = []
        for result in results:
            json_data.append(dict(zip(row_headers, result)))
        j = json.dumps(json_data)

        json_object = json.loads(j)

        return json_object

    except Exception as e:
        print(e)

    finally:
        connection.close()


def deleteBook(id):
    connection = create_connection()

    try:
        cursor = connection.cursor()
        sql = '''DELETE FROM Books WHERE id='%s';''' % (
            id)
        result = cursor.execute(sql)
        connection.commit()
        return result

    except Exception as e:
        print(e)

    finally:
        connection.close()
