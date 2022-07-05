![65f4a1dd9c51265f49d0](https://user-images.githubusercontent.com/85242327/177227053-d5c9852c-714d-4f48-9766-493ae324f43a.png)

# 0x00. AirBnB clone - The console

## First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine

# What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object


# How to start the console

Run the comand:


<img width="113" alt="Screen Shot 2022-07-04 at 8 10 09 PM" src="https://user-images.githubusercontent.com/85242327/177227282-53b0c6b2-fe12-4a8a-a686-3b9d7a79fb81.png">

After running the console file it will show the promt of the terminal:


<img width="72" alt="Screen Shot 2022-07-04 at 8 21 38 PM" src="https://user-images.githubusercontent.com/85242327/177227869-baf651e2-c5d4-4cd5-bf41-506c8c9da256.png">


# Commands for the console

Type 'help' to show the avalible commands:


<img width="372" alt="Screen Shot 2022-07-04 at 8 28 17 PM" src="https://user-images.githubusercontent.com/85242327/177228324-f3866982-d213-4aca-b6e2-32bfd1f5baff.png">


Type 'quit' to exit the console:


<img width="399" alt="Screen Shot 2022-07-04 at 8 31 13 PM" src="https://user-images.githubusercontent.com/85242327/177228409-6f2198e1-2c59-46c5-a424-1cbd20e6e4e9.png">


The 'create' command Creates a new instance of a class, saves it (to the JSON file) and prints the id:


<img width="399" alt="Screen Shot 2022-07-04 at 8 33 50 PM" src="https://user-images.githubusercontent.com/85242327/177228547-16d63960-4d76-4665-9e4a-eaeeb32e0be1.png">


The 'show' command prints the string representation of an instance based on the class name and id:


<img width="1129" alt="Screen Shot 2022-07-04 at 8 38 23 PM" src="https://user-images.githubusercontent.com/85242327/177228817-fcee616e-feb1-408a-a1b3-b260948594fb.png">


The 'all' command prints all string representation of all instances based or not on the class name:


<img width="1147" alt="Screen Shot 2022-07-04 at 8 47 42 PM" src="https://user-images.githubusercontent.com/85242327/177229339-7a19b275-0bd4-4b45-82d1-42c4086b267d.png">


The 'update' command updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file):


<img width="1132" alt="Screen Shot 2022-07-04 at 8 50 36 PM" src="https://user-images.githubusercontent.com/85242327/177229498-fb164385-e8f7-43dd-ad74-5e29e88257a9.png">


The 'destroy' command deletes an instance based on the class name and id (save the change into the JSON file):


<img width="434" alt="Screen Shot 2022-07-04 at 8 53 18 PM" src="https://user-images.githubusercontent.com/85242327/177229664-b16393eb-fae0-4528-b36c-0a23e1fdb400.png">
