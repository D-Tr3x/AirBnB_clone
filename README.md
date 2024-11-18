# AirBnB clone - The Console


## Project Description

The goal of this project is to cretae a simple copy of the AirBnB website.
This project serves as a foundational step in understanding the core concepts
of higher-level programming, data modeling and application design. It includes:
 - A command-line interface (CLI) for data management
 - Essential functionalities for creating, updating, deleting and retrieving objects

This project will also evolve over time, implementing more complex features as we progress.



## Files and Directories:
   models/
    (directory) containing all classes in the project

        - base_model.py
           (file) base class of all models
            Attributes:
              `id` - unique identifier for each object
              `created_at` - timestamp when the object was created
              `updated_at` - timestamp when the object was last updated
            Methods:
              `save()` - updates `updated_at` with the current time
              `to_json()` - converts the object to a dictionary format

        - engine/
           (directory) containing all storage classes

                - file_storage.py
                  handles the storage of objects in a JSON file

   tests/
    (directory) containing all unit tests

   console.py
    (file) entry point of command-line interpreter



## The Command Interpreter

   Tool to interact with and manage objects in the system


   How to start it:
       ./console.py

   How to use it:
       (hbnb) create <class_name>
       (hbnb) show <class_name> <id>
       (hbnb) destroy <class_name <id>
       (hbnb) all <class_name>

   Examples:
       (hbnb) create BaseModel
       (hbnb) show BaseModel 1234-5678-9001
       (hbnb) destroy BaseModel 1234-5678-9001
       (hbnb) all BaseModel
