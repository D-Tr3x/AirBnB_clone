#!/usr/bin/python3
""" Defines the command interpreter for HBNB """

import cmd
from models.base_model import BaseModel
from models import storage


global_cls = {
    "BaseModel": BaseModel,
}


class HBNBCommand(cmd.Cmd):
    """ Command interpreter for HBNB """

    prompt = '(hbnb) '
    intro = "Welcome to the HBNB command interpreter."\
        " Type help or ? to list commands.\n"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program on EOF (CTRL+D)"""
        print()
        return True

    def emptyline(self):
        """Prevents empty lines from executing"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of the class.

        Usage: create <class name>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in global_cls:
            print("** class doesn't exist **")
            return
        new_instance = global_cls[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.

        Usage: show <class name> <id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in global_cls:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes a instance based on the class name and id.

        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in global_cls:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.

        Usage:(1) all
              (2) all <class name>
        """
        args = arg.split()
        result = []
        if len(args) > 0 and args[0] not in global_cls:
            print("** class doesn't exist **")
            return

        for key, obj in storage.all().items():
            if len(args) == 0 or key.startswith(f"{args[0]}."):
                result.append(str(obj))
        print(result)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating an attribute.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in global_cls:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        instance = storage.all()[key]
        attr_name = args[2]
        attr_value = eval(args[3])

        setattr(instance, attr_name, attr_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
