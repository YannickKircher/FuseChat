import requests
import json
import datetime

# Define the URL of the API endpoint
url = "http://localhost:5000/api/answer"

# Define the question to ask
question = "What is the capital of France? and why is it called the city of love? Write an essay!"

# Define the headers for the POST request
headers = {
    "Content-Type": "application/json"
}

# Define the body of the POST request
data = {
    "question": question
}

# Send the POST request to the API endpoint
response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)

# Print the response from the API as a stream
for chunk in response.iter_content(chunk_size=128):
    print(chunk.decode())
print(f"Finished streaming at {datetime.datetime.now()}")