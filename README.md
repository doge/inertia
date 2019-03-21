# inertia
a simple cli menu library for python

## features
* [x] arrow based navigation
* [x] titles
* [x] easy to use

## things to add
* [x] clearing cli
* [x] colors
* [ ] ~~sub menus~~

## usage
```python
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
```
[requirements.txt](https://github.com/pain/inertia/blob/master/requirements.txt)
