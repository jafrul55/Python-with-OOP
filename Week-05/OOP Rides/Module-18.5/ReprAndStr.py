class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Person('{self.name}',{self.age})"

    def __str__(self) -> str:
        return f"{self.name},{self.age}"

#instance:
person = Person("Jafrul",23)
print(repr(person))
print(str(person))