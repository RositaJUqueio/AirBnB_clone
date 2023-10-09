<h1 align="center">AirBnB clone</h1>

<h2 align="center">Description</h2>
<p>This project is the first step towards building a full web application: an AirBnB clone. It involves creating a command interpreter to manage AirBnB objects.</p>

<h2 align="center">Console</h2>
<p>The console is a command interpreter that allows users to interact with a program using text commands. It facilitates various operations on AirBnB objects. Here are some of its key functionalities:</p>
<ul>
  <li><strong>Create:</strong> Create new AirBnB objects, such as users, states, cities, places, and more, using the interpreter.</li>
  <li><strong>Retrieve:</strong> Retrieve objects from files, databases, or other sources and work with them within the interpreter.</li>
  <li><strong>Operations:</strong> Perform various operations on objects, including counting them, computing statistics, and more.</li>
  <li><strong>Update:</strong> Modify attributes of an existing object.</li>
  <li><strong>Destroy:</strong> Delete an object when it is no longer needed.</li>
</ul>

<h2 align="center">Using The Console</h2>
The console can be run both interactively and non-interactively. 

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
Non-interactive mode
``````
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
``````







