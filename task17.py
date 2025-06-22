# Quyidagi dictni `for` loop orqali chiqar: `kalit → qiymat` ko‘rinishida.

# ```python
# student = {"name": "Ali", "age": 25, "grade": "A"}
# ```

student = {
    "name": "Ali", 
    "age": 25, 
    "grade": "A"
}

for key in student:
    print(key,"->",student[key])
