sneakers = {"nike": "dunks", 
"jordan": "retros", 
"adidas": "yeezy"}
# print(sneakers["nike"]) # fetching data by key

sneakers["nike"] = "lebrons" # editing value
sneakers["new balance"] ="540's" #adding new key/values to dictionary 
# print(sneakers)

emptyDictionary = {} # empty dictionary 
# print(emptyDictionary)

# sneakers = {}
# print(sneakers)

# for key in sneakers:
#     print(key)
#     print(sneakers[key])

student_scores = {
    "Harry": 70,
    "Ron": 78,
    "Herminoe": 81,
    "Draco": 91,
    "Neville": 62
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 80:
        student_grades[student] = "good"
        

print(student_grades)