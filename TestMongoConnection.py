import pymongo
import pandas as pd

from pymongo import MongoClient, errors


# use a try-except indentation to catch MongoClient() errors
try:
    # try to instantiate a client instance
    MONGO_URI = 'mongodb://CGLMONGODB:Hg78_Pt31@js01dp1x.ced.it:27017,js02dp1x.ced.it:27017,js03dp1x.ced.it:27017/admin?replicaSet=rsprod&ssl=true'
    client = pymongo.MongoClient(MONGO_URI, ssl=False)
    

    # print the version of MongoDB server if connection successful
    print ("server version:", client.server_info()["version"])

except errors.ServerSelectionTimeoutError as err:
    # set the client instance to 'None' if exception
    client = None

    # catch pymongo.errors.ServerSelectionTimeoutError
    print ("pymongo ERROR:", err)

db = client['c-dms']

query = {"COLLECTION" : "BUSTA_CASSA"}

cursor = db['stat.jobs'].find(query)

df =  pd.DataFrame(list(cursor))

print(df.head())
del df['_id']
print(df.head())

df.to_csv('c:\\temp\\out.csv', sep=';')