from manager import Database
import time
from datetime import datetime
import multiprocessing


query_1 = {
     "query_1": "INSERT INTO users VALUES('Ali', 21)",
     "query_2": "INSERT INTO users VALUES('Abdulaziz', 19)",
     "query_3": "INSERT INTO users VALUES('Akobir', 20)",
     "query_4": "INSERT INTO users VALUES('Azkiz', 12)",
     "query_5": "INSERT INTO users VALUES('Abror', 32)",
     "query_6": "INSERT INTO users VALUES('Sardor', 25)",
     "query_7": "INSERT INTO users VALUES('Davron', 27)",
     "query_8": "INSERT INTO users VALUES('Feruz', 23)"

 }

query_2 = {
     "query_1": "INSERT INTO courses VALUES('c++', 100, 'Yunusobod')",
     "query_2": "INSERT INTO courses VALUES('java', 500, 'Chilonzor')",
     "query_3": "INSERT INTO courses VALUES('python', 900, 'Xorazm')",
     "query_4": "INSERT INTO courses VALUES('SMM', 900, 'Xadra')",
     "query_5": "INSERT INTO courses VALUES('Dizayn', 700, 'Chimboy')",
     "query_6": "INSERT INTO courses VALUES('.NET', 124, 'Yunusobod')",
     "query_7": "INSERT INTO courses VALUES('c', 650, 'Chilonzor')",
     "query_8": "INSERT INTO courses VALUES('Marketing', 899, 'Xadra')",

}


def insert_data(query, query_type):
    time.sleep(3)
    print(Database.connect(query, query_type))


def process():

    query1 = "INSERT INTO courses VALUES('c++', 100, 'Yunusobod')"
    query_2 = "INSERT INTO courses VALUES('java', 500, 'Chilonzor')"
    query_3 = "INSERT INTO  courses VALUES('python', 900, 'Xorazm')"
    query_4 = "INSERT INTO courses VALUES('SMM', 900, 'Xadra')"
    query_5 = "INSERT INTO courses VALUES('Dizayn', 700, 'Chimboy')"
    query_6 = "INSERT INTO courses VALUES('.NET', 124, 'Yunusobod')"
    query_7 = "INSERT INTO courses VALUES('c', 650, 'Chilonzor')"
    query_8 = "INSERT INTO courses VALUES('Marketing', 899, 'Xadra')"
    query_type_1 = "insert"
    query_type_2 = "insert"
    query_type_3 = "insert"
    query_type_4 = "insert"
    query_type_5 = "insert"
    query_type_6 = "insert"
    query_type_7 = "insert"
    query_type_8 = "insert"

    process1 = multiprocessing.Process(target=insert_data, args=[query1, query_type_1])
    process2 = multiprocessing.Process(target=insert_data, args=[query_2, query_type_2])
    process3 = multiprocessing.Process(target=insert_data, args=[query_3, query_type_3])
    process4 = multiprocessing.Process(target=insert_data, args=[query_4, query_type_4])
    process5 = multiprocessing.Process(target=insert_data, args=[query_5, query_type_5])
    process6 = multiprocessing.Process(target=insert_data, args=[query_6, query_type_6])
    process7 = multiprocessing.Process(target=insert_data, args=[query_7, query_type_7])
    process8 = multiprocessing.Process(target=insert_data, args=[query_8, query_type_8])

    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    process8.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()
    process7.join()
    process8.join()


if __name__ == '__main__':
    print(datetime.now())
    process()
    print(datetime.now())
