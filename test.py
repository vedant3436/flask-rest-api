import requests

BASE = "http://127.0.0.1:5000/"

# data = [{'likes': 10, 'name':"csgo", 'views':69420},
#         {'likes': 57, 'name':"django", 'views':231314},
#         {'likes': 634, 'name':"flask", 'views':12314},
#         ]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())


response = requests.patch(BASE + "video/2", {"views": 99})
print(response.json())
