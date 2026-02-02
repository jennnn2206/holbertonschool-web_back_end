#!/usr/bin/env python3
"""Module to insert a new document in a collection"""

def insert_school (mongo_collection, **kwargs): 
    """Inserts a new document in a MongoDB collection"""
    result = collection.insert_one(kwargs)
    return (result.inserted_id)