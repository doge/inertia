from lib import inertia_repl as inertia

# creating a sub menu is as easy as creating a menu. just add "sub_menu" as
# an argument and make sure it is a string.

def foo():
  print("bar")

def bar():
  print("foo")

m = inertia.menu("inertia", ">", "cyan")
s_m = inertia.menu("sub-menu", ">", "red", "sub_menu")

m.add_item("foo", foo)
m.add_item("second menu", s_m.render)

s_m.add_item("1st item", foo)
s_m.add_item("2nd item", bar)

m.render()
