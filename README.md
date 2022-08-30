Concepts
For this project, we expect you to look at these concepts:

Python packages
AirBnB clone

0x00. AirBnB clone - The console

![Nnenna](https://camo.githubusercontent.com/29aee5323f56eeaf0ca03669b3181f360af907609dc764ab1c5006815a03f4ff/68747470733a2f2f692e696d6775722e636f6d2f4a4f68615a356d2e706e67)

Background Context


This project works with a console that uses the cmd python module and a command interpreter that manages our AirBnb objects

First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine
What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object

Execution
Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

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
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

Data Diagram
![Rosita](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220830%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220830T162650Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6e1e526c1b4a9026a1d1bacd157f164b8980badaad867d63fa58b8abc628b47c)





