#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 07:21:39 2024

@author: dominickmarqu_snhu
"""

from pymongo import MongoClient
from pymongo.cursor import Cursor

class AnimalShelter():
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        self.USER = USER
        self.PASS = PASS
        #USER = 'aacuser'
        #PASS = '<my_password>'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30712
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        self.fields = {
            'animal_type':0,
            'breed':0,
            'sex_upon_outcome':0,
            'age_upon_outcome_in_weeks':0
            }
        
# create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data) #data should be dictionary
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
# read method to implement the R in CRUD
    def read(self, query):
        if query is not None:
            cursor = self.database.animals.find(query)
            return list(cursor)
        else:
            raise Exception("Nothing to read, because query parameter is empty")
            
# readAll method
    def readAll(self, query: str = None) -> Cursor:
        #return self.database.animals.find(query, {"_id": False})
        return self.database.animals.find(query, {"_id": False})
# update method to implement the U in CRUD
    def update(self, query, update_data):
        if query is not None:
            result = self.database.animals.update_many(query, {"$set": update_data})
            return f"Modified {result.modified_count} document(s) from the collection"
        else:
            raise Exception("Nothing to update, because query parameter is empty")

#delete method to implement the D in CRUD
    def delete(self, query):
        if query is not None:
            result = self.database.animals.delete_many(query)
            return f"Removed {result.deleted_count} document(s) from the collection"
        else:
            raise Exception("Nothing to delete, because query parameter is empty")
            