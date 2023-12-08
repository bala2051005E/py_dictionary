dummy_data = [
    {"Name": "John", "ID": 0, "Age": 25, "Skills": ["Programming", "Analysis"]},
    {"Name": "Sarah", "ID": 1, "Age": 30, "Skills": ["Marketing", "Communication"]},
    {"Name": "Alex", "ID": 2, "Age": 22, "Skills": ["Design", "Creative"]},
    {"Name": "Emily", "ID": 3, "Age": 28, "Skills": ["Data Analysis", "Research"]},
    {"Name": "Michael", "ID": 4, "Age": 35, "Skills": ["Leadership", "Strategy"]},
    {"Name": "Olivia", "ID": 5, "Age": 26, "Skills": ["Writing", "Editing"]},
    {"Name": "Ethan", "ID": 6, "Age": 32, "Skills": ["Project Management", "Teamwork"]},
]


ID = 5

for i in dummy_data:
    if ID == i["ID"]:
        print(i)
