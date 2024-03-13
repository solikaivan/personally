class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old. I am {self.gender}. Currently living in {self.address}.")


person1 = Person("Ivan", 20, "male", "Bamburi, Mtopanga, 1086")


person1.introduce()

