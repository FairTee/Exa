#!/usr/bin/python3

"""This module defines the HBNBCommand class."""
import cmd
import json
import re
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    valid_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "Amenity": Amenity,
        "City": City,
        "Review": Review,
        "State": State
        }
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """when two arguments involve"""
        print('\n'.join(["Quit command to exit the program"]))

    def emptyline(self):
        """ Do nothing on emptyline"""
        pass

    def do_create(self, arg):
        """Creates a new instances of a class"""
        if arg:
            try:
                glo_cls = globals().get(arg, None)
                obj = glo_cls()
                obj.save()
                print(obj.id)
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        class name and id.
        """
        arr = arg.split()
        if len(arr) < 1:
            print("** class name missing **")
            return
        elif arr[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        elif len(arr) < 2:
            print("** instance id missing **")
            return
        else:
            new_s = f"{arr[0]}.{arr[1]}"
            if new_s not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[new_s])

    def do_destroy(self, arg):
        """Destroy command deletes an instance based on the class name and id
        """
        arr = arg.split()
        if len(arr) < 1:
            print("** class name missing **")
        elif arr[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(arr) < 2:
            print("** instance id missing **")
        else:
            new_s = f"{arr[0]}.{arr[1]}"
            if new_s not in storage.all().keys():
                print("** no instance found **")
            else:
                storage.all().pop(new_s)
                storage.save()

    def do_all(self, arg):
        """ Print all instances in string representation """
        if arg == "":
            print([str(value) for value in storage.all().values()])
        else:
            s = arg.split(" ")
            if s[0] not in self.valid_classes:
                print("** class doesn't exist **")
            else:
                class_instances = [
                    str(value)
                    for key, value in storage.all().items()
                    if key.startswith(f"{s[0]}.")
                ]
            print(class_instances)

    def do_update(self, arg):
        """Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        """
        arr = arg.split()
        if len(arr) < 1:
            print("** class name missing **")
            return
        elif arr[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        elif len(arr) < 2:
            print("** instance id missing **")
            return
        else:
            new_s = f"{arr[0]}.{arr[1]}"
            instances = models.storage.all()

            if new_s not in instances.keys():
                print("** no instance found **")
            elif len(arr) < 3:
                print("** attribute name missing **")
                return
            elif len(arr) < 4:
                print("** value missing **")
                return
            else:
                try:
                    setattr(instances[new_s], arr[2], arr[3])
                    instances[new_s].save()
                except Exception as e:
                    print(e)

    def do_count(self, arg):
        """Print the count all class instances"""
        do_class = globals().get(arg, None)
        if do_class is None:
            print("** class doesn't exist **")
            return
        class_count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == arg:
                class_count += 1
        print(class_count)

    def default(self, arg):
        if arg is None:
            return

        cmdPattern = r"^([A-Za-z]+)\.([a-z]+)\(([^()]*)\)"
        paramsPattern = r"""^"([^"]+)"(?:,\s*(?:"([^"]+)"|(\{[^}]+\}))"
                   (?:,\s*(?:("?[^"]+"?)))?)?"""
        n = re.match(cmdPattern, arg)
        if not n:
            super().default(arg)
            return
        nName, method, params = n.groups()
        n = re.match(paramsPattern, params)
        params = [item for item in n.groups() if item] if n else []

        cmd = " ".join([nName] + params)

        if method == 'all':
            return self.do_all(cmd)

        if method == 'count':
            return self.do_count(cmd)

        if method == 'show':
            return self.do_show(cmd)

        if method == 'destroy':
            return self.do_destroy(cmd)

        if method == 'update':
            return self.do_update(cmd)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
