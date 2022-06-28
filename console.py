#!/usr/bin/env python3
""" module that contains the command interpreter """
import cmd

class HBNBCommand(cmd.Cmd):
    """ defines command interpreter class """
    prompt = '(hbnb)'

    def do_quit(self, args):
        """ exits the command interpreter """
        'Quit command to exit the program\n'
        exit()

    def do_EOF(self, args):
        """ exits the command interpreter """
        'Quit command to exit the program\n'
        exit()

    def postcmd(self, stop, line):
        """ continues command interpreter after help """
        if cmd.Cmd.do_help:
            HBNBCommand().cmdloop()


if __name__ == '__main__':
    HBNBCommand().cmdloop()