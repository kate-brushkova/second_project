class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @classmethod
    def is_adult(cls, age):
        return age >= 18


print(Person.is_adult(1))
print(Person.is_adult())



