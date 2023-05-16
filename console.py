#!/usr/bin/python3
"""module defines class HBNBCommand"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Implements an interactive command interpreter"""

    prompt = "(hbnb)"
    class_list = ["BaseModel", "User", "State",
                  "City", "Amenity", "Place",
                  "Review"]

    def emptyline(self):
        """Overwrite default behavior to repeat last cmd"""

        pass

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel,\
            saves it (to the JSON file) and prints the id
        """

        if arg:
            if arg in HBNBCommand.class_list:
                obj = eval(arg)()
                obj.save()
                print(f"{obj.id}")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
           Prints the string representation of \
           an instance based on the class name and id
        """

        size = len(arg)
        args = parse(arg)
        if size ==0:
            print("** class name missing **")
            return
        if size == 2:
            obj_id = f"{args[0]}.{args[1]}"
            if arg1 not in HBNBCommand.class_list:
                print("** class doesn't exist **")
            elif obj_id not in [k for k in storage.all().keys()]:
                print("** no instance found **")
            else:
                print(storage.all()[obj_id])
        elif size == 1:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """
           Deletes an instance based on the \
           class name and id (save the change into the JSON file)
        """

        args = arg.split()
        size = len(args)
        if size == 2:
            arg1, arg2 = args
            obj_id = f"{arg1}.{arg2}"
            if arg1 not in HBNBCommand.class_list:
                print("** class doesn't exist **")
            elif obj_id not in [key for key in storage.all().keys()]:
                print("** no instance found **")
            else:
                del storage.all()[obj_id]
                storage.save()
        elif size == 1:
            print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """
            Prints all string representation of all
            instances based or not on the class name
        """

        obj_list = []
        if arg:
            if arg not in HBNBCommand.class_list:
                print("** class doesn't exist **")
            else:
                for obj in storage.all().values():
                    if obj.__class__.__name__ == arg:
                        obj_list.append(f"{obj}")

                print(obj_list)
        else:
            for key in storage.all().keys():
                obj_list.append(f"{storage.all()[key]}")
            print(obj_list)

    def do_update(self, arg):
        """
           Updates an instance based on the class name and id by adding or
           updating attribute (save the change into the JSON file)
        """

        size = len(arg)
        args = arg.split()
        if size >= 4:
            arg1, arg2, arg3, arg4 = args
            obj_id = f"{arg1}.{arg2}"
            for k, obj in storage.all().items():
                if k == obj_id:
                    setattr(obj, arg3, eval(arg4))
                    obj.save()
        elif size == 3:
            print("** value missing **")
        elif size == 2:
            obj_id = f"{arg1}.{arg2}"
            if obj_id not in [k for k in storage.all().keys()]:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif size == 1:
            if arg1 not in HBNBCommand.class_list:
                print("** class doesn't exist **")
            else:
                printt("** instance id missing **")
        else:
            print("** class name missing **")

    def do_quit(self, arg):
        """Exits the program"""

        return True

    def do_EOF(self, arg):
        """Cleanly exits the interpreter"""

        print()
        return True


def parse(line):
    """Helper method to parse user typed input"""
    return tuple(line.split())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
