#!/usr/bin/python3
'''
Serialized instances to a JSON file and deserializes
in JSON file to instances
'''
import json


class FileStorage:
    '''
    FileStorage class
    '''

    __file_path = "JSONstorage.json"
    __objects = {}

    def all(self):
        '''
        Returns the dictiornary
        '''

        return self.__objects

    def new(self, obj):
        '''
        Sets in __objects the obj with key
        <obj class name>.id
        '''
        key = str(type(self).__name__ + "." + obj.id)
        __objects[key] = obj

    def save(self):
        '''
        Deserializes the JSON file
        '''

        with open(self.__file_path, "w+") as write_file:
            json.dump(FileStorage.__objects, write_file)
        
    def reload(self):
        '''
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        '''

        with open(self.__file_path, "r") as read_file:
            FileStorage.__objects = json.load(read_file)
