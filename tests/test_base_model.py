#!/usr/bin/python3
import sys
import os
#get the current file's directory path
current_location=os.path.dirname(os.path.abspath(__file__))
#append to it .. in order to get the whole project directory
project_folder=os.path.abspath(os.path.join(current_location,'..'))
#add this path to sys.path 
sys.path.append(project_folder)
from models.base_model import BaseModel
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))