import inertia

def hello():
    print("Hello")

def world():
    print("World")

inertia.title("My Menu")
inertia.add_item("hello", hello)
inertia.add_item("world", world)
inertia.add_item("hello world", 'print("hello world")')
inertia.render()
