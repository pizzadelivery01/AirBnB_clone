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
              "Review" : Review,
              "City" : City}


class HBNBCommand(cmd.Cmd):
    '''
    console class
    '''
    prompt = '(hbtn) '
    classes = {'BaseModel': BaseModel}

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
        elif class_name not in Class_Dict:
            print("** Class doesn't exitst **")
        elif len(new_instance) >= 1:
            try:
                new_objects = storage.all()
                new_key = class_name + '.' + class_id
                flag = 0
                for key, values in new_objects.items():
                    if key == new_key:
                        flag = 1
                        print(values)
                if flag == 0:
                    print("** no instance found **")
            except IndexError:
                print('** instance id missing **')

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
        new_args = arg.partition(" ")
        if not arg:
            print('** class name missing **')
        elif new_args[0] not in Class_Dict:
            print("** class doesn't exist **")
        elif len(new_args) <= 1:
            try:
                new_objects = storage.all()
                new_key = new_args[0] + '.' + new_args[1]
                try:
                    new_objects.pop(new_key)
                    storage.save()
                except KeyError:
                    print("** no instance found **")
            except IndexError:
                    print("** instance id missing **")

    def help_destroy(self):
        '''
        Help for destroy
        '''
        print('Destroy command to show delete an instance based\
        on class name and id\n')

    def do_all(self, arg):
        new_arg = arg.partition(" ")
        if not arg:
            new_list = []
            new_objects = storage.all()
            for key, values in new_objects.items():
                new_list.append(str(values))
            print(new_list)
        elif new_arg[0] not in Class_Dict:
            print("** Class doesn't exitst **")
        else:
            new_list = []
            new_objects = storage.all()
            for key, values in new_objects.items():
                new_key = key.split(".")
                if new_key[0] == new_arg[0]:
                    new_list.append(str(values))
                print(new_list)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
