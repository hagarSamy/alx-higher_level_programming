#!/usr/bin/python3
'''A module to write a script
that adds all arguments to a
Python list, and then save
them to a file
'''
import json
import os
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


args = sys.argv[1:]

if os.path.isfile("add_item.json"):
    itemsToAdd = load_from_json_file("add_item.json")
else:
    itemsToAdd = []

allToAdd = itemsToAdd + args

save_to_json_file(allToAdd, "add_item.json")
