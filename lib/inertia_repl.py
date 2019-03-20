import getch, os, replit
from subprocess import call

current = 0
items = {}

def separator():
    print("-----------------------")

def add_item(name, function):
    items[name] = function


def render():
  for x in range(0, len(items)):
      if x == current:
          print("[*] %s" % list(items.keys())[x])
      else:
          print("[ ] %s" % list(items.keys())[x])

def display():
  global current
  replit.clear()
  render()
  while True:    
      key = ord(getch.getch())
      if key == 66:
          if current <= 0:
            current = current + 1
          else:
            current = len(items) - 1
          replit.clear()
          render()
      elif key == 65: 
          if current > 0:
              current = current - 1
          else:
              current = 0
          replit.clear()
          render()
      elif key == 67:
        separator()
        if callable(list(items.values())[current]):
            list(items.values())[current]()
        else:
            eval(list(items.values())[current])
        separator()
