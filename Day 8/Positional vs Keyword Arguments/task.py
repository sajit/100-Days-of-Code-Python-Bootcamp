# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")


def greet_with(name:str,location:str):
    print(f"Hello {name} and your location is {location}")


greet_with("Jack Baure","Neverland")

greet_with("Neverland","SD")
greet_with(location="Neverland",name="Joseph")