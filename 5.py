import time
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname , password):
        a=0
        b=0
        for user in self.users:
            if nickname == user:
                a=1
            if password == user:
                b=1
        if a == 1 and b == 1:
            print('Все успешно')


    def register(self, nickname , password , age):
        for user in self.users:
            if nickname == user.nickname:
                print('иди нафиг такой пользователь уже есть')
            else:
                self.users.append(nickname)
            if hash(password) == user.password:
                print('ты че хакер')
            else:
                self.users.append(password)
            if user == age:
                print('ты че хакер')
            else:
                self.users.append(age)

    def log_out(self):
        print('доделать')

    def add(self,*args):
        for i in self.videos:
            for video in args:
                if i == video:
                    print('None')
                else:
                    self.videos.append(video)

    def get_video(self, num):
        listvideo=[]
        for i in self.videos:
            k=i.lower()
            k.split()
            if num.lower() in k:
                listvideo.append(i)
        return listvideo

    def watch_video(self,n):
        for i in self.videos:
            if n == i:
                print('секунды')
                break

class Video:

    def __init__(self, title, duration, time_now=0 , adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
u=User('Для', 1041,14)






# ur.watch_video('Лучший язык программирования 2024 года!')
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')


