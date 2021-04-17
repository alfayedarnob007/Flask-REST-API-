import requests

BASE = "http://127.0.0.1:5000/"

# data = [
#     {"likes":15, "name":'Tea',"views":100},
#     {"likes":20, "name":'Tom',"views":1009},
#     {"likes":50, "name":'Tonny',"views":10890},
#     {"likes":10, "name":'Turner',"views":67000}       
# ]

# for i in range(len(data)):

#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print (response.json())

# input()

# response = requests.delete(BASE + "video/1")
# print (response)

# input()

response = requests.patch(BASE + "video/2",{"views":99,"likes":105})
print (response.json())