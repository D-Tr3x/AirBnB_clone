#!/usr/bin/python3
""" Defines the command interpreter for HBNB """

import cmd


class HBNBCommand(cmd.Cmd):
    """ Command interpreter for HBNB """

    prompt = '(hbnb) '
    intro = "Welcome to the HBNB command interpreter."\
        "Type help or ? to list commands.\n"

    def emptyline(self):
        """Prevents empty lines from executing"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program on EOF (CTRL + D)"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
