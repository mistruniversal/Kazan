# import threading
# from queue import Queue
# from threading import Thread
# import random
# import time
#
#
# class Table():
#     def __init__(self,number,guest=None):
#         self.number=number
#         self.guest=guest
#
#
#
# # class Guest(Thread):
# class Guest():
#     def __init__(self,name:str):
#         self.name=name
#
#     def run(self):
#         time.sleep(random.randint(3,10))
#
#
#
# class Cafe():
#     def __init__(self,*table):
#         self.table=table
#         self.queue=Queue()
#
#     def guest_arrival(self,*quests):
#         if len(quests)>1:
#             for i in quests:
#                 for k in self.table:
#                     if k.guest == None:
#                         k.guest=i.name
#                         print(f'Стол {k.number} заняли')
#                         break
#                     else:
#                         print('Пропуск')
#         else:
#             for k in self.table:
#                 if k.guest == None:
#                     k.guest = quests.name
#                     print(f'Стол {k.number} занят')
#                     break
#
#
#
#
#     def discuss_guests(self,quests):
#         print(quests.name)
#
# id1=Guest('vasya')
# is1=Cafe(Table(1),Table(2))
#
# is1.guest_arrival(id1)
#


















import threading
from queue import Queue
from threading import Thread
import random
import time


class Table():
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
# class Guest():
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe():
    def __init__(self, *table):
        self.table = table
        self.queue = Queue()

    def guest_arrival(self, *quests):
        for i in quests:
            for k in self.table:
                if k.guest is None:
                    k.guest = i.name
                    i.start
                    print(k.number, i.name)
                    print('Есть контакт')
                else:
                    self.queue.put(i.name)
                    print(f'{i.name} в очереди')

    def discuss_guests(self):
        # print(not self.queue.empty())
        while not self.queue.empty():
            for i in self.table:
                if i.guest and i.guest.is_alive():
                    print("Закончил")
                    i.guest=None
        #     for i in self.table:
        #         time.sleep(random.randint(2,5))
        #         print('мы пожрали')
        #     print(self.queue.empty())




id1 = Guest('vasya')
is1 = Cafe(Table(1), Table(2))

is1.guest_arrival(id1)
is1.discuss_guests()















# import random
# import time
# from threading import Thread
# from queue import Queue
#
#
# class Table:
#     def __init__(self, number):
#         self.number = number
#         self.guest = None
#
#
# class Guest(Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         wait_time = random.randint(3, 10)
#         time.sleep(wait_time)
#
#
# class Cafe:
#     def __init__(self, *tables):
#         self.queue = Queue()
#         self.tables = tables
#
#     def guest_arrival(self, *guests):
#         for guest in guests:
#             assigned = False
#             for table in self.tables:
#                 if table.guest is None:  # Если стол свободен
#                     table.guest = guest  # Сажаем гостя за стол
#                     guest.start()  # Запускаем поток гостя
#                     print(f"{guest.name} сел(-а) за стол номер {table.number}")
#                     assigned = True
#                     break
#
#             if not assigned:  # Если нет свободных столов
#                 self.queue.put(guest)  # Помещаем в очередь
#                 print(f"{guest.name} в очереди")
#
#     def discuss_guests(self):
#         while not self.queue.empty() or any(table.guest is not None for table in self.tables):
#             for table in self.tables:
#                 if table.guest is not None and not table.guest.is_alive():  # Гость закончил приём пищи
#                     print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
#                     print(f"Стол номер {table.number} свободен")
#                     table.guest = None  # Освобождаем стол
#
#                 # Если есть очередь и стол свободен
#                 if table.guest is None and not self.queue.empty():
#                     next_guest = self.queue.get()  # Берём следующего из очереди
#                     table.guest = next_guest  # Сажаем его за стол
#                     next_guest.start()  # Запускаем поток этого гостя
#                     print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
#
#
# # Пример использования
# if __name__ == "__main__":
#     cafe = Cafe(Table(1), Table(2), Table(3))
#
#     # Создаём гостей
#     guests = [Guest("Vasya"), Guest("Masha"), Guest("Petya"), Guest("Olya")]
#
#     # Гости прибывают в кафе
#     cafe.guest_arrival(*guests)
#
#     # Обслуживаем гостей
#     cafe.discuss_guests()
