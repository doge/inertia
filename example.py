import inertia

'''
  colors:
    black, red, green, yellow, blue, purple, cyan, white
'''

def hello_world():
  print("hello world")

def world_hello():
  print("world hello")

main = inertia.main_menu("this is our first menu title", "red", ">") # (self, title, color, indicator)
main.add_item("hello world", hello_world)

sub = inertia.sub_menu("this is our second menu title", "blue", ">")
sub.add_item("hello world | sub (1)", hello_world)
sub.add_item("hello world | sub (2)", world_hello)
main.add_sub("sub-menu", sub)

main.render()
