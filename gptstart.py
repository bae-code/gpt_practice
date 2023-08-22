# Note: The openai-python library support for Azure OpenAI is in preview.
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



messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."}
    ]


question = ""
# Send a completion call to generate an answer
while question != "exit":

        
    question = input("질문을 입력하세요 : ")
    user_q = {"role": "user", "content": question}
    messages.append(user_q)

    response = openai.ChatCompletion.create(
        engine=deployment_name,  # The deployment name you chose when you deployed the GPT-35-Turbo or GPT-4 model.
        messages=messages,
    )

    print(response['choices'][0]['message']['content'])


    messages.append(response["choices"][0]["message"])

chat_collection.insert_one({"session_id": 1, "messages": messages})
