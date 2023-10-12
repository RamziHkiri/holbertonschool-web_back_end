#!/usr/bin/env python3
"""Provide stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == '__main__':
    con = MongoClient('mongodb://localhost:27017').logs.nginx
    print(f'{con.count_documents({})} logs')
    print('Methods:')
    print(f'\tmethod GET: {con.count_documents({"method": "GET"})}')
    print(f'\tmethod POST: {con.count_documents({"method": "POST"})}')
    print(f'\tmethod PUT: {con.count_documents({"method": "PUT"})}')
    print(f'\tmethod PATCH: {con.count_documents({"method": "PATCH"})}')
    print(f'\tmethod DELETE: {con.count_documents({"method": "DELETE"})}')
    print(f'{con.count_documents({"path": "/status"})} status check')
