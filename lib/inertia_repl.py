import getch, replit

items = {}
current = 0
title_text = ""

current_color = ""
colors = {
  "black": "\033[1;30;1m",
  "red": "\033[1;31;1m",
  "green": "\033[1;32;1m",
  "yellow": "\033[1;33;1m",
  "blue": "\033[1;34;1m",
  "purple": "\033[1;35;1m",
  "cyan": "\033[1;36;1m",
  "white": "\033[1;37;1m"
}

def separator():
  print("-----------------------")

def color(col):
  global current_color
  current_color = col

def title(text):
  global title_text
  title_text = text

def add_item(name, function):
  items[name] = function

if current_color == "":
  current_color = "white"

def populate():
  if len(title_text) > 0:
    print(colors["white"] + title_text)
  for x in range(0, len(items)):
    if x == current:
      if len(title_text) > 0:
        print("%s\t> %s" % (colors[current_color], list(items.keys())[x]))
      else:
        print("%s> %s" % (colors[current_color], list(items.keys())[x]) + colors["white"])
    else:
        if len(title_text) > 0:
          print("%s\t %s" % (colors["white"], list(items.keys())[x]))
        else:
          print("%s %s" % (colors["white"], list(items.keys())[x]))

def render():
  global current, current_color
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
        print(colors["white"])
        separator()
        print("\t\toutput")
        separator()
        if callable(list(items.values())[current]):
            list(items.values())[current]()
        else:
            eval(list(items.values())[current])
        separator()
