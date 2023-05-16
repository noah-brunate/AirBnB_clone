**Creation of a command interpreter to manage the hbnb projects**
## <p align="center">![alt text](https://github.com/Dikachis/AirBnB_clone/blob/main/web_static/images/65f4a1dd9c51265f49d0.png?raw=true)</p>

# :books: AirBnB Clone :pen:

## Description
> This is the first phase of the Airbnb Clone: the console.
> This repository holds a command interpreter and classes (i.e. BaseModel class
> and several other classes that inherit from it: `Amenity`, `City`, `State`, `Place`,
> `Review`, `User`), and a command interpreter. The command interpreter, like a shell,
> can be activated, take in user input, and perform certain tasks
> to manipulate the object instances.

## How to Use Command Interpreter
---
| Commands  | Sample Usage                                  | Functionality                              |
| --------- | --------------------------------------------- | ------------------------------------------ |
| `help`    | `help`                                        | displays all commands available            |
| `create`  | `create <class>`                              | creates new object (ex. a new User, Place) |
| `update`  | `User.update('123', {'name' : 'Greg_n_Mel'})` | updates attribute of an object             |
| `destroy` | `User.destroy('123')`                         | destroys specified object                  |
| `show`    | `User.show('123')`                            | retrieve an object from a file, a database |
| `all`     | `User.all()`                                  | display all objects in class               |
| `count`   | `User.count()`                                | returns count of objects in specified class|
| `quit`    | `quit`                                        | exits                                      |

## Installation
```
git clone git@github.com:MG-Musty/AirBnB_clone.git
cd AirBnB_clone
```
## Usage
Interactive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
## Functionalities and contents of Individual file that make up the Console
---
File                    | Method                       | Description
------------------------|------------------------------|----------------------
[console.py](https://github.com/robertokoba7/AirBnB_clone/blob/main/console.py) | command interpreter  | The starting point of the console functionality
|                       |  `quit`                      | It terminates the console and exit the program
|                       |  `help`                      | It gives information about a command line
|                       |  `<emptyline>`               | It loops the console when the user presses enter
|                       |  `create`                    | It creates a new instance of the BaseModel and saves it to JSON file
|                       |  `show`                      | It shows and prints the string representation of the instances created
|                       |  `destroy`                   | It deletes an instance based on the class name and id
|                       |  `all`                       | It prints all the string representation of all instances
|                       |  `update`                    | It updates an instance based on the class name and id by adding or updating an attribute
|                       |  `precmd`                    | fixes the command line to be interpretable for the console
|                       |  `prepare_dict`              | prepare a string to update an instance usign dictionaries
|                       |  `prepare_line`              | prepare the string to return an interpretable command line
| [base_model.py](https://github.com/robertokoba7/AirBnB_clone/blob/main/models/base_model.py) |  Instanciator | The BaseModel defines all common attributes/methos for other classes
|                       | `def __init__(self, *args, **kwargs)` | Initialization of BaseModel receiving commands line
|                       | `def save(self)`             | It saves new instances and updates attributes to a JSON file
|                       | `def to_dict(self)`          | It returns a dictionary containing all keys/values of an instance
|                       | `def __str__(self)`          | It prints the string representation of the BaseModel class
| [classes that inherits from BaseModel](https://github.com/robertokoba7/AirBnB_clone/blob/main/models) | `user.py`| It represents the user
|                       | `amenity.py`                 | It represents the amenity that the user requires
|                       | `city.py`                    | The city to visit
|                       | `place.py`                   | The place to stay
|                       | `review.py`                  | The critic of the place
|                       | `state.py`                   | The state of the city
| [file_storage.py](https://github.com/robertokoba7/AirBnB_clone/blob/main/models/engine/file_storage.py) | File storage  | It serializes instances to JSON file and deserializes JSON file to instances
|                      | `all`                         | It returns a dictionary of instances and attributes
|                      | `new`                         | It sets the object to a new instance and key into the dictionary
|                      | `save`                        | It serializes the dictionary to the JSON file
|                      | `reload`                      | It deserializes the JSON file to a directory

## Tests for our base files
---
You will be able to see the different tests and emphasis on certain methods, e.g: Creation of directories, instantiation, creation of classes and attributes, etc.
File                   | Method                        | Description
-----------------------|-------------------------------|-------------------------
[tests_console.py](https://github.com/robertokoba7/AirBnB_clone/blob/main/tests/console.py) | Test for the console | Checks how well the instantiation works
|                      | `test_base_pep8_conformance_console` | Test that we conform to PEP8
|                      | `base_pep8_conformance_consoletest`  | Test that we conform to PEP8 of the test itself
| [tests_base_model.py](https://github.com/robertokoba7/AirBnB_clone/blob/main/tests/test_models/test_base_model.py) | Test for the BaseModel Instantiator | Checks how well the instantiation works
|                      | `test_base_pep8_conformance_model`   | Test that we conform to PEP8
|                      | `base_pep8_conformance_basemodeltest`| Test that we conform to PEP8 of the test itself
|                      | `instances`                      | test instances creation
|                      | `test_time_attributes` | it tests the attribute of time
|                      | `test_id_assignment`| it tests the id assignment
|                      | `test_to_dict` | tests dictionary instance
|                   | `test__str__` | tests the printing
|      | `test_save` | tests the save instances
[test_models/](https://github.com/robertokoba7/AirBnB_clone#airbnb-project-link:~:text=the%20save%20instances-,test_models/,-test%20for%20classes)| test for classes | these tests checks for the same actions but the different attributes, they tend to be the same
[tests_city.py](https://github.com/robertokoba7/AirBnB_clone/blob/main/tests/test_models/test_city.py)| test city | tests Attr: name, state_id
[tests_place.py](https://github.com/robertokoba7/AirBnB_clone/blob/main/tests/test_models/test_place.py) | test place | tests attr: city_id,user_id, name, description, number_rooms,number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids
[tests_state.py](https://github.com/robertokoba7/AirBnB_clone/blob/main/tests/test_models/test_state.py)| test state | test attri: name
[tests_review.py](https://github.com/robertokoba7/AirBnB_clone/blob/main/tests/test_models/test_review.py) | test review | tests attr: place_id, user_id, text
[tests_user.py](https://github.com/robertokoba7/AirBnB_clone/blob/main/tests/test_models/test_user.py) | test user | tests attr: email, password, first_name, last_name
[tests_file_storage.py](https://github.com/robertokoba7/AirBnB_clone/blob/master/tests/test_models/test_engine/test_file_storage.py) | test for FileStorage class | This test will test the storage of info in json files
|                        | `test_all_dict_returned` | test the method all when returns dict
|                        | `test_file_storage_exist`| Checks if methods exists
|                        | `test_new`  | test the method new at the creation of new object
|                        | `test_User_saveStorage` | Checks if the save function works
|                       | `test save` | Test that save properly saves objects to file.json
|                       | `test_BaseModel_saveStorage` | Checks if the save function works
|                       | `test_base_pep8_conformance_file_storage`| Test that we conform to PEP8
|                         | `test_base_pep8_conformance_filesto_test` | Test that we conform to PEP8 of the test itself
|                       | `test_file_storage_docstring` | test docstring


## Environment
* Language: Python3
* OS: Ubuntu 20.04 LTS
* Style guidelines: [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/) \|| [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/l\atest/example_google.html) || [WC3 Validator](https://github.com/holbertonschool/W3C-Validator)

# :pen: Authors

Noah and Bruno
