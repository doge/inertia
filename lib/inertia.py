import os
from msvcrt import getch
from subprocess import call

items = {}


def separator():
    print("-----------------------")


def clear():
    _ = call('clear' if os.name =='posix' else 'cls')


def add_item(name, function):
    items[name] = function


def display():
    current = 0
    while True:
        for x in range(0, len(items)):
            if x == current:
                print("[*] %s" % list(items.keys())[x])
            else:
                print("[ ] %s" % list(items.keys())[x])

        key = ord(getch())
        if key == 224:  # special keys
            key = ord(getch())
            if key == 80: # down arrow
                current = current + 1
                print(current)
            elif key == 72: # up arrow
                if current > 0:
                    current = current - 1
                else:
                    current = 0
                print(current)
            elif key == 77: # right arrow
              if callable(list(items.values())[current]):
                  list(items.values())[current]()
              else:
                  eval(list(items.values())[current])
            '''
            elif key == 75: # left arrow
                print('left')
            '''
