# ec2_info = {
#     "Name": "Jagadeesh",
#     "Age": 10,
#     "Weight": 34
# }

# ec2_info = [
#     {
#        "id": "ec2_instance-001",
#        "type": "t2.micro"
#     },
#     {
#         "id": "ec2_instance-002",
#         "type": "t2.medium"
#     },
#     {
#         "id": "ec2_instance-003",
#         "type": "t2.xlarge"
#     }
# ]

# print(ec2_info[1]["type"])

import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
output = response.json()
for element in range(len(output)):
    print(output[element]["user"]["login"])
