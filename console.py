#!/usr/bin/python3
'''
Contains entry point of command interpretter
'''
from models.base_model import BaseModel
from models.__init__ import storage
import cmd


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
        elif args != BaseModel():
            baseModel_instance = BaseModel()
            print(baseModel_instance.id)

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

        if class_name not in HBNBCommand.classes:
            print('** class name missing **')
            return
        if not class_id:
            print('** instance id missing **')
            return

        key = class_name + '.' + class_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print('** no instance found **')

    def help_show(self):
        '''
        Help for show
        '''
        print('Show command to show string representation\n')

    def do_destroy(self, args):
        '''
        Deletes an instance basesd on
        class name and id
        '''
        new_instance = args.partition(' ')
        class_name = new_instance[0]
        class_id = new_instance[2]
        if not class_name:
            print('** class name missing **')
            return
        if not class_id:
            print('** instance id missing **')
            return

        key = class_name + '.' + class_id
        try:
            del (storage._FileStorage__objects[key])
        except KeyError:
            print('** no instance found **')

    def help_show(self):
        '''
        Help for destroy
        '''
        print('Destroy command to show delete an instance based\
        on class name and id\n')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
