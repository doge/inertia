import inertia

def hello_world():
    print("Hello world!")

inertia.title("example title")
inertia.color("red")
inertia.add_item("hello_world", hello_world)
inertia.add_item("print('hello world')", "print('hello world')")
inertia.render()
