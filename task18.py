# items()` yordamida barcha juftliklarni chiqar. Har bir kalitni katta harflarda chiqarsin:

# ```python
# name → Ali  → NAME → Ali

student = {
    "name": "Ali", 
    "age": 25, 
    "grade": "A"
}
for key, value in student.items():
    print(f"{key} → {value}  → {key.upper()} → {value}")