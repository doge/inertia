# inertia
a simple cli menu library for python

## features
* [x] arrow based navigation
* [x] colors
* [x] titles
* [x] easy to use

## usage
```python
import inertia

def hello():
    print("Hello")

def world():
    print("World")

inertia.title("inertia")
inertia.color("red")
inertia.indicator(">")
inertia.add_item("hello", hello)
inertia.add_item("world", world)
inertia.add_item("hello world", 'print("hello world")')
inertia.render()
```
[requirements.txt](https://github.com/pain/inertia/blob/master/requirements.txt)
