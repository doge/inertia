# inertia
a simple cli menu library for python

## features
* arrow based navigation
* easy to use

## things to add
* sub menus
* clearing cli on new item select [cmd]
* colors

## usage
```python
import inertia

def hello():
    print("Hello")

def world():
    print("World")

inertia.add_item("hello", hello)
inertia.add_item("world", world)
inertia.add_item("hello world", 'print("hello world")')
inertia.display()
```
