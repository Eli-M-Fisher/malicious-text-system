import os
import time
from pymongo import MongoClient
from confluent_kafka import Producer

class Retriever:
    """
    This class connects to mongodb Atlas, fetches documents,

    and publishes them into kafka topics based on classification
    """

    def __init__(self):
        # are i read environment variables (no hardcoding!)

        # and setup mongodb connection

        # setup kafka producer

        print("Retriever initialized successfully")

    def fetch_documents(self, limit=100):
        """
        now fetch oldest documents from mongodb based on timestamp
        """
        return list(cursor)

    def publish_to_kafka(self, documents):
        """
        and publish documents to kafka based on antisemitic flag
        """


    def run(self):
        """
        now i run the retriever loop (fetch every 60 seconds).
        """