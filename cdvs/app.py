import curses
from curses import panel
from time import sleep

class Menu(object):

    def __init__(self, items, stdscreen):
        self.window = stdscreen.subwin(0,0)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.position = 0
        self.items = items
        self.items.append(('Exit','exit'))

    def navigate(self, n):
        self.position += n
        if self.position < 0:
            self.position = 0
        elif self.position >= len(self.items):
            self.position = len(self.items)-1

    def display(self):
        self.panel.top()
        self.panel.show()
        self.window.clear()

        while True:
            self.window.refresh()
            curses.doupdate()
            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                msg = '%d. %s' % (index, item[0])
                self.window.addstr(1+index, 1, msg, mode)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                if self.position == len(self.items)-1:
                    break
                else:
                    self.items[self.position][1](self.window)

            elif key == curses.KEY_UP:
                self.navigate(-1)

            elif key == curses.KEY_DOWN:
                self.navigate(1)
        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()

ideas = []
votes = {}
def add_idea(window):
    global ideas
    curses.echo()
    box = window.derwin(3,32,2,25)
    window.clear()
    window.refresh()
    box.box()
    idea = box.getstr(1,1,32)
    box.clear()
    ideas.append(idea)
    curses.noecho()

def print_idea(window):
    global ideas
    num = 1
    box = window.derwin(2 + len(ideas) ,32,3,25)
    box.box()
    for idea in ideas:
        box.addstr(num, 1, idea)
        num = num + 1
    window.refresh()

def vote_idea(window):
    global votes
    num = 1
    box = window.derwin(2 + len(ideas) ,32,3,25)
    box.box()
    for idea in ideas:
        box.addstr(num, 1, idea)
        num = num + 1
    num = 1
    for idea in ideas:
        curses.echo()
        vnum = box.getstr(num, 35, 2)
        curses.noecho()
        votes[idea] = vnum
    window.refresh()
    box.clear()

class MyApp(object):

    def __init__(self, stdscreen):
        self.screen = stdscreen
        curses.curs_set(0)

        main_menu_items = [
                ('Add idea', add_idea),
                ('Print ideas', print_idea),
                ('Vote ideas', vote_idea),
                ]
        main_menu = Menu(main_menu_items, self.screen)
        main_menu.display()
