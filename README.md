# inertia
a simple cli menu library for python

## features
* [x] arrow based navigation
* [x] sub-menus
* [x] colors
* [x] titles

## to-do
* [x] [repl.it](https://repl.it) support
* [ ] windows support
* [ ] osx support

## example
```python
from lib import inertia_repl as inertia

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
```
[requirements.txt](https://github.com/pain/inertia/blob/master/requirements.txt)
