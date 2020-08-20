#!/usr/bin/env python
# coding: utf-8


import pymongo
import ssl
import pprint
import pandas as pd

MONGO_URI = 'mongodb://CGLMONGODB:Hg78_Pt31@js01dp1x.ced.it:27017,js02dp1x.ced.it:27017,js03dp1x.ced.it:27017/admin?replicaSet=rsprod&ssl=true'
client = pymongo.MongoClient(MONGO_URI, ssl=False)
print("Databases - " + str(client.list_database_names()))

pipeline = [
        {
            "$project": {
                    "year": {"$year": '$DATE_INSERT'},
                    "month": {"$month": '$DATE_INSERT'},
                    "dayOfMonth": {"$dayOfMonth": '$DATE_INSERT'},
              	 	"COLLECTION" : 1,
                    "DATE_INSERT" : 1,
                    "NUM_DOC" : 1
            	}
        },

        {
            "$group": {
                    "_id": {
                            "coll" : "$COLLECTION", 
                            "year": '$year',
                            "month": '$month',
                            "dayOfMonth" : '$dayOfMonth'
                    },
                    "total_doc" : { 
                        "$sum": "$NUM_DOC"
                    },
                    "total_job" : { 
                    	"$sum": 1
                    }                  
                }
        },

        {
            "$project": {
                    "collection": '$_id.coll',
                    "year": '$_id.year',
                    "month": '$_id.month',
                    "dayOfMonth": '$_id.dayOfMonth',
                    "total_doc" : 1,
                    "total_job" : 1,
                    "_id": 0
            }
        },
    ]

client.list_database_names()
#db = client.list_database_names()[1]
db = client['c-dms']

#print(list(client[db].stat.jobs.aggregate(pipeline)))
#pprint.pprint(list(client[db].stat.jobs.aggregate(pipeline)))

stat = str(list(db.stat.jobs.aggregate(pipeline)))
stat= stat.replace("'", '"')
df = pd.read_json(stat ,orient='records')

df.head()

import matplotlib.pyplot as plt

group_by_year = df.loc[:, ['year', 'total_doc', 'total_job']].groupby('year')
group_by_year.head()

avgs = group_by_year.mean()
x = avgs.index
print(x)
y1 = avgs.total_doc
print(y1)

def plot(x, y, ax, title, y_label):
    ax.set_title(title)
    ax.set_ylabel(y_label)
    ax.plot(x, y)
    ax.margins(x=0, y=0)

fig, ax = plt.subplots()
plot(x, y1, ax, 'Numero di documenti caricati', 'Numero documenti caricati')

plt.s

