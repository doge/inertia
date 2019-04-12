import replit
from getch import getch

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
  

class main_menu(object):
  def __init__(self, title, color, indicator):

    self.title = title
    self.color = color
    self.indicator = indicator

    self.items = {}
    self.labels = []
    self.current = 0

  def add_sub(self, label, init):
    self.labels.append(label)
    self.items[init] = sub_menu

  def add_item(self, label, function):
    self.labels.append(label)
    self.items[label] = function

  def populate(self):
    print(colors["white"] + self.title)
    for x in range(0, len(self.items)):
      if x == self.current:
          print("%s\t%s %s%s" % (colors[self.color], self.indicator, self.labels[x], colors["white"]))
      else:
          print("%s\t %s" % (colors["white"], self.labels[x]))

  def render(self):
    replit.clear()
    self.populate()
    while True:
      key = ord(getch())
      if key == 65: # When the up arrow key is pressed,
        if self.current > 0:
          self.current -= 1
        else:
          self.current = 0
        replit.clear()
        self.populate()
      elif key == 66: # When the down arrow key is pressed,
        if self.current >= 0 and self.current < len(self.items) - 1:
          self.current += 1
        else:
          self.current = len(self.items) - 1
        replit.clear()
        self.populate()
      elif key == 67: # When the right arrow key is pressed,
        try:
          if isinstance(list(self.items.keys())[self.current], list(self.items.values())[self.current]):
            replit.clear()
            list(self.items.keys())[self.current].render()
        except:
          if callable(list(self.items.values())[self.current]):
            replit.clear()
            list(self.items.values())[self.current]()
            print("The function has finished executing. Press any of the arrow keys to go to the main menu.")
          else:
            print("The function you have entered is not callable.")
      elif key == 68: # When the left arrow key is pressed,
          replit.clear()
          self.populate()


class sub_menu(object): # find a better way to do this
  def __init__(self, title, color, indicator):

    self.title = title
    self.color = color
    self.indicator = indicator

    self.items = {}
    self.labels = []
    self.current = 0

  def add_sub(self, label, init):
    self.labels.append(label)
    self.items[init] = sub_menu

  def add_item(self, label, function):
    self.labels.append(label)
    self.items[label] = function

  def populate(self):
    print(colors["white"] + self.title)
    for x in range(0, len(self.items)):
      if x == self.current:
          print("%s\t%s %s%s" % (colors[self.color], self.indicator, self.labels[x], colors["white"]))
      else:
          print("%s\t %s" % (colors["white"], self.labels[x]))
    print("To go back to the main menu, press %s<--%s twice." % (colors[self.color], colors["white"]))

  def render(self):
    replit.clear()
    self.populate()
    while True:
      key = ord(getch())
      if key == 65: # When the up arrow key is pressed,
        if self.current > 0:
          self.current -= 1
        else:
          self.current = 0
        replit.clear()
        self.populate()
      elif key == 66: # When the down arrow key is pressed,
        if self.current >= 0 and self.current < len(self.items) - 1:
          self.current += 1
        else:
          self.current = len(self.items) - 1
        replit.clear()
        self.populate()
      elif key == 67: # When the right arrow key is pressed,
        try:
          if isinstance(list(self.items.keys())[self.current], list(self.items.values())[self.current]):
            replit.clear()
            list(self.items.keys())[self.current].populate()
        except:
          if callable(list(self.items.values())[self.current]):
            replit.clear()
            list(self.items.values())[self.current]()
            print("The function has finished executing. Press any of the arrow keys to go to the main menu.")
          else:
            print("The function you have entered is not callable.")
      elif key == 68: # When the left arrow key is pressed,
        replit.clear()
        break
