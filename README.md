# <center>0x00. AirBnB clone - The console</center>

## Background
This project is the first part ongoing Airbnb Clone.

In this project we are building the backend of the Airbnb. We created a Command Line Interpreter (CLI). This is similiar the the Shell project in C, but with Python's high level `cmd` framwork makes this as simple as importing `cmd` and beginning each function with `do_*`.

The command intepreter is written in the console.py file. It has several methods which allow us to manage the objects of the project:

* Create a new object (ex: a new User or * a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

The CLI is linked to several other classes:
* BaseModel
* User
* FileStorage
* amenity
* City 
* State
* Place
* Review

`BaseModel` is the parent class. It takes care of initiliazing, serializing and deserializing each instance.

The flow of the serialization and deserialization is:
`instantce <-> Dictionary <-> JSON string <-> file`

In file_storage.py we created a storage engine for the project. The methods for creating a new instance, saving and reloading it are in the `FileStorage` class.

## Use
Run the console:
```
./console.py
```
This is the start of the console:
```
(hbnb)
```
Type `help` for a list of commands:
```
(hnbn) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hnbn)        
```
Typing help followed by a command returns a useful text that describes the command, for example:
 ```
 (hnbn) help create
Create command to create new instance

(hnbn)
 ```
 To create a new instance, type `create` followed by a class name:
 ```
 (hnbn) create User
7a5014f4-f195-4698-9ae6-9de930fc0a25
 ```
 This returns a unique id, from the `UUID` import class. This unique number that is tagged to a instance. The `show` command displays a dictionary represntation of the object:
 ```
 (hnbn) show User 7a5014f4-f195-4698-9ae6-9de930fc0a25
[User] (7a5014f4-f195-4698-9ae6-9de930fc0a25) {'id': '7a5014f4-f195-4698-9ae6-9de930fc0a25', 'created_at': datetime.datetime(2020, 2, 18, 14, 34, 6, 879768), 'updated_at': datetime.datetime(2020, 2, 18, 14, 34, 6, 879782)}
 ```
 This saves a dictionary representation of the instance, which includes:
* Class name
* Unique ID number
* Created at (date/time)
* Updated at (date/time)

Further, the `destroy` method destroys the instance, so when we run it:
```
(hnbn) destroy User 7a5014f4-f195-4698-9ae6-9de930fc0a25
```
And try to `show` it again, we get this message:
```
** no instance found **
```
The instance has been deleted.

