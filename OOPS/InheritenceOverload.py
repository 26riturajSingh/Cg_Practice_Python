class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} says: ")

class Dog(Animal):

    def __init__(self, name):
        # Call parent constructor properly
        super().__init__(name)

    def sound(self):
        # Optionally call parent behavior first
        super().sound()
        print("Bow!")


d = Dog("Dog")
d.sound()