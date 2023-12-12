class Person:
    def __init__(self, Age, Name, Money):
        self.name = Name
        self.age = Age
        self.money = Money
        self.job = None
        self.family = None
        self.house = None
        self.hungry = 0
        self.health = 100
        self.intelligence = 100
        self.expirience = 18


    def earn_money(self):
        self.money += 1000

    def spend_money(self, amount):
        self.money -= amount

    def __str__(self):
        return f'Student {self.name}'


    def get_job(self, job):
        if self.expirience <= self.age:
            print('Congrats! You got the job')
            self.job = job

        else:
            print('You are not experienced enough')


    def buy_home(self, home):
        if home.price <= self.money:
            print('Congrats! You bough this house!')
            self.house = home
            home.humans.append(self)
            self.money -= home.price
        else:
            print('Looks like you do not enough money :(')

class Doctor:
    def hospital(self, money):
        if self.money >= 5:
            print('Go on, the doctor is waiting for you')
        else:
            print('You do not have enough money')


    def doctor(self, health):
        if self.health <= 100:
            print('You have to take medecine and stay at home')
        else:
            print('You are healthy')



class Home:
    def __init__(self, price):
        self.furniture = []
        self.humans = []
        self.price = price

    def __str__(self):
        return f'Home for {self.price}'

class Job:
    def __init__(self, salary, name):
        self.salary = salary
        self.name = name
        self.timetable = None


bob = Person(27, 'Bob', 20000)
villa = Home(15000)
print(bob.house, villa.humans)

bob.buy_home(villa)

print(bob.house, villa.humans, bob.money)



person1 = Person(15, 'Bob', 1000)
person2 = Person(18, 'Ann', 2500)

print(person1)
print(person2)


class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sleep = 0


    def to_sleep(self):
        self.sleep += 10


class Student(Human):

    def study(self):
        self.sleep -= 10


class Restaurant(Home):

    def work(self):
        if len(self.humans) != 0:
            self.humans[0].money += 1000