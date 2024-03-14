def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"How are you doing, {name}?")
    print(f"What's your {location} for today?")


greet_with_name("Mastron", "Nowhere ")
#positional argument
greet_with_name("Mastron", "Nowhere ")


#keyword argument
greet_with_name(name="Mastron", location="Nowhere ")
greet_with_name( location="Nowhere ",name="Mastron")