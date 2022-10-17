class Guest:
    def __init__(self, first_name,second_name,city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance
    def __str__(self):
        return f'''"{self.first_name} {self.second_name}". {self.city}. Баланс: {self.balance} руб.'''

    def get_guest(self):
        return f'{self.first_name} {self.second_name},г. {self.city}'
guest_1 = Guest('Смирнов','Сергей','Москва',200)
guest_2 = Guest('Андрей','Макаров','Кострома',150)
guest_3 = Guest('Анна','Иванова','Новосибирск',100)

guest_list=[guest_1,guest_2,guest_3]
print(guest_1, guest_2, guest_3)

for guest in guest_list:
    print(guest.get_guest())
