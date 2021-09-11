
def greet():
  print("hello")
  print("namaste")
  print("ola")


def greet_with_position(name,location):
  print(f"hello {name}")
  print(f"what is it like in {location}?")

greet_with_position("pankaj","Nepal")


def greet_with_keyword(name,location):
  print(f"hello {name}")
  print(f"what is it like in {location}?")

greet_with_keyword(location="france", name="robin")
