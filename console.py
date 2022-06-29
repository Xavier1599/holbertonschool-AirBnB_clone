#!/usr/bin/env python3
""" module that contains the command interpreter """
import cmd
import json

from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ defines command interpreter class """
    prompt = '(hbnb) '

    def do_create(self, args):
        'comment'
        if not args:
            print("** class name missing **")
        elif args != BaseModel.__name__:
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, args):
        rep = storage.all()
        arg_list = args.split()
        if not arg_list:
            print ("** class name is missing **")
        elif arg_list[0] != BaseModel.__name__:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif len(arg_list) > 1 or arg_list[2] != new.id:
            print("** no instance found **")
        else:
            for obj_id in rep.keys():
                if args[1] == rep[obj_id]:
                    print(obj_id)

    def do_quit(self, args):
        'Quit command to exit the program\n'
        exit()

    def do_EOF(self, args):
        'Quit command to exit the program\n'
        exit()

    def postcmd(self, stop, line):
        """ continues command interpreter after help """
        if cmd.Cmd.do_help:
            HBNBCommand().cmdloop()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
