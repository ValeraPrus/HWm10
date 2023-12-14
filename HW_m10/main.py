from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if isinstance(value, str) and value.isdigit() and len(value) == 10:
            self.value = value
        else:
            raise ValueError


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, numb):
        self.phones.append(Phone(numb))

    def remove_phone(self, numb):
        for phone in self.phones:
            if phone.value == numb:
                self.phones.remove(phone)

    def edit_phone(self, old_numb, new_numb):
        for phone in self.phones:
            if phone.value == old_numb:
                phone.value = new_numb
                break
        else:
            raise ValueError

    def find_phone(self, numb):
        for phone in self.phones:
            if phone.value == numb:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, \
                phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, name):
        self.data[name.name.value] = name

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
