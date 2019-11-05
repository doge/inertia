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

class menu(object):
  def __init__(self, title, indicator, color, *args):
    self.labels = []
    self.items = []
    self.selected = 0
    self.color = color
    self.indicator = indicator
    self.title = title
    self.extra_args = list(args)

  def add_item(self, label, function, *args):
    ''' 
      append the function and arguments to the 'items' list and then append the 'label' of the item to the 'labels' list
    '''
    self.items.append([function, args])
    self.labels.append(label);

  def __concatenate_string(self, string, color):
    ''' add a color to the string string and return the result '''
    return colors[color] + string + colors["white"]

  def __populate(self):
    ''' add colors to our string and return the result '''
    print(self.title)
    for x in range(0, len(self.labels)):
      if x == self.selected:
        print(" %s" % self.__concatenate_string(self.indicator + " " + self.labels[x], self.color))
      else:
        print(" ", self.labels[x])

  def render(self):
    '''
      we can populate the cli with labels and then use 'getch' to capture input given from the cli then handle the input
    '''

    self.__populate()
    while True:
      key = ord(getch.getch())
      # when w or up arw is pressed;
      if key == 119 and self.selected > 0 or key == 65 and self.selected > 0:
        self.selected -= 1
        self.__populate()
      # when s or dwn arw is pressed;
      elif key == 115 and self.selected < len(self.labels) - 1 or key == 66 and self.selected < len(self.labels) - 1:
        self.selected += 1
        self.__populate()
      # when d or right arw is pressed;
      elif key == 100 or key == 67:
        # let's execute the function if it has arguments
        if len(self.items[self.selected][1]) <= 0:
          self.items[self.selected][0]()
        else:
          self.items[self.selected][0](*self.items[self.selected][1])
      elif key == 97 or key == 68:
        if len(self.extra_args) > 0 and self.extra_args[0] == "sub_menu":
          break
        else:
          replit.clear()
          self.__populate()

      replit.clear()
