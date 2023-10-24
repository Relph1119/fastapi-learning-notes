from mongoframes import Frame
from pymongo import MongoClient


def create_db_client():
    Frame._client = MongoClient('mongodb://localhost:27017/obrs')


def disconnect_db_client():
    Frame._client.close()
