import getch, os, replit

current = 0
items = {}
title_text = ""

def separator():
  print("-----------------------")

def title(text):
  global title_text
  title_text = text

def add_item(name, function):
  items[name] = function

def populate():
  if len(title_text) > 0:
    print(title_text)
  for x in range(0, len(items)):
    if x == current:
      if len(title_text) > 0:
        print("\t[*] %s" % list(items.keys())[x])
      else:
        print("[*] %s" % list(items.keys())[x])
    else:
        if len(title_text) > 0:
          print("\t[ ] %s" % list(items.keys())[x])
        else:
          print("[ ] %s" % list(items.keys())[x])

def render():
  global current
  replit.clear()
  populate()
  while True:    
      key = ord(getch.getch())
      if key == 66:
          if current <= 0:
            current = current + 1
          else:
            current = len(items) - 1
          replit.clear()
          populate()
      elif key == 65: 
          if current > 0:
              current = current - 1
          else:
              current = 0
          replit.clear()
          populate()
      elif key == 67:
        separator()
        print("\t\toutput")
        separator()
        if callable(list(items.values())[current]):
            list(items.values())[current]()
        else:
            eval(list(items.values())[current])
        separator()
