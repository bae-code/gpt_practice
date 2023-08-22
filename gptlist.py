import os
import openai
import json
import pymongo

client = pymongo.MongoClient()
db = client["chat_database"]
chat_collection = db["chat_history"]

openai.api_type = "azure"
openai.api_version = "2023-07-01-preview"
openai.api_base = ""  # Enter your endpoint here
openai.api_key = ""  # Enter your API key here

"""
"""

deployment_name = ""  # This will correspond to the custom name you chose for your deployment when you deployed a model.


a = (chat_collection.find({"session_id": 1})[1])
print(a)

