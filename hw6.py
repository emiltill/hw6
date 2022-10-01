import re

class Data:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value


person = []
obj_list = []

with open("MOCK_DATA.txt", "r", encoding='UTF-8') as data:
    lines = data.readlines()
    for line in lines:
        fullname = re.findall(r"(?:^[A-Z][a-z-]+\s[A-Za-z-'. ]+)", line)
        fullname = " ".join(fullname)
        email = re.findall(r"(?:[a-z\d]+@[a-z\d-]+\.[a-z\.]+)", line)
        email = ' '.join(email)
        filename = re.findall(r"(?:[A-Z][a-zA-Z]*\.[a-z\d]+)", line)
        filename = ' '.join(filename)
        color = re.findall(r"(?:#[\da-z]+)", line)
        color = " ".join(color)
        data = Data(fullname, email, filename, color)
        obj_list.append(data)

for obj in obj_list:
    with open("fullname.txt", 'a') as f:
        f.write(obj.full_name+"\n")
    with open("email.txt", 'a') as e:
        e.write(obj.email+"\n")
    with open("file.txt", 'a') as file:
        file.write(obj.file_name+"\n")
    with open("color.txt", 'a') as colors:
        colors.write(obj.color + "\n")
















