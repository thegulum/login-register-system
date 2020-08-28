db = []


class User:
    def __init__(self, _name, _surname, _username, _password):
        self.name = _name
        self.surname = _surname
        self.username = _username
        self.password = _password

    def show_user(self):
        print(f"Sizin adınız {self.name}, soyadınız isə {self.surname}.")


print(type(open("demo.txt", "w")))

i = 1


def melumatlari_al_qeydiyyat():
    global i
    x = int(input("İstifadəçilərin sayını qeyd edin : "))
    while i <= x:
        input_name = input("Adınızı daxil edin : ")
        input_surname = input("Soyadınızı daxil edin : ")
        input_username = input("İstifadəçi adınızı daxil edin : ")
        input_password = input("Şifrənizi daxil edin : ")
        db.append(User(input_name, input_surname, input_username, input_password))
        i += 1

    return db


melumatlari_al_qeydiyyat()


def show_data():
    for user in db:
        user.show_user()


show_data()


def show_data_by_name():
    data_by_name = input("Adı daxil edin : ")
    for istifadeci in db:
        if data_by_name == istifadeci.name:
            istifadeci.show_user()


def show_longest_name():
    if len(db) == 0:
        print("İstifadəçi yoxdur!")
    else:
        longest_name = " "
        for user in db:
            if len(user.name) > longest_name:
                longest_name = user.name


show_longest_name()
