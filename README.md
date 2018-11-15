# An AirBnB Console Clone
![Image of Holberton B&B Logo](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png)

## A Command Interpreter Project

### Contents
* [Project Description]
* [Technologies Used]
* [File Descriptions]
* [Console Commands]
* [Installation]
* [Command Usage]
* [Examples]
* [Authors]
---

### Project Description
This repository contains a working Console (CLI) that is modeled after the\
AirBnB application. This Console is the first part of making a complete 'Clone'\
of the AirBnB app.  The Console will be the interactive back-end of the\
application that can take care of initialization, serialization, and\
deserialization of any instances that are created.  It can create any classes\
that are used for AirBnB such as: User, State, City, Place, etc... It also\
creates an abstracted storage engine for the project. This repository also\
contains a Unittest that can be used to validate all classes made as well as\
the storage engine.

---

### Technologies Used
* Language: Python 3
* Operating System: Ubuntu 14.04 LTS (Trusty64)
* Style Guide: PEP8

---

### File Descriptions
---
#### Console Files:
| File | Description | Hierarchy |
| --------------- | -------------- |:--------------:|
| `console.py` | The main file for the console | [console.py](console.py) |
| `amenity.py` | The module for the Amenity Class | [models/amenity.py](models/amenity.py) |
| `base_model.py' | The module for the Base Model Class | [models/base_model.py](models/base_model.py) |
| `city.py` | The module for the City Class | [models/city.py](models/city.py) |
| `place.py` | The module for the Place Class | [models/place.py](models/place.py) |
| `review.py` | The module for the Review Class | [models/review.py](models/review.py) |
| `state.py` | The module for the State Class | [models/state.py](models/state.py) |
| `user.py` | The module for the User Class | [models/user.py](models/user.py)                    |
| `file_storage.py` | The module for the Storage Engine |\
[models/engine/file_storage.py](models/engine/file_storage.py) |

#### Unittest Files:
| -------------- |:--------------:|
| `test_amenity.py` | [tests/test_models/test_amenity.py](tests/test_models/test_amenity.py) |
| `test_base_model.py`   | [tests/test_models/test_base_model.py](tests/test_models/test_base_model.py) |
| `test_city.py` | [tests/test_models/test_city.py](tests/test_models/test_city.py) |
| `test_place.py` | [tests/test_models/test_place.py](tests/test_models/test_place.py) |
| `test_review.py` | [tests/test_models/test_review.py](tests/test_models/test_review.py) |
| `test_state.py` | [tests/test_models/test_state.py](tests/test_models/test_state.py) |
| `test_user.py` | [tests/test_models/test_user.py](tests/test_models/test_user.py) |
| `test_file_storage.py` | [tests/test_models/test_engine/test_file_storage.py](tests/test_models/test_engine/test_file_storage.py) |

---

### Installation
```
git@github.com:jogden4195/AirBnB_clone.git
```

---

### Console Commands
| Command | Description |
| ------------- |:-------------:|
| help | lists all documented commands |
| exit | exits the console |
| EOF | exits the console |
| all | Prints all string representations of all instances based or not on the class name |
| create | Creates a new instance of BaseModel and saves it to the JSON file |
| destroy | Deletes an instance based on the class name and id |
| show | Prints the string represenation of an instance based on the class name and id |
| update | Updates an instance based on the class name and id by adding or updating attribute |

---

### Command Usage

**create** - create <class name>
**show** - show <class name> <id>
**destroy** - destroy <class name> <id>
**all** - all or all <class name>
**update** - update <class name> <id> <attribute name> "<attribute value">
**quit** - quit
**EOF** - EOF / Ctrl - D / Ctrl - Z

---

### Examples
```
$ ./console.py

(hbnb) create User
4519fc05-a69b-4496-85fb-c0aebccd00b3

(hbnb) show User 4519fc05-a69b-4496-85fb-c0aebccd00b3
[User] (4519fc05-a69b-4496-85fb-c0aebccd00b3) {'updated_at': datetime.datetime(2018, 11, 15, 6, 55, 28, 570448), 'created_at': datetime.datetime(2018, 11, 15, 6, 55, 28, 570423), 'id': '4519fc05-a69b-4496-85fb-c0aebccd00b3'}

(hbnb) update User 4519fc05-a69b-4496-85fb-c0aebccd00b3 first_name Jenn

(hbnb) show User 4519fc05-a69b-4496-85fb-c0aebccd00b3
[User] (4519fc05-a69b-4496-85fb-c0aebccd00b3) {'first_name': 'Jenn', 'updated_at': datetime.datetime(2018, 11, 15, 6, 55, 28, 570448), 'created_at': datetime.datetime(2018, 11, 15, 6, 55, 28, 570423), 'id': '4519fc05-a69b-4496-85fb-c0aebccd00b3'}

(hbnb) all
["[User] (4519fc05-a69b-4496-85fb-c0aebccd00b3) {'first_name': 'Jenn', 'updated_at': datetime.datetime(2018, 11, 15, 6, 55, 28, 570448), 'created_at': datetime.datetime(2018, 11, 15, 6, 55, 28, 570423), 'id': '4519fc05-a69b-4496-85fb-c0aebccd00b3'}", "[BaseModel] (38eadc6a-1c05-4a5f-9c5e-66dfcd0671e2) {'id': '38eadc6a-1c05-4a5f-9c5e-66dfcd0671e2', 'updated_at': datetime.datetime(2018, 11, 15, 6, 51, 19, 138448), 'created_at': datetime.datetime(2018, 11, 15, 6, 51, 19, 138425), '__class__': 'BaseModel'}", "[User] (69a81cf3-d68c-4fe0-998c-ae511bf3e8b2) {'first_name': '=', 'updated_at': datetime.datetime(2018, 11, 15, 6, 53, 51, 705678), 'created_at': datetime.datetime(2018, 11, 15, 6, 53, 51, 705654), '__class__': 'User', 'id': '69a81cf3-d68c-4fe0-998c-ae511bf3e8b2'}", "[BaseModel] (e9616e57-12da-42d5-ade8-b0c6aba20bec) {'id': 'e9616e57-12da-42d5-ade8-b0c6aba20bec', 'updated_at': datetime.datetime(2018, 11, 15, 6, 51, 49, 563214), 'created_at': datetime.datetime(2018, 11, 15, 6, 51, 49, 563187), '__class__': 'BaseModel'}"]
(hbnb)
```
---

#### Authors
Jennifer Ogden & Joshua Jimenez