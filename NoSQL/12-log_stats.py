#!/usr/bin/env python3
""" 12. Log stats """
from pymongo import MongoClient


def log_stats():
    ''' script that provides some stats about Nginx logs stored in MongoDB '''
    client = MongoClient()
    db = client.logs
    logs = db.nginx
    count_logs = logs.count_documents({})
    print(f'{count_logs} logs')
    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count_method = logs.count_documents({'method': method})
        print(f'\tmethod {method}: {count_method}')
    status = logs.count_documents({'method': 'GET', 'path': '/status'})
    print(f'{status} status check')


log_stats()
