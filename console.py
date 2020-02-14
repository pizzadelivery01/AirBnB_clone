#!/usr/bin/python3
'''
Contains entry point of command interpretter
'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''
    console class
    '''
    prompt = '(hbtn) '

    def do_quit(self, command):
        '''
        Quit command to exit the program
        '''
        exit()

    def do_EOF(self, command):
        '''
        End of file
        '''
        exit()

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
