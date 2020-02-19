#!/usr/bin/python3
'''
Contains entry point of command interpretter
'''
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

Class_Dict = {"BaseModel": BaseModel,
              "User": User,
              "Place": Place,
              "State": State,
              "Amenity": Amenity,
              "Review": Review,
              "City": City}


class HBNBCommand(cmd.Cmd):
    '''
    console class
    '''
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel,
               "User": User,
               "Place": Place,
               "State": State,
               "Amenity": Amenity,
               "Review": Review,
               "City": City}

    def do_quit(self, command):
        '''
        Quit command to exit the program
        '''
        exit()

    def help_quit(self):
        '''
        Help for quit
        '''
        print('Quit command to exit the program\n')

    def do_EOF(self, command):
        '''
        End of file
        '''
        print()
        exit()

    def help_EOF(self):
        '''
        Help for EOF
        '''
        print('EOF command to exit the program\n')

    def emptyline(self):
        '''
        Guard against 'enter'
        '''
        pass

    def do_create(self, args):
        '''
        Create new instance of BaseModel
        '''
        if not args:
            print('** class name missing **')
            return
        elif args in Class_Dict:
            for key, value in Class_Dict.items():
                if key == args:
                    new_instance = Class_Dict[key]()
            storage.save()
            print(new_instance.id)
        else:
            print("** class doesn't exits")

    def help_create(self):
        '''
        Help for create
        '''
        print('Create command to create new instance\n')

    def do_show(self, args):
        '''
        Print str repr of an instance
        bases on class name and id
        '''
        new_instance = args.partition(' ')
        class_name = new_instance[0]
        class_id = new_instance[2]

        if not args:
            print('** class name missing **')
            return
        if class_name not in Class_Dict:
            print("** Class doesn't exitst **")
            return
        if not class_id:
            print('** instance id missing **')
            return
        new_key = class_name + '.' + class_id
        try:
            print(storage._FileStorage__objects[new_key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        '''
        Help for show
        '''
        print('Show command to show string representation\n')

    def do_destroy(self, arg):
        '''
        Deletes an instance basesd on
        class name and id
        '''
        new_args = arg.split(" ")
        class_name = new_args[0]
        class_id = new_args[1]
        if not class_name:
            print('** class name missing **')
        elif class_name not in Class_Dict:
            print("** class doesn't exist **")
        elif not class_id:
            print("** instance id missing **")
        else:
            new_key = class_name + '.' + class_id
            try:
                del(storage._FileStorage__objects[new_key])
                storage.save()
            except KeyError:
                print("** no instance found **")

    def help_destroy(self):
        '''
        Help for destroy
        '''
        print('Destroy command to show delete an instance based\
        on class name and id\n')

    def do_all(self, arg):
        """
        Prints all instances based on class
        """
        new_list = []

        if arg:
            if arg not in Class_Dict:
                print("** class doesn't exsist **")
                return
            for key, value in storage._FileStorage__objects.items():
                if key.split(".")[0] == arg:
                    new_list.append(str(value))
        else:
            for key, value in storage._FileStorage__objects.items():
                new_list.append(str(value))
        print(new_list)

    def help_all(self):
        """
        displays all instances [based on class if chosen]
        """
        print("displays all instances [based on class if chosen]")
        print("all [class]")

    def do_update(self, args):
        """
        updates object
        """
        new_object = args.split(" ")
        class_name = new_object[0]
        class_id = new_object[1]
        at_name = new_object[2]
        at_val = new_object[3]
        objects = storage._FileStorage__objects.items()
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in Class_Dict:
            print("** class doesn't exsist **")
            return
        if not class_id:
            print("** instance id missing **")
            return
        if not at_val:
            print("** value missing **")
            return
        if not at_name:
            print("** attribute name missing **")
            return
        new_key = class_name + "." + class_id
        no_touchy = ["id", "created_at", "updated_at"]
        try:
            for key, value in storage._FileStorage__objects.items():
                if new_key not in no_touchy:
                    if new_key == key:
                        setattr(value, at_name, at_val)
                        storage.save()
        except KeyError:
            pass

    def help_update(self):
        """
        Help for update
        """
        print("updates and objects with new information")
        print("update <class> <id> <attribute> <value>")

    def do_count(self, arg):
        """
        count number of instances by class
        """
        counter = 0

        new_arg = arg.split(" ")
        if new_arg[0] not in Class_Dict:
            print("** class doesn't exsist **")
            return
        new_list = storage._FileStorage__objects.items()
        for key, value in new_list:
            temp_key = str(key)
            new_key = temp_key.split(".")
            if new_key[0] == new_arg[0]:
                counter = (counter + 1)
        print(counter)

    def help_count(self):
        """
        counts the number of instances of a class
        """
        print("count <class>")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
