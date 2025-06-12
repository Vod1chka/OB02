# Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы, помимо обычных данных пользователей,
# имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.

# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).

# 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`. Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров `User`).

# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User():
    def __init__(self, id, name, access_level = "user"):
        self.__id = id # Приватный атрибут
        self.__name = name # Приватный атрибут
        self._access_level = access_level # Защищенный атрибут

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self._access_level

    def info(self):
        info = f"ID: {self.__id}, Name: {self.__name}, Access Level: {self._access_level}"
        return info

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name, access_level = "admin")
        self.__user_list = []

    def add_user(self, user):
        if isinstance(user, User) and user.get_access_level() != "admin":
            if user not in self.__user_list:
                self.__user_list.append(user)
                print(f"Пользователь {user.get_name()} добавлен.")
            else:
                print("Пользователь уже существует.")
        else:
            print("Нельзя добавить администратора или неверный тип объекта.")

    def remove_user(self, user):
        if user in self.__user_list and user.get_access_level() != "admin":
            self.__user_list.remove(user)
            print(f"Пользователь {user.get_name()} удалён.")
        else:
            print("Пользователь не найден или является администратором.")

    def list_users(self):
        if not self.__user_list:
            return "Список пользователей пуст."
        return "\n".join(user.info() for user in self.__user_list)



admin1 = Admin(1, "Vod1chka")
print(admin1.info())

print(admin1.list_users())

user1 = User(2, "Пользователь 1")
user2 = User(3, "Пользователь 2")
admin1.add_user(user1)
admin1.add_user(user2)

print(admin1.list_users())

admin1.remove_user(user1)

print(admin1.list_users())