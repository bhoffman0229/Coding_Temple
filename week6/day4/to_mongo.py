# Imports
from base import Base
import pymongo
import os
from dotenv import load_dotenv

class ToMongo(Base):
    def __init__(self, user=os.getenv('USERNAME'), password=os.getenv('PASSWORD')):
        Base.__init__(self)
        load_dotenv()
        self.user = user
        self.password = password
        self.mongo_url = f'mongodb+srv://{self.user}:{self.password}@cluster0.ij5lejr.mongodb.net/?retryWrites=true&w=majority'
        #Connect to PyMongo
        self.client = pymongo.MongoClient(self.mongo_url)
        #Create a database
        self.db = self.client.database_names
        #Create a collection
        self.student = self.db.student
        #Set dataframe index to the id column
        self.df.set_index('id', inplace=True)

    def upload_one_by_one(self):

        for i in self.df.index:
            self.student.insert_one(self.df.loc[i].to_dict())

if __name__ == '__main__':
    c = ToMongo()
    print('Successful Connection to Client Object')
    c.upload_one_by_one()
    print('Successfully Uploaded all student Info to Mongo')
