# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 20:09:14 2022

@author: I534329
"""

import os

class DBConnection:

    def getMyDb(self, db):
        # mongoURI = "mongodb://MY_MONGO_CONN:KubernetesRocks!@localhost:27017/my-db?authSource=admin"
        mongo_user = "MY_MONGO_CONN"
        mongo_password = "KubernetesRocks!"
        host = os.getenv('mongo_host', 'localhost')
        port = '27017'
        print(host + str(port))
        authSource = "authSource=admin"
        mongoURI = "mongodb://%s:%s@%s/%s?%s" % (mongo_user, mongo_password, host, db, authSource)
        return mongoURI