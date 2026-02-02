#!/usr/bin/env python3
"""Module to change topics on a document based on the name"""

def update_topics(mongo_collection, name, topics):
    """Change topics on a document based on the name"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})