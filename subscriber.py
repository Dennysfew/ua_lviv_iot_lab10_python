class Subscriber:
    def __init__(self, phone_number: int, surname: str, name: str, middle_name: str, address: str):
        self.__phone_number = phone_number
        self.__surname = surname
        self.__name = name
        self.__middle_name = middle_name
        self.__address = address

    def __str__(self) -> str:
        return f'Surname: {self.__surname}\n' \
               f'Name: {self.__name}\n' \
               f'Middle name: {self.__middle_name}\n' \
               f'Address: {self.__address}\n' \
               f'Telephone: {self.__phone_number}\n'

    def get_surname(self):
        return self.__surname

    def get_phone_number(self):
        return self.__phone_number

    def __repr__(self) -> str:
        return self.__str__()