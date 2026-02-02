#!/usr/bin/env python3
"""Module to display nginx stats"""

from pymongo import MongoClient

if __name__ == "__main__":
    """Display nginx stats"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    c = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{c} status check")