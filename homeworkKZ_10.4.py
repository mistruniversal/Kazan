import threading
from queue import Queue
from threading import Thread
import random
import time


class Table():
    def __init__(self,number,guest=None):
        self.number=number
        self.guest=guest



# class Guest(Thread):
class Guest():
    def __init__(self,name:str):
        self.name=name

    def run(self):
        time.sleep(random.randint(3,10))



class Cafe():
    def __init__(self,*table):
        self.table=table
        self.queue=Queue()

    def guest_arrival(self,*quests):
        if len(quests)>1:
            for i in len(quests):
                for k in len(self.table):
                    if self.table[k].guest == None:
                        self.table[k].guest=quests[i].name
                        print(f'Стол {self.table[k].number} заняли')
                        break
                    else:
                        print('Пропуск')
        else:
            for k in len(self.table):
                if self.table[k].guest == None:
                    self.table[k].guest = quests.name
                    print(f'Стол {self.table[k].number} заняли')
                    break




    def discuss_guests(self,quests):
        print(quests.name)

id1=Guest('vasya')
is1=Cafe(Table(1),Table(2))

is1.guest_arrival(id1)


