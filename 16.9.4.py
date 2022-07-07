class Clients:
    def __init__(self, name, last_name, city, balance):
        self.name = name
        self.last_name = last_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"{self.name} {self.last_name}.{self.city}.Баланс:{self.balance}."

    def get_guest(self):
        return f"{self.name} {self.last_name}.г.{self.city} "


client_1 = Clients("Иван", "Иванов", "Москва", 50)
client_2 = Clients("Маша", "Соколова", "Санкт-Петербург", 100)
client_3 = Clients("Петя", "Петров", "Саратов", 80)

guest_list = [client_1, client_2, client_3]

for guest in guest_list:
    print(guest.get_guest())
