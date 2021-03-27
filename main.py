# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from util.helper import process
from util.helper import Utility


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    name = process(name)
    return f'Hi, {name}'  # Press ⌘F8 to toggle the breakpoint.


def printer(name):
    # Use a breakpoint in the code line below to debug your script.
    name = Utility.process(name)
    return f'Hi, {name}'  # Press ⌘F8 to toggle the breakpoint.


def op(file):
    Utility.open_file(file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
