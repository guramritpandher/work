#APIs (Application Programming Interfaces) allow different software applications to communicate with each other.
'''Request: You send a request to the API endpoint (URL).
Response: The API returns a response (usually in JSON or XML format).'''

import requests
import json

# url="https://api.sunrisesunset.io/json?lat=38.907192&lng=-77.036873"
# response=requests.get(url)

# print("Status Code:", response.status_code)
# print("Response JSON:", response.json())

# json_data=response.json()
# print(json_data)

# dict_data=json.dumps(json_data)
# print(dict_data)


# data={
#     'name':'Guramrit',
#     'mid_name':'Kaur',
#     'surname':'Pandher',
#     'gender':'Female',
#     'age':23,
#     'email':'onal052001@gmail.com',
#     'number':'xxxxx00716'
# }

# # Write the dictionary to a JSON file
# with open("output.json", "w") as file:
#     json.dump(data, file, indent=4)


# # Open the JSON file and load its contents
# with open("output.json", "r") as file:
#     data = json.load(file)

# print(data)           
# print(data['name'])  


#GET
# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": "Learn APIs",
#     "body": "APIs are awesome!",
#     "userId": 1
# }

# response = requests.post(url, json=data)

# print("Status Code:", response.status_code)  
# print("Response JSON:", response.json())



#put
# Updated data
url = "https://jsonplaceholder.typicode.com/posts/1"
# updated_data = {
#     "title": "Updated Title",
#     "body": "Updated content!",
#     "userId": 1
# }

# response = requests.put(url, json=updated_data)

# print("Status Code:", response.status_code)  
# print("Response JSON:", response.json()) 



response = requests.delete(url)

print("Status Code:", response.status_code) 
print("Response Text:", response.text)