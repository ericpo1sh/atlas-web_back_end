#!/usr/bin/env python3
""" 10. Change school topics  """


def update_topics(mongo_collection, name, topics):
    ''' changes all topics of a school document based on the name '''
    topics_to_update = {"$set": {"topics": topics}}
    key_to_update = {"name": name}
    update = mongo_collection.update_one(key_to_update, topics_to_update)
    return update
